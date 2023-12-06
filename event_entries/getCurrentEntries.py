import pandas as pd


headers = ['event', 'series', 'class', 'number', 'team', 'driver1firstName', 'driver1lastName', 'driver1nationality', 'driver1category',
           'driver2firstName', 'driver2lastName', 'driver2nationality', 'driver2category', 'sponsors', 'car', 'manufacturer', 'id', 'created']


def getCurrentEntries():
    data = pd.read_excel('./event_entries/master_entry_list.xlsx')

    results = []

    for index, row in data.iterrows():
        row_dict = {f'{headers[i]}': value for i, value in enumerate(row)}
        results.append(row_dict)

    return results
