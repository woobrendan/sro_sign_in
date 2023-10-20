import openpyxl
from csv_to_series_entries import csv_to_series_entries

csv_file = './entries_23.csv'
event_name = 'Sonoma Raceway'


def create_manager_signin(series_entries, event):
    wb = openpyxl.load_workbook('./signin_templates/manager_signin.xlsx')

    wb.save(f'manager__signin/{event}.xlsx')
