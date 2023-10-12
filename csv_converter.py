import csv
import io

file_path = "./RA_entries.csv"

key_list = [
    'Car Class',
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


def clean_results(arr, key_arr):
    entries = []
    for entry in arr:
        filtered = {key: entry[key] for key in key_arr if key in entry}
        entries.append(filtered)
    return entries


def csv_to_clean_keys(csv_file):
    dict_arr = csv_to_dict_arr(csv_file)


print(csv_to_dict_arr(file_path))
