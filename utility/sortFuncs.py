import copy
from utility.convertEntry import convertEntry
from utility.events import events_dict
from utility.utility import getSeriesShort


def sort_by_num(entry):
    number = entry['number']
    return int(number.lstrip('#'))


def sortBySeries(entry_arr):
    series = {}
    for entry in entry_arr:
        series_short = getSeriesShort(entry['series'])

        #  return array of entries if key exists, else return empty arr
        series_entries = series.get(series_short, [])
        series_entries.append(entry)
        series[series_short] = series_entries

    for series_name in series.keys():
        series[series_name].sort(key=sort_by_num)

    return series


# 'Flying Lizard Motorsports': ['2', '8', '460'], 'Crowdstrike by Riley': ['04'], 'Blackdog Speed Shop': ['5'], 'DXDT Racing': ['08', '91']...}
# returns an array of tuples, ('Auto Technic Racing', ['51', '253'])
def get_teams_carNums(entry_arr):
    teams = {}
    for entry in entry_arr:
        team_name = entry['team']
        num = entry['number']

        exists = teams.get(team_name, [])
        exists.append(num)
        teams[team_name] = exists

    for team in teams.keys():
        unique_entries = list(set(teams[team]))
        teams[team] = sorted(unique_entries, key=lambda x: int(x.lstrip('#')))

    sorted_teams = sorted(teams.items())

    return sorted_teams


# Take in sort array of classes to sort by desired class
def sortEntriesByClass(entry_arr, sort_arr):
    entries = {}

    for entry in entry_arr:
        classif = entry['class']
        exists = entries.get(classif, [])
        exists.append(entry)

        entries[classif] = exists

    ordered = []
    # loop through SRO3, GT2, GT4 fetch val using key from entries and create one long arr
    for car_class in sort_arr:
        entries_arr = entries.get(car_class)
        if entries_arr:
            ordered += entries_arr

    return ordered


# take in api version of entry, convert to simplified dict. keys are event names, values are array of entries
def sortByEvent(all_entries):
    entry_event_dict = copy.deepcopy(events_dict)

    for entry in all_entries:
        event_name = entry['eventLabel']

        # convert entry into object entry list objs

        new_entry = convertEntry(entry)

        entry_event_dict[event_name].append(new_entry)

    return entry_event_dict
