from utility.utility import findFirstEmptyRow


def writeToMasterEntry(entries, sheet):
    first = findFirstEmptyRow(sheet)

    for entry in entries:

        sheet.cell(row=first, column=1, value=entry["event"])
        sheet.cell(row=first, column=2, value=entry['series'])
        sheet.cell(row=first, column=3, value=entry["class"])
        sheet.cell(row=first, column=4, value=entry['number'])
        sheet.cell(row=first, column=5, value=entry['team'])
        sheet.cell(row=first, column=6, value=entry['driver1firstName'])
        sheet.cell(row=first, column=7, value=entry['driver1lastName'])
        sheet.cell(row=first, column=8, value=entry['driver1nationality'])
        sheet.cell(row=first, column=9, value=entry['driver1category'])
        sheet.cell(row=first, column=10,
                   value=entry.get('driver2firstName', ''))
        sheet.cell(row=first, column=11,
                   value=entry.get('driver2lastName', ''))
        sheet.cell(row=first, column=12,
                   value=entry.get('driver2nationality', ''))
        sheet.cell(row=first, column=13,
                   value=entry.get('driver2category', ''))
        sheet.cell(row=first, column=14, value=entry['sponsors'])
        sheet.cell(row=first, column=15, value=entry['car'])
        sheet.cell(row=first, column=16, value=entry['manufacturer'])
        sheet.cell(row=first, column=17, value=entry["id"])
        sheet.cell(row=first, column=18, value=entry['created'])

        first += 1
