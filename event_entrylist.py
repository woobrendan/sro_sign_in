from functions.excel_handlers import handle_single_driver
import openpyxl


def event_entrylist(series_entries):
    wb = openpyxl.load_workbook('./templates/entry_list_template.xlsx')

    sheet = wb['GTAM']

    entries = series_entries['GTAM']
