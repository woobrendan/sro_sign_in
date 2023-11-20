# Take in sort array of classes to sort by desired class
def sortEntriesByClass(entry_arr, sort_arr):
    entries = {}

    for entry in entry_arr:
        classif = entry['class']
        exists = entries.get(classif)

        if exists:
            entries[classif].append(entry)
        else:
            entries[classif] = [entry]

    ordered = []
    for car_class in sort_arr:
        entry_arr = entries.get(car_class)
        if entry_arr:
            ordered += entry_arr

    return ordered


def getSeriesShort(series_name):
    series = {
        'GT4 America': 'PGT4A',
        'GT World Challenge America': 'GTWCA',
        'GT America': 'GTAM',
        'TC America': 'TCAM'
    }
    return series[series_name]
