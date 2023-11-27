from utility.csv_to_series_entries import csv_to_series_entries
from utility.create_drivers_signin import create_drivers_signin
from utility.create_manager_signin import create_manager_signin
from fetch_entries import fetch_entries
from

# Change variables accordingly
entries_csv = './entries_23.csv'
event_name = 'Road America'


# Use to create all sign in sheets

def event_signin(csv_file, event):
    # entries = csv_to_series_entries(csv_file, event)
    # create_manager_signin(entries, event)
    data = fetch_entries()
    sorted_entries = sortByEvent(data)
    create_drivers_signin(sorted_entries, event)


if __name__ == "__main__":
    event_signin(entries_csv, event_name)
