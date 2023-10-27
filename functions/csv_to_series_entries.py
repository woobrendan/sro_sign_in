import csv
from functions.sortFuncs import sortBySeries
from functions.utility import getSeries

sponsor_str = 'Team Sponsors - Please seperate each Sponsor with a comma'
key_list = [
    '\ufeffCar Class',
    'Driver Designation',
    'Registered Car #',
    'Team Name',
    'Driver Name (First Name)',
    'Driver Name (Last Name)',
    'Nationality',
    # 'FIA Driver Categorization',
    sponsor_str,
    '2nd Driver (First Name)',
    '2nd Driver (Last Name)',
    'Event Selection'
]

vehicle_types = ['GTWCA Car Make / Model',
                 'GTA Car Make/Model',
                 'GT4 Car Make/Model',
                 'TCX Car Make / Model',
                 'TC Car Make/Model',
                 'TCA Car Make/Model']


def csv_to_dict_arr(csv_file_path, event):

    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        entries = []
        for row in csv_reader:
            entry_dict = dict(zip(headers, row))

            if entry_dict['Event Selection'] in [event, 'FULL SEASON ENTRY']:
                entries.append(entry_dict)
    return entries

# Only keep keys from key list, removing unused columns


def clean_results(arr, key_arr):
    entries = []
    for entry in arr:
        filtered = {}
        for key in key_arr:
            if key in entry and entry[key]:
                filtered[key] = entry[key]

        entries.append(filtered)
    return entries


def change_key_name(dict_arr, event):
    for entry in dict_arr:
        # change full season or event name to event param
        entry['event'] = event
        del entry['Event Selection']

        # fix headers from csv to match needed output
        entry['Car Class'] = entry.pop('\ufeffCar Class')
        entry["number"] = entry.pop('Registered Car #')
        entry['NAT'] = entry.pop('Nationality')
        entry['sponsors'] = entry.pop(sponsor_str)

        if entry['Car Class'] in ['TCX', 'TC', 'TCA']:
            entry['series'] = 'TCAM'
            entry['Driver Designation'] = entry.pop('Car Class')
        else:
            entry['series'] = getSeries(entry['Car Class'])
            del entry['Car Class']

        driver1 = f"{entry.pop('Driver Name (First Name)', '')} {entry.pop('Driver Name (Last Name)', '')}".strip(
        )
        entry['driver1'] = driver1
        entry['classif'] = entry.pop('Driver Designation')

        if '2nd Driver (First Name)' in entry and entry['2nd Driver (First Name)']:
            driver2 = f"{entry.pop('2nd Driver (First Name)', '')} {entry.pop('2nd Driver (Last Name)', '')}".strip(
            )
            entry['driver2'] = driver2

        for key in vehicle_types:
            val = entry.get(key)
            if val:
                entry['vehicle'] = entry.pop(key)
                break

    return dict_arr


def csv_to_all_entries(csv_file, event):
    keys_list = key_list.copy()
    keys_list.extend(vehicle_types)

    dict_arr = csv_to_dict_arr(csv_file, event)
    cleaned = clean_results(dict_arr, keys_list)
    return change_key_name(cleaned, event)


def csv_to_series_entries(csv_file, event):
    all_entries = csv_to_all_entries(csv_file, event)

    return sortBySeries(all_entries)
