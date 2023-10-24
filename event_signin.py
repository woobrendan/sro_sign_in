from functions import create_drivers_signin, create_manager_signin, csv_to_series_entries

# Change variables accordingly
entries_csv = './entries_23.csv'
event_name = 'Road America'


# Use to create all sign in sheets

def event_signin(csv_file, event):
    entries = csv_to_series_entries(csv_file, event)
    create_manager_signin(entries, event)
    create_drivers_signin(entries, event)


if __name__ == "__main__":
    event_signin(entries_csv, event_name)
