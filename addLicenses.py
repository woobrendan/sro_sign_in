from utility.utility import getMostRecentDate, getAllId, filterEntriesById, addValuesToExcel
from licensing import fetch_licenses
import openpyxl

def handleNewLicenses():

    wb = openpyxl.load_workbook('./licensing/2024_Licenses.xlsx')

    sheet = wb['2024']
    recent_date = getMostRecentDate(sheet, "H")
    all_ids = getAllId(sheet)

    registrations = fetch_licenses(recent_date)

    filtered_reg = filterEntriesById(all_ids, registrations)

    count = addValuesToExcel(filtered_reg, sheet)

    print(f'{count} registrations have been added to the licensing document')

    wb.save(f'2024_Licsenes_updated.xlsx')