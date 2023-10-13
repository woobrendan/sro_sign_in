import csv
import io

file_path = "./RA_entries.csv"

key_list = [
    '\ufeffCar Class',
    'Driver Designation',
    'Registered Car #',
    'Team Name',
    'Driver Name (First Name)',
    'Driver Name (Last Name)',
    '2nd Driver (First Name)',
    '2nd Driver (Last Name)',
    'Event Selection'
]


def csv_to_dict_arr(csv_file):

    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        entries = []
        for row in csv_reader:
            entry_dict = dict(zip(headers, row))
            entries.append(entry_dict)
    return entries

# Only keep keys from key list, removing unused columns


def clean_results(arr, key_arr):
    entries = []
    for entry in arr:
        filtered = {key: entry[key] for key in key_arr if key in entry}
        entries.append(filtered)
    return entries


def getSeries(series_name):
    series = {
        'GT4 America': 'PGT4A',
        'GTWCA': 'GTWCA',
        'GTA': 'GTAM'
    }
    return series[series_name]


def change_key_name(dict_arr):
    for entry in dict_arr:
        if '\ufeffCar Class' in entry:
            entry['Car Class'] = entry.pop('\ufeffCar Class')

        if 'Registered Car #' in entry:
            entry["number"] = entry.pop('Registered Car #')

        if 'Event Selection' in entry:
            entry['event'] = entry.pop('Event Selection')

        if entry['Car Class'] in ['TCX', 'TC', 'TCA']:
            entry['series'] = 'TCAM'
            entry['Driver Designation'] = entry.pop('Car Class')
        else:
            entry['series'] = getSeries(entry['Car Class'])
            del entry['Car Class']

        if '2nd Driver (First Name)' in entry and entry['2nd Driver (First Name)']:
            driver2 = f"{entry.pop('2nd Driver (First Name)', '')} {entry.pop('2nd Driver (Last Name)', '')}".strip(
            )
            entry['driver2'] = driver2
        else:
            entry.pop('2nd Driver (First Name)')
            entry.pop('2nd Driver (Last Name)')

        driver1 = f"{entry.pop('Driver Name (First Name)', '')} {entry.pop('Driver Name (Last Name)', '')}".strip(
        )
        entry['driver1'] = driver1
    return dict_arr


def sortBySeries(entry_arr):
    series = {}
    for entry in entry_arr:
        series_name = entry['series']

        #  return array of entries if key exists, else return empty arr
        series_entries = series.get(series_name, [])
        series_entries.append(entry)
        series[series_name] = series_entries

    return series


def csv_to_clean_keys(csv_file):
    dict_arr = csv_to_dict_arr(csv_file)
    cleaned = clean_results(dict_arr, key_list)
    # return change_key_name(cleaned)
    changed_keys = change_key_name(cleaned)
    return sortBySeries(changed_keys)


# for testing GTWCA
def getWCEntries(csv_file):
    sorted_series = csv_to_clean_keys(csv_file)
    return sorted_series['GTWCA']


print(getWCEntries(file_path))
