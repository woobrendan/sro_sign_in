from utility.utility import findFirstEmptyRow
import openpyxl


def master_entry_list():
    wb = openpyxl.load_workbook('')  # add in workbook template

# open master excel file
# take each row and convert into dict
# fetch responses
# filter for unique ids


# add those new entries to entry lists
def writeToExcel(entries):
    first = findFirstEmptyRow()

    for entry in entries:
        # find first empty row
        sheet.cell

# print out x new entries added
