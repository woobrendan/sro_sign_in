from format_sign_in.create_drivers_signin import create_drivers_signin
from format_sign_in.create_manager_signin import create_manager_signin
from utility.fetch_entries import fetch_entries
from utility.sortFuncs import sortByEvent, sortBySeries
from format_entry_list.test.test_entries import test_entries


# Use to create all sign in sheets

def event_signin(event):
    data = fetch_entries()
    sorted_entries = sortByEvent(data)
    event_entries = sorted_entries[event] + \
        sorted_entries['FULL SEASON ENTRY'] + test_entries

    class_entries = sortBySeries(event_entries)

    create_manager_signin(class_entries, event)
    create_drivers_signin(class_entries, event)


if __name__ == "__main__":
    event_name = 'Sonoma Raceway'
    event_signin(event_name)
