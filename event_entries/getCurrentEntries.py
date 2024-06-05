import pandas as pd
from event_entries.headers import headers


def getCurrentEntries():
    data = pd.read_excel('./event_entries/master_entry_list.xlsx')

    results = []

    for index, row in data.iterrows():
        row_dict = {f'{headers[i]}': value for i, value in enumerate(row)}
        results.append(row_dict)

    return results
