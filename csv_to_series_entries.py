import csv
from functions.sortFuncs import sortBySeries
from functions.helpers import getSeries

# file_path = "./RA_entries.csv"
file_path = './entries_23.csv'

key_list = [
    '\ufeffCar Class',
    'Driver Designation',
    'Registered Car #',
    'Team Name',
    'Driver Name (First Name)',
    'Driver Name (Last Name)',
    # 'Nationality',
    # 'FIA Driver Categorization'
    '2nd Driver (First Name)',
    '2nd Driver (Last Name)',
    'Event Selection'
]

event = 'Road America'


def csv_to_dict_arr(csv_file_path, event):

    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        entries = []
        for row in csv_reader:
            entry_dict = dict(zip(headers, row))

            if entry_dict['Event Selection'] in [event, 'FULL SEASON ENTRY']:
                entries.append(entry_dict)

        # print(entries)
    return entries

# Only keep keys from key list, removing unused columns


def clean_results(arr, key_arr):
    entries = []
    for entry in arr:
        filtered = {key: entry[key] for key in key_arr if key in entry}
        entries.append(filtered)
    return entries


def change_key_name(dict_arr, event):
    for entry in dict_arr:
        # change full season or event name to event param
        entry['event'] = event
        del entry['Event Selection']

        if '\ufeffCar Class' in entry:
            entry['Car Class'] = entry.pop('\ufeffCar Class')

        if 'Registered Car #' in entry:
            entry["number"] = entry.pop('Registered Car #')

        if entry['Car Class'] in ['TCX', 'TC', 'TCA']:
            entry['series'] = 'TCAM'
            entry['Driver Designation'] = entry.pop('Car Class')
        else:
            entry['series'] = getSeries(entry['Car Class'])
            del entry['Car Class']

        driver1 = f"{entry.pop('Driver Name (First Name)', '')} {entry.pop('Driver Name (Last Name)', '')}".strip(
        )
        entry['driver1'] = driver1

        if '2nd Driver (First Name)' in entry and entry['2nd Driver (First Name)']:
            driver2 = f"{entry.pop('2nd Driver (First Name)', '')} {entry.pop('2nd Driver (Last Name)', '')}".strip(
            )
            entry['driver2'] = driver2
        else:
            entry.pop('2nd Driver (First Name)')
            entry.pop('2nd Driver (Last Name)')

    return dict_arr


def csv_to_series_entries(csv_file):
    dict_arr = csv_to_dict_arr(csv_file, event)
    cleaned = clean_results(dict_arr, key_list)
    changed_keys = change_key_name(cleaned, event)
    return sortBySeries(changed_keys)


csv_to_series_entries(file_path)