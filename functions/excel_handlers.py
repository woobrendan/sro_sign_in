from .utility import get_all_teams, series_long_name


def event_log(wb, series_entries):
    # Updates event logistics page of signin
    sheet = wb['Event_log']

    all_entries = get_all_teams(series_entries)

    current = 8

    for team_name in all_entries:
        sheet.cell(row=current, column=1, value=team_name)

        current += 1

    return wb

# {'Driver Designation': 'Pro - Am', 'Team Name': 'RealTime', 'number': '43', 'event': 'Road America', 'series': 'GTWCA', 'driver2': 'Adam Christodoulou', 'driver1': 'Anthony Bartone', 'NAT': 'USA'}
# take in array of dicts, where dict is shaped as above
# add in natinoality etc


def handle_single_driver(wb, series_entries):
    series = series_entries[0]['series']
    series_name = series_long_name(series)

    sheet = wb['series']

    current = 7

    for entry in series_entries:
        sheet.cell(row=current, column=1, value=series_name)
        sheet.cell(row=current, column=2, value=entry['number'])
        sheet.cell(row=current, column=3, value=entry['Team Name'])
        sheet.cell(row=current, column=4, value=entry['driver1'])
        sheet.cell(row=current, column=5, value=entry[''])
