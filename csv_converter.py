import csv
import io

file_path = "./RA_entries.csv"


def csv_to_dict_arr(csv_file):
    csv_reader = csv.reader(io.TextIOWrapper(csv_file, encoding='utf-8'))
    headers = next(csv_reader)
    entries = []
    for row in csv_reader:
        entry_dict = dict(zip(headers, row))
        entries.append(entry_dict)
    return entries
