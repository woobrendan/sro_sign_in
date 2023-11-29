import pandas as pd
import os
# from utility.csv_funcs.csv_to_series_entries import csv_to_all_entries
from fetch_entries import fetch_entries
from utility.sortFuncs import sortByEvent


# Pass in csv file of all entries, and filter by event, create excel file
def entries_by_event(event):
    data = fetch_entries()
    sorted_entries = sortByEvent(data)
    event_entries = sorted_entries[event]

    excel_file = f'event_entries/{event} entries.xlsx'

    data = pd.DataFrame(event_entries)
    data.to_excel(excel_file, index=False)


if __name__ == "__main__":
    event_name = 'Sonoma Raceway'
    entries_by_event(event_name)
