import pandas as pd


headers = ['event', 'series', 'class', 'number', 'team', 'driver1firstName', 'driver1lastName', 'driver1nationality', 'driver1category',
           'driver2firstName', 'driver2lastName', 'driver2nationality', 'driver2category', 'sponsors', 'car', 'manufacturer', 'id']


def getCurrentEntries():
    data = pd.read_excel('./master_entry_list.xlsx')

    results = []
