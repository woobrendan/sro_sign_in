from format_sign_in.create_drivers_signin import create_drivers_signin
from format_sign_in.create_manager_signin import create_manager_signin
# from utility.fetch_event_entries import fetch_event_entries
from utility.sortFuncs import sortBySeries
from utility.convertEntry import convertEntry
from utility.fetch_mongo_entries import fetch_all_entries, fetch_event_entries


# Use to create all sign in sheets

def event_signin(event):
    data = fetch_event_entries(event)
    
    # converted = [convertEntry(entry) for entry in data]

    # class_entries = sortBySeries(converted)
    class_entries = sortBySeries(data)

    create_manager_signin(class_entries, event)
    create_drivers_signin(class_entries, event)


if __name__ == "__main__":
    event_name = 'Sebring International Raceway'
    event_signin(event_name)
