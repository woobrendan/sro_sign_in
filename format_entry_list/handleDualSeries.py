from utility.utility import getSeriesShort
from utility.events import sro_events


def handle_dual_driver(wb, entries, event):
    first_entry = entries[0]
    series_short = getSeriesShort(first_entry['series'])

    sheet = wb[series_short]
    current = 7

    sorted_entries = sorted(entries, key=lambda x: int(x["number"]))

    # Entry list title, event name and date
    sheet['D2'] = event
    sheet['D4'] = sro_events[event]

    for entry in sorted_entries:
        car_num = entry["number"]

        if not car_num.startswith('0') and car_num.isdigit():
            car_num = int(car_num)

        sheet.cell(row=current, column=1, value=entry["series"])
        sheet.cell(row=current, column=2, value=car_num)
        sheet.cell(row=current, column=3, value=entry['team'])
        sheet.cell(row=current, column=4,
                   value=f'{entry["driver1firstName"]} {entry["driver1lastName"]}')
        sheet.cell(row=current, column=5, value=entry['driver1nationality'])
        # driver license
        sheet.cell(row=current, column=7, value=entry['driver1category'])
        sheet.cell(row=current, column=8,
                   value=f'{entry["driver2firstName"]} {entry["driver2lastName"]}')
        sheet.cell(row=current, column=9, value=entry['driver2nationality'])
        # driver license
        sheet.cell(row=current, column=11, value=entry['driver2category'])
        sheet.cell(row=current, column=12, value=entry['sponsors'])
        sheet.cell(row=current, column=13, value=entry['car'])
        sheet.cell(row=current, column=14, value=entry['class'])

        current += 1


# {
#        "series": "GT4 America",
#        "event": "Sonoma Raceway",
#        "class": "Silver",
#        "number": "28",
#        "team": "G Speed",
#        "driver1firstName": "Kevin",
#        "driver1lastName": "Gausman",
#        "driver1category": "Silver",
#        "driver1nationality": "USA",
#        "driver2firstName": "Chris",
#        "driver2lastName": "Bassatt",
#        "driver2category": "Silver",
#        "driver2nationality": "CAN",
#        "car": "Porsche 718 Cayman CS",
#        "manufacturer": "Porsche",
#        "sponsors": "Cy Young"
#    },
