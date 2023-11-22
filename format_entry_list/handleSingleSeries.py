from format_entry_list.functions.utility import sortEntriesByClass, getSeriesShort


def handle_single_driver(wb, entries):
    first_entry = entries[0]
    series_short = getSeriesShort(first_entry['series'])

    sheet = wb[series_short]
    current = 7

    sort_arr = ['SRO3', 'GT2', 'GT4'] if series_short == 'GTAM' else [
        'TCX', 'TC', 'TCA']

    entries = sortEntriesByClass(entries, sort_arr)

    # Entry list title, event name and date
    event_name = first_entry['event']
    # Change date value accordingly
    date_str = 'April 5 - 7'
    sheet['D2'] = event_name
    sheet['D4'] = date_str

    for entry in entries:

        # entry['classif'] = 'SRO3' if series == 'GTAM' and entry['classif'] == 'GT3' else entry['classif']

        sponsor_col = 8 if series_short == 'GTAM' else 6
        vehicle_col = 9 if series_short == 'GTAM' else 7
        classif_col = 10 if series_short == 'GTAM' else 8

        sheet.cell(row=current, column=1, value=entry["series"])
        sheet.cell(row=current, column=2, value=entry['number'])
        sheet.cell(row=current, column=3, value=entry['team'])
        sheet.cell(row=current, column=4,
                   value=f'{entry["driver1firstName"]} {entry["driver1lastName"]}')
        sheet.cell(row=current, column=5, value=entry['driver1nationality'])
        sheet.cell(row=current, column=sponsor_col, value=entry['sponsors'])
        sheet.cell(row=current, column=vehicle_col, value=entry['car'])
        sheet.cell(row=current, column=classif_col, value=entry['class'])

        current += 1


# {
#    "series": "GT America",
#    "class": "SRO3",
#    "number": "3",
#    "team": "SKI Autosports",
#    "driver1firstName": "Johnny",
#    "driver1lastName": "O'Connell",
#    "driver1nationality": "USA",
#    "car": "audiR8Lms",
#    "manufacturer": "Audi",
#    "sponsors": "SKI Autosports"
# }
