from functions.excel_handlers import handle_single_driver
from functions.csv_to_series_entries import csv_to_series_entries
import openpyxl


def event_entrylist(series_entries):
    wb = openpyxl.load_workbook('./templates/entry_list_template.xlsx')

    file_name = "Sonoma Provisional Entry List"

    for series in ['GTAM', 'TCAM']:
        entries = series_entries[series]

        handle_single_driver(wb, entries)
#
#    entries = series_entries['GTAM']
#
#    handle_single_driver(wb, entries)

    wb.save(f'./entry_lists/{file_name}.xlsx')


if __name__ == "__main__":
    event = "Sonoma Raceway"
    entries_csv = './entries_23.csv'
    entries = csv_to_series_entries(entries_csv, event)
    event_entrylist(entries)
