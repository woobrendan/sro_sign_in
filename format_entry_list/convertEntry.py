from format_entry_list.labels import labels
import json


# Take in entry object from and convert into format usable for entry list and USAC app
def convertEntry(entry):
    new_entry = {}

    for label in labels:
        for field in entry["fieldData"]:

            if label == 'Championship / Class' and field["path"] == 'carType.tca':
                new_entry[label] = field["label"]

            if field["label"] == label:
                new_entry[label] = field["value"]

    return new_entry


def convertSeries(series):
    series_list = {
        'gtsSprintx': "GT4 America",
        'gtSportsClub': "GT America",
        "sprintX": "GT World Challenge America",
        "tc": "TC America"
    }

    return series_list.get(series, f'Series Error {series}')


def convertClassif(classif):
    class_list = {
        "sro3": "SRO3",
        'gt4': "GT4",
        'gt2': 'GT2',
        'proAm': "Pro-Am",
        'proPro': "Pro",
        'am': 'Am',
        'silver': 'Silver',
        'TCX': 'TCX',
        'TC': 'TC',
        'TCA': 'TCA'
    }

    return class_list.get(classif, f'classification error {classif}')

# USAC APP
# {
#    fields: {
#        driver2category: "Bronze",
#        driver1category: "Bronze",
#        driver1firstName: "Robert",
#        driver1nationality: "USA",
#        racelinkNumber: "219311",
#        driver1drivesFirst: true,
#        team: "STR38 Motorsports",
#        driver1lastName: "Mau",
#        transponderNumber: "14974222",
#        driver2firstName: "Chris",
#        driver2lastName: "Allen",
#        isTeam: true,
#        manufacturer: "BMW",
#        driver1licenseNationality: "USA",
#        number: "438",
#        driver2driverId: 2,
#        driver1driverId: 1,
#        car: "BMW M4 GT4 (G82)",
#        sponsors: "Cannonball Storage, OVN, Sim Seats",
#        series: "GT4 America",
#        driver2licenseNationality: "USA",
#        class: "Am",
#        driver2nationality: "USA"
#    },
#    updatedAt: "2023-10-04T21:43:30.243Z",
#    id: "entries:events-Qsd47Qg251SxArN7zAEuu:nKsb2Q4V7DnXbflK6omLb",
#    createdAt: "2023-10-04T21:09:23.397Z",
#    eventId: "events:Qsd47Qg251SxArN7zAEuu"
# },
