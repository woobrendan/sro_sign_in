import pandas as pd
from csv_to_series_entries import csv_to_series_entries

# Change Variables here
csv_file = './entries_23.csv'
event_name = 'Sonoma Raceway'


def output_csv(csv_file, event):
    entries = csv_to_series_entries(csv_file, event)
    all_entries = []

    for series_entries in entries.values():
        all_entries.extend(series_entries)

    excel_file = 'output.xlsx'

    data = pd.DataFrame(all_entries)
    data.to_excel(excel_file, index=False)


if __name__ == "__main__":
    output_csv(csv_file, event_name)
