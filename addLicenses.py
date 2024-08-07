from utility.utility import getAllId, filterEntriesById, addValuesToExcel
from utility.handle_dates import getMostRecentDate
from licensing.fetch_licenses import fetch_licenses
import openpyxl
import json

def handleNewLicenses():

    wb = openpyxl.load_workbook('../2024_Licenses.xlsx')

    sheet = wb['2024']
    recent_date = getMostRecentDate(sheet, "J")
    all_ids = getAllId(sheet, "I")

    registrations = fetch_licenses(recent_date)

    filtered_reg = filterEntriesById(all_ids, registrations)
    # order new registrants by date
    new_regs = sorted(filtered_reg, key=lambda x: x['created'])
    
    count = addValuesToExcel(new_regs, sheet)

    print(f'{count} registrations have been added to the licensing document')

    wb.save(f'../2024_Licenses_updated.xlsx')


if __name__ == "__main__":
    handleNewLicenses()