def handle_single_driver(wb, entries):
    first_entry = entries[0]
    series = first_entry['series']

    series_name = series_long_name(first_entry['series'])

    sheet = wb[series]
    current = 7

    sort_arr = ['GT3', 'GT2', 'GT4'] if series == 'GTAM' else [
        'TCX', 'TC', 'TCA']

    entries = sortEntriesByClass(entries, sort_arr)

    # Entry list title, event name and date
    event_name = first_entry['event']
    # Change date value accordingly
    date_str = 'April 5 - 7'
    sheet['D2'] = event_name
    sheet['D4'] = date_str

    for entry in entries:

        entry['classif'] = 'SRO3' if series == 'GTAM' and entry['classif'] == 'GT3' else entry['classif']

        sponsor_col = 8 if series == 'GTAM' else 6
        vehicle_col = 9 if series == 'GTAM' else 7
        classif_col = 10 if series == 'GTAM' else 8

        sheet.cell(row=current, column=1, value=series_name)
        sheet.cell(row=current, column=2, value=entry['number'])
        sheet.cell(row=current, column=3, value=entry['Team Name'])
        sheet.cell(row=current, column=4, value=entry['driver1'])
        sheet.cell(row=current, column=5, value=entry['NAT'])
        sheet.cell(row=current, column=sponsor_col, value=entry['sponsors'])
        sheet.cell(row=current, column=vehicle_col, value=entry['vehicle'])
        sheet.cell(row=current, column=classif_col, value=entry['classif'])

        current += 1
