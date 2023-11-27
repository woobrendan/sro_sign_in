from format_entry_list.labels import labels, car_types
import copy
import re


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


def getFieldPathVal(field):
    return field["path"].split('.')[1]


def getManuf(vehicle):
    # Use a regular expression to find the positions of capital letters
    capital_positions = [m.start() for m in re.finditer(r'[A-Z]', vehicle)]

    # Split the string using the identified positions
    parts = [vehicle[i:j]
             for i, j in zip([0] + capital_positions, capital_positions + [None])]

    # Remove empty strings from the list
    parts = [part for part in parts if part]

    return parts[0].capitalize()


def getDriverName(driver, field, entry):
    name = getFieldPathVal(field)
    name_arr = name.split(' ')

    copy_entry = copy.deepcopy(entry)

    if len(name_arr) == 3:
        copy_entry[f"{driver}firstName"] = f'{name_arr[0]} {name_arr[1]}'
        copy_entry[f"{driver}lastName"] = name_arr[2]
    else:
        copy_entry[f"{driver}firstName"] = name_arr[0]
        copy_entry[f"{driver}lastName"] = name_arr[1]

    return copy_entry


# Take in entry object from and convert into format usable for entry list and USAC app
def convertEntry(entry):
    new_entry = {
        "event": entry["eventLabel"]
    }

    for label in labels:
        for field in entry["fieldData"]:

            if label == 'Championship / Class' and 'carType.' in field["path"]:
                new_entry['class'] = convertClassif(field["label"])
                break

            if (label == 'driver1' and 'primaryDriverName.' in field["path"]) or \
                    (label == 'driver2' and '2ndDriverName2.' in field["path"]):
                new_entry = getDriverName(label, field, new_entry)
                break

            if (label == 'driver1nationality' and 'nationality2.' in field["path"]) or \
                (label == 'driver2nationality' and 'nationality32.' in field["path"]) or \
                    (label == 'team' and 'temName.' in field["path"]):
                new_entry[label] = getFieldPathVal(field)
                break

            if (label == 'driver1category' and 'fiaDriverCategorization.' in field['path']) or \
                    (label == 'driver2category' and 'fiaDriverCategorization2.' in field['path']):
                new_entry[label] = field["label"]
                break

            if label == 'car' and field["label"] in car_types:
                car = field['value']
                new_entry['car'] = car
                new_entry['manufacturer'] = getManuf(car)

            if field["label"] == label:
                if label == 'Championship / Class':
                    new_entry['class'] = convertClassif(field["value"])
                    break

                if label == "Team Sponsors - Please seperate each Sponsor with a comma":
                    new_entry["sponsors"] = field["value"]
                    break

                if label == 'Car Series':
                    new_entry["series"] = convertSeries(field["value"])
                    break

                if label == "Registered Car #":
                    new_entry['number'] = field["value"]
                    break

    return new_entry


# USAC APP
# {
#    fields: {
#        driver2category: "Bronze",
#        driver1category: "Bronze",
#        driver1firstName: "Robert",
#        driver1nationality: "USA",
#        racelinkNumber: "219311",  --
#        driver1drivesFirst: true, --
#        team: "STR38 Motorsports",
#        driver1lastName: "Mau",
#        transponderNumber: "14974222", --
#        driver2firstName: "Chris",
#        driver2lastName: "Allen",
#        isTeam: true, --
#        manufacturer: "BMW",
#        driver1licenseNationality: "USA", --
#        number: "438",
#        driver2driverId: 2, --
#        driver1driverId: 1, --
#        car: "BMW M4 GT4 (G82)",
#        sponsors: "Cannonball Storage, OVN, Sim Seats",
#        series: "GT4 America",
#        driver2licenseNationality: "USA", --
#        class: "Am",
#        driver2nationality: "USA"
#    },
#    updatedAt: "2023-10-04T21:43:30.243Z",
#    id: "entries:events-Qsd47Qg251SxArN7zAEuu:nKsb2Q4V7DnXbflK6omLb",
#    createdAt: "2023-10-04T21:09:23.397Z",
#    eventId: "events:Qsd47Qg251SxArN7zAEuu"
# },

# TICKETSPICE
# {
#            "id": 56185461,
#            "displayId": "01HERBBFYJJD6V3347V",
#            "formId": 656178,
#            "formName": "2024 SRO MOTORSPORTS ENTRY",
#            "formAccRef": "2024SRMTRSPRT",
#            "orderCustomerId": 879444,
#            "customerId": 879444,
#            "orderId": 42897892,
#            "orderDisplayId": "01HERBBFXQ2YWN7ZTM0",
#            "orderNumber": "2024SRMTRSPRTKLM0003",
#            "orderEmail": "woo.brendan@gmail.com",
#            "levelLabel": "EVENT ENTRY",
#            "levelKey": "adult",
#            "amount": "7425.00",
#            "fee": "0.00",
#            "total": "7425.00",
#            "currency": "USD",
#            "status": "completed",
#            "fieldData": [
#                {
#                    "amount": "0",
#                    "label": "Fee",
#                    "path": "fee"
#                },
#                {
#                    "label": "Car Series",
#                    "path": "carClass",
#                    "value": "gtsSprintx"
#                },
#                {
#                    "amount": "0",
#                    "label": "GT4 America",
#                    "path": "carClass.gtsSprintx",
#                    "value": "true"
#                },
#                {
#                    "label": "Championship / Class",
#                    "path": "multipleChoice",
#                    "value": "proAm"
#                },
#                {
#                    "amount": "0",
#                    "label": "Pro-Am",
#                    "path": "multipleChoice.proAm",
#                    "value": "true"
#                },
#                {
#                    "label": "Registered Car #",
#                    "path": "pwcRegisteredCarNumber",
#                    "value": "123"
#                },
#                {
#                    "label": "Is this car registered with the RaceSelect program for 2024?",
#                    "path": "thisCarRegisteredWith",
#                    "value": "no"
#                },
#                {
#                    "amount": "0",
#                    "label": "No",
#                    "path": "thisCarRegisteredWith.no",
#                    "value": "true"
#                },
#                {
#                    "label": "Team Name",
#                    "path": "temName"
#                },
#                {
#                    "label": "CDR Valkyrie",
#                    "path": "temName.CDR Valkyrie",
#                    "value": "true"
#                },
#                {
#                    "label": "GT4 Car Make/Model",
#                    "path": "gt4CarMakemodel",
#                    "value": "audiR8LmsGt4"
#                },
#                {
#                    "amount": "0",
#                    "label": "Audi R8 LMS GT4",
#                    "path": "gt4CarMakemodel.audiR8LmsGt4",
#                    "value": "true"
#                },
#                {
#                    "label": "Car Year",
#                    "path": "carYear",
#                    "value": "2015"
#                },
#                {
#                    "label": "Team Sponsors - Please seperate each Sponsor with a comma",
#                    "path": "teamSponsors",
#                    "value": "Sponsor - test"
#                },
#                {
#                    "label": "PRIMARY DRIVER NAME",
#                    "path": "primaryDriverName"
#                },
#                {
#                    "label": "Charlie Luck",
#                    "path": "primaryDriverName.Charlie Luck",
#                    "value": "true"
#                },
#                {
#                    "label": "PRIMARY DRIVER NATIONALITY",
#                    "path": "nationality2"
#                },
#                {
#                    "label": "CAN",
#                    "path": "nationality2.CAN",
#                    "value": "true"
#                },
#                {
#                    "label": "FIA Driver Categorization",
#                    "path": "fiaDriverCategorization",
#                    "value": "b"
#                },
#                {
#                    "amount": "0",
#                    "label": "Silver",
#                    "path": "fiaDriverCategorization.b",
#                    "value": "true"
#                },
#                {
#                    "label": "Bronze Test At This Event?",
#                    "path": "bronzeTestAtThis",
#                    "value": "noWillNotParticipate"
#                },
#                {
#                    "amount": "0",
#                    "label": "NO - Primary Driver Will Not Participate In Bronze Test",
#                    "path": "bronzeTestAtThis.noWillNotParticipate",
#                    "value": "true"
#                },
#                {
#                    "label": "Driver Home Town",
#                    "path": "driverHomeTown",
#                    "value": "Toronto"
#                },
#                {
#                    "label": "Driver Email",
#                    "path": "driverEmail",
#                    "value": "woo.brendan@gmail.com"
#                },
#                {
#                    "label": "Driver Cell",
#                    "path": "driverCell",
#                    "value": "+12893141303"
#                },
#                {
#                    "label": "2nd Driver Name",
#                    "path": "2ndDriverName2"
#                },
#                {
#                    "label": "Alec Udell",
#                    "path": "2ndDriverName2.Alec Udell",
#                    "value": "true"
#                },
#                {
#                    "label": "FIA Driver Categorization",
#                    "path": "fiaDriverCategorization2",
#                    "value": "b"
#                },
#                {
#                    "amount": "0",
#                    "label": "Silver",
#                    "path": "fiaDriverCategorization2.b",
#                    "value": "true"
#                },
#                {
#                    "label": "Bronze Test At This Event?",
#                    "path": "bronzeTestAtThis2",
#                    "value": "no2ndDriverWill"
#                },
#                {
#                    "amount": "0",
#                    "label": "NO - 2nd Driver Will Not Participate In Bronze Test",
#                    "path": "bronzeTestAtThis2.no2ndDriverWill",
#                    "value": "true"
#                },
#                {
#                    "label": "2nd Driver Hometown",
#                    "path": "2ndDriverHometown",
#                    "value": "Vancouver"
#                },
#                {
#                    "label": "2nd Driver Nationality",
#                    "path": "nationality32"
#                },
#                {
#                    "label": "CAN",
#                    "path": "nationality32.CAN",
#                    "value": "true"
#                },
#                {
#                    "label": "2nd Driver Email",
#                    "path": "2ndDriverEmail",
#                    "value": "woo.brendan@gmail.com"
#                },
#                {
#                    "label": "2nd Driver Cell",
#                    "path": "2ndDriverCell",
#                    "value": "+12893141303"
#                }
#            ],
#            "eventLabel": "Sebring International Raceway",
#            "metadata": null,
#            "sourceType": "standard",
#            "dateCreated": "2023-11-08T20:53:03Z",
#            "dateUpdated": "2023-11-08T20:53:03Z"
#        }
