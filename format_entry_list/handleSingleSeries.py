from utility.sortFuncs import sortEntriesByClass
from utility.utility import getSeriesShort
from utility.events import sro_events


def handle_single_driver(wb, entries, event):
    first_entry = entries[0]
    series_short = getSeriesShort(first_entry['series'])

    sheet = wb[series_short]
    current = 7

    sort_arr = ['SRO3', 'GT2', 'GT4'] if series_short == 'GTAM' else [
        'TCX', 'TC', 'TCA'] if series_short != 'GR Cup' else ['Am']

    sorted_entries = sortEntriesByClass(entries, sort_arr)

    # Entry list title, event name and date
    sheet['D2'] = event
    sheet['D4'] = sro_events[event]

    for entry in sorted_entries:
        car_num = entry["number"]
        sponsors = entry.get('sponsors', "")

        if not car_num.startswith('0') and car_num.isdigit():
            car_num = int(car_num)

        sponsor_col = 8 if series_short == 'GTAM' else 6
        vehicle_col = 9 if series_short == 'GTAM' else 7
        classif_col = 10 if series_short == 'GTAM' else 8

        sheet.cell(row=current, column=1, value=entry["series"])
        sheet.cell(row=current, column=2, value=car_num)
        sheet.cell(row=current, column=3, value=entry['team'])
        sheet.cell(row=current, column=4,
                   value=f'{entry["driver1firstName"]} {entry["driver1lastName"]}')
        sheet.cell(row=current, column=5, value=entry['driver1nationality'])

        if series_short == 'GTAM':
            sheet.cell(row=current, column=7, value='Bronze')

        sheet.cell(row=current, column=sponsor_col, value=sponsors)
        sheet.cell(row=current, column=vehicle_col, value=entry['car'])
        sheet.cell(row=current, column=classif_col, value=entry['class'])

        current += 1


# }
