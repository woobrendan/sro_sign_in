from utility.utility import findFirstEmptyRow


def writeToMasterEntry(entries, sheet):
    first = findFirstEmptyRow(sheet)

    for entry in entries:
        event, series, number, team, driver1firstName, driver1lastName, driver1nationality, driver1category, driver2firstName, driver2lastName, driver2nationality, driver2category, sponsors, car, manufacturer = entry.values()

        sheet.cell(row=first, column=1, value=event)
        sheet.cell(row=first, column=2, value=series)
        sheet.cell(row=first, column=3, value=entry["class"])
        sheet.cell(row=first, column=4, value=number)
        sheet.cell(row=first, column=5, value=team)
        sheet.cell(row=first, column=6, value=driver1firstName)
        sheet.cell(row=first, column=7, value=driver1lastName)
        sheet.cell(row=first, column=8, value=driver1nationality)
        sheet.cell(row=first, column=9, value=driver1category)

        if driver2firstName:
            sheet.cell(row=first, column=10, value=driver2firstName)
            sheet.cell(row=first, column=11, value=driver2lastName)
            sheet.cell(row=first, column=12, value=driver2nationality)
            sheet.cell(row=first, column=13, value=driver2category)

        sheet.cell(row=first, column=14, value=sponsors)
        sheet.cell(row=first, column=15, value=car)
        sheet.cell(row=first, column=16, value=manufacturer)
        sheet.cell(row=first, column=17, value=entry["id"])
