from utility.fetch_entries import fetch_entries
from format_entry_list.handleSingleSeries import handle_single_driver
from format_entry_list.handleDualSeries import handle_dual_driver
from utility.sortFuncs import sortByEvent, sortBySeries
from format_entry_list.test.test_entries import test_entries
import openpyxl
from utility.fetch_mongo_entries import fetch_event_entries
import json
from utility.utility import series_long_name


def event_entrylist(event):
    wb = openpyxl.load_workbook('./templates/entry_list_template.xlsx')

    series_entries = sortBySeries(fetch_event_entries(event))
    # print(json.dumps(series_entries, indent=4))

    file_name = f"{event} Provisional Entry List"

    for series in ['GTAM', 'TCAM', 'GR Cup']:
        # series_long = series_long_name(series)
        entries = series_entries[series]
        handle_single_driver(wb, entries, event)

    for series in ['GTWCA', 'PGT4A']:
        # series_long = series_long_name(series)
        entries = series_entries[series]

        handle_dual_driver(wb, entries, event)

    wb.save(f'./entry_lists/{file_name}.xlsx')


if __name__ == "__main__":
    event = "Sebring International Raceway"
    # data = fetch_entries()
    # sorted_entries = sortByEvent(data)

    # sorted_entries[event] += sorted_entries['FULL SEASON ENTRY']

    # entries = sorted_entries.get(event)
    # series_entries = sortBySeries(entries)

    # event_entrylist(series_entries, event)
    event_entrylist(event)
