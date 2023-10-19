import csv_to_series_entries


def sort_by_num(entry):
    number = entry['number']
    return int(number.lstrip('#'))


def sortBySeries(entry_arr):
    series = {}
    for entry in entry_arr:
        series_name = entry['series']

        #  return array of entries if key exists, else return empty arr
        series_entries = series.get(series_name, [])
        series_entries.append(entry)
        series[series_name] = series_entries

    for series_name in series.keys():
        series[series_name].sort(key=sort_by_num)

    return series


def get_teams_carNums(entry_arr):
    teams = {}
    for entry in entry_arr:
        team_name = entry['Team Name']
        team_val = entry.get(team_name)

        if team_val:
            teams[team_name].append(entry['number'])
        else:
            teams[team_name] = [entry['number']]
    return teams


if __name__ == "__main__":
    csv_file = '../entries_23.csv'
    event_name = 'Sonoma Raceway'
    entries = csv_to_series_entries.csv_to_series_entries(csv_file, event_name)
    gtam_entries = entries['GTAM']

    print(get_teams_carNums(gtam_entries))
