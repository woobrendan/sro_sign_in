import pandas as pd
import os
from csv_to_series_entries import csv_to_series_entries

# Change Variables here
csv_file = './entries_23.csv'
event_name = 'Sonoma Raceway'

# Pass in csv file of all entries, and filter by event, create excel file


def entries_by_event(csv_file, event):
    entries = csv_to_series_entries(csv_file, event)
    all_entries = []

    for series_entries in entries.values():
        all_entries.extend(series_entries)

    excel_file = f'event_entries/{event} entries.xlsx'

    data = pd.DataFrame(all_entries)
    data.to_excel(excel_file, index=False)


if __name__ == "__main__":
    entries_by_event(csv_file, event_name)
