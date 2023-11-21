# Take in sort array of classes to sort by desired class
def sortEntriesByClass(entry_arr, sort_arr):
    entries = {}

    for entry in entry_arr:
        classif = entry['class']
        exists = entries.get(classif, [])
        exists.append(entry)

        entries[classif] = exists

    ordered = []
    # loop through SRO3, GT2, GT4 fetch val using key from entries and create one long arr
    for car_class in sort_arr:
        entries_arr = entries.get(car_class)
        if entries_arr:
            ordered += entries_arr

    return ordered


def getSeriesShort(series_name):
    series = {
        'GT4 America': 'PGT4A',
        'GT World Challenge America': 'GTWCA',
        'GT America': 'GTAM',
        'TC America': 'TCAM'
    }
    return series[series_name]
