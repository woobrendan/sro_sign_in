import csv
import io

file_path = "./RA_entries.csv"


def csv_to_dict_arr(csv_file):

    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)
        entries = []
        for row in csv_reader:
            entry_dict = dict(zip(headers, row))
            entries.append(entry_dict)
    return entries


print(csv_to_dict_arr(file_path))
