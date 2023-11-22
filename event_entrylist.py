# from functions.excel_handlers import handle_single_driver
from fetch_entries import fetch_entries
from format_entry_list.handleSingleSeries import handle_single_driver
from format_entry_list.functions.sortByEvent import sortByEvent
from format_entry_list.functions.sortByseries import sortBySeries
from format_entry_list.test.test_entries import test_entries
from functions.csv_to_series_entries import csv_to_series_entries
import openpyxl
import json


# def event_entrylist(series_entries):
#    wb = openpyxl.load_workbook('./templates/entry_list_template.xlsx')
#
#    file_name = "Sonoma Provisional Entry List"
#
#    for series in ['GTAM', 'TCAM']:
#        entries = series_entries[series]
#
#        handle_single_driver(wb, entries)
##
# entries = series_entries['GTAM']
##
# handle_single_driver(wb, entries)
#
#    wb.save(f'./entry_lists/{file_name}.xlsx')
#
#
# if __name__ == "__main__":
#    event = "Sonoma Raceway"
#    entries_csv = './entries_23.csv'
#    entries = csv_to_series_entries(entries_csv, event)
#    event_entrylist(entries)


# refactor using entries from API
def event_entrylist(series_entries):
    wb = openpyxl.load_workbook('./templates/entry_list_template.xlsx')

    file_name = "Sonoma Provisional Entry List"

    for series in ['GTAM', 'TCAM']:
        entries = series_entries[series]

        handle_single_driver(wb, entries)

    wb.save(f'./entry_lists/{file_name}.xlsx')


if __name__ == "__main__":
    event = "Sonoma Raceway"
    data = fetch_entries()
    sorted_entries = sortByEvent(data)

    # add in test data to sonoma
    sorted_entries['Sonoma Raceway'] = sorted_entries['Sonoma Raceway'] + test_entries

    entries = sorted_entries.get(event)
    series_entries = sortBySeries(entries)

    event_entrylist(series_entries)
