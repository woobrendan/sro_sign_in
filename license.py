from licensing.fetch_licenses import fetch_licenses
from licensing import handleNewLicenses
import json
import openpyxl

def license():
    wb = openpyxl.load_workbook('./licensing/2024_Licenses.xlsx')

    handleNewLicenses(wb)




if __name__ == '__main__':
    license()


