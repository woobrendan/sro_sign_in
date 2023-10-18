import pandas as pd
from csv_to_series_entries import csv_to_series_entries


# csv_file = './entries_23.csv'
csv_file = './RA_entries.csv'
event = 'Sonoma Raceway'


def output_csv(csv_file, event):
    entries = csv_to_series_entries(csv_file)
    excel_file = 'output.xlsx'

    data = pd.DataFrame(entries)
    data.to_excel(excel_file, index=False)


if __name__ == "__main__":
    output_csv(csv_file)
