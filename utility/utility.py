import openpyxl
from datetime import datetime, timedelta

def getSeriesShort(series_name):
    series = {
        'GT4 America': 'PGT4A',
        'GT World Challenge America': 'GTWCA',
        'GT America': 'GTAM',
        'TC America': 'TCAM',
        'Toyota GR Cup': 'GR Cup'
    }
    return series[series_name]


def series_long_name(series_name):
    series = {
        'GTWCA': 'FGTWCA',
        'PGT4A': 'GT4 America',
        'TCAM': 'TC America',
        'GTAM': 'GT America',
        'GRC': 'GR Cup'
    }

    return series[series_name]


# take in series_entries {'gtwca': [{entry}]} and return combined list of all entries removed duplicates
def get_all_teams(series_entries):
    all_entries = []

    for entries in series_entries.values():
        for entry in entries:
            all_entries.append(entry['team'].strip())

    unique_teams = list(set(all_entries))

    return sorted(unique_teams)


def findFirstEmptyRow(sheet):
    for cell in sheet["Q"]:
        if cell.value is None:
            return cell.row


def unique_id(entry, id_list):
    return entry['id'] not in id_list


def filterEntriesById(id_list, all_entries):
    return list(filter(lambda entry: unique_id(entry, id_list), all_entries))


def copy_font(font):
    new_font = openpyxl.styles.Font(
        name=font.name, sz=font.sz, b=font.b, color=font.color)
    return new_font


def copy_alignment(align):
    new_align = openpyxl.styles.Alignment(
        horizontal=align.horizontal, vertical=align.vertical)
    return new_align


def copy_border(border):
    new_border = openpyxl.styles.Border(
        left=border.left, right=border.right, top=border.top, bottom=border.bottom
    )
    return new_border

def getMostRecentDate(sheet, series):
    submit_dates = []

    column_id = 'R'

    column = sheet[column_id]

    for cell in column[1:]:
        if cell.value is not None:
            submit_dates.append(cell.value)
        else:
            break

    if submit_dates:
        # convert each date string into date obj, get max then return as str
        date_objs = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
                     for date in submit_dates]

        most_recent = max(date_objs)

        most_recent += timedelta(seconds=1)

        return most_recent.strftime('%Y-%m-%dT%H:%M:%SZ')
