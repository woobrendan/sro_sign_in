import openpyxl
from datetime import datetime, timedelta, date

def getSeriesShort(series_name):
    series = {
        'GT4 America': 'PGT4A',
        'Pirelli GT4 America': 'PGT4A',
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


def findFirstEmptyRow(sheet, var):
    for cell in sheet[var]:
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

def getAllId(sheet, column_id):
    ids = []

    column = sheet[column_id]

    for cell in column[1:]:
        if cell.value is not None:
            ids.append(cell.value)
        else:
            break  # exit loop when cell is empty

    return ids


def addValuesToExcel(regs, sheet):
    first_row = findFirstEmptyRow(sheet, 'A')

    if first_row is None:
        first_row = 2

    first_cell = sheet.cell(row=2, column=1)
    count = 0

    lic_headers = [
        "First Name",
        "Last Name",
        'Team',
        "Email",
        'TEXT  Number',
        "Date of Birth",
        "ticketType",
        'event',
        'Coupon Code',
        "id",
        "created",
    ]

    for reg in regs:
        count += 1

        for i, header in enumerate(lic_headers, start=1):
            new_cell = sheet.cell(row=first_row, column=i)
            val = reg.get(header, '')

            new_cell.value = val

            # set formatting of cell
            new_cell.font = copy_font(first_cell.font)
            new_cell.alignment = copy_alignment(first_cell.alignment)
            new_cell.border = copy_border(first_cell.border)

        first_row += 1

    return count