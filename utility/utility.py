def getSeries(series_name):
    series = {
        'GT4 America': 'PGT4A',
        'GTWCA': 'GTWCA',
        'GTA': 'GTAM'
    }
    return series[series_name]


def getSeriesShort(series_name):
    series = {
        'GT4 America': 'PGT4A',
        'GT World Challenge America': 'GTWCA',
        'GT America': 'GTAM',
        'TC America': 'TCAM',
        'Toyota GR Cup': 'GR Cup'
    }
    return series[series_name]


def series_long_name(series_name):
    series = {
        'GTWCA': 'FGTWCA',
        'PGT4A': 'GT4 America',
        'TCAM': 'TC America',
        'GTAM': 'GT America',
        'GRC': 'GR Cup'
    }

    return series[series_name]

# take in series_entries {'gtwca': [{entry}]} and return combined list of all entries removed duplicates


def get_all_teams(series_entries):
    all_entries = []

    for entries in series_entries.values():
        for entry in entries:
            all_entries.append(entry['Team Name'].strip())

    unique_teams = list(set(all_entries))

    return sorted(unique_teams)
