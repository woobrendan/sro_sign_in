import json
from event_entries.writeToMasterEntry import writeToMasterEntry
from event_entries.getCurrentEntries import getCurrentEntries
from utility.fetch_entries import fetch_entries
from utility.utility import filterEntriesById
from utility.convertEntry import convertEntry
import openpyxl


def master_entry_list():
    # open master excel file
    wb = openpyxl.load_workbook('./event_entries/master_entry_list.xlsx')
    sheet = wb["master"]

# take each row and convert into dict
    existing_entries = getCurrentEntries()
    existing_ids = [entry["id"] for entry in existing_entries]

# fetch responses
    api_entries = fetch_entries()
    converted = [convertEntry(entry) for entry in api_entries]

# filter for unique ids
    filtered_entries = filterEntriesById(existing_ids, converted)

# add those new entries to entry lists
    writeToMasterEntry(filtered_entries, sheet)

    wb.save(f'./event_entries/master_entry_list_latest.xlsx')


# print out x new entries added


if __name__ == "__main__":
    # entries = getCurrentEntries()
    # print(json.dumps(entries, indent=4))
    master_entry_list()
