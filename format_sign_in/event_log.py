from utility.utility import get_all_teams


def event_log(wb, series_entries):
    # Updates event logistics page of signin
    sheet = wb['Event_log']

    all_entries = get_all_teams(series_entries)

    current = 8

    for team_name in all_entries:
        sheet.cell(row=current, column=1, value=team_name)

        current += 1

    return wb
