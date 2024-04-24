from licensing.fetch_licenses import fetch_licenses
from licensing import handleNewLicenses
import json
import openpyxl

def license():
    wb = openpyxl.load_workbook('./licensing/2024_Licenses.xlsx')
    entries = fetch_licenses()
    print(json.dumps(entries, indent=4))

    # handleNewLicenses(wb, entries)




if __name__ == '__main__':
    license()


