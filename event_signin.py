from format_sign_in.create_drivers_signin import create_drivers_signin
from format_sign_in.create_manager_signin import create_manager_signin
from utility.fetch_event_entries import fetch_event_entries
from utility.sortFuncs import sortBySeries
from utility.convertEntry import convertEntry


# Use to create all sign in sheets

def event_signin(event):
    data = fetch_event_entries(event)
    
    converted = [convertEntry(entry) for entry in data]

    class_entries = sortBySeries(converted)

    create_manager_signin(class_entries, event)
    create_drivers_signin(class_entries, event)


if __name__ == "__main__":
    event_name = 'Sonoma Raceway'
    event_signin(event_name)
