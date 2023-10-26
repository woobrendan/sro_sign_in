def getSeries(series_name):
    series = {
        'GT4 America': 'PGT4A',
        'GTWCA': 'GTWCA',
        'GTA': 'GTAM'
    }
    return series[series_name]

# take in series_entries {'gtwca': [{entry}]} and return combined list of all entries removed duplicates


def get_all_teams(series_entries):
    all_entries = []

    for entries in series_entries.values():
        for entry in entries:
            all_entries.append(entry['Team Name'].strip())

    unique_teams = list(set(all_entries))

    return sorted(unique_teams)


def event_log(wb, series_entries):
    # Updates event logistics page of signin
    sheet = wb['Event_log']

    all_entries = get_all_teams(series_entries)

    current = 8

    for team_name in all_entries:
        sheet.cell(row=current, column=1, value=team_name)

        current += 1

    return wb
