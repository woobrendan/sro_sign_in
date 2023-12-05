import json
from event_entries.writeToMasterEntry import writeToMasterEntry
from event_entries.getCurrentEntries import getCurrentEntries
from utility.fetch_entries import fetch_entries
import openpyxl


def master_entry_list():
    # open master excel file
    wb = openpyxl.load_workbook('./event_entries/master_entry_list.xlsx')
    sheet = wb["master"]

# take each row and convert into dict
    existing_entries = getCurrentEntries()
# fetch responses
    api_entries = fetch_entries()
# filter for unique ids


# add those new entries to entry lists
    # writeToMasterEntry(entries, sheet)


# print out x new entries added


if __name__ == "__main__":
    entries = getCurrentEntries()
    print(json.dumps(entries, indent=4))
