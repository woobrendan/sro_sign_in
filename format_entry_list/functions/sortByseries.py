from format_entry_list.functions.utility import getSeriesShort
from utility.sortFuncs import sort_by_num


def sortBySeries(entry_arr):
    series = {}
    for entry in entry_arr:
        series_short = getSeriesShort(entry['series'])

        #  return array of entries if key exists, else return empty arr
        series_entries = series.get(series_short, [])
        series_entries.append(entry)
        series[series_short] = series_entries

    for series_name in series.keys():
        series[series_name].sort(key=sort_by_num)

    return series
