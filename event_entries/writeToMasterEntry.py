from utility.utility import findFirstEmptyRow, copy_alignment, copy_border, copy_font
from event_entries.headers import headers


def writeToMasterEntry(entries, sheet):
    first = findFirstEmptyRow(sheet)
    first_cell = sheet.cell(row=2, column=1)

    for entry in entries:

        for i, header in enumerate(headers, start=1):
            new_cell = sheet.cell(first, column=i)
            val = entry.get(header, '')

            new_cell.value = val

            new_cell.font = copy_font(first_cell.font)
            new_cell.alignment = copy_alignment(first_cell.alignment)
            new_cell.border = copy_border(first_cell.border)

        first += 1
