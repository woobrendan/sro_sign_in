gt4_entry = {
    "id": 56185461,
    "displayId": "01HERBBFYJJD6V3347V",
    "formId": 656178,
    "formName": "2024 SRO MOTORSPORTS ENTRY",
    "formAccRef": "2024SRMTRSPRT",
    "orderCustomerId": 879444,
    "customerId": 879444,
    "orderId": 42897892,
    "orderDisplayId": "01HERBBFXQ2YWN7ZTM0",
    "orderNumber": "2024SRMTRSPRTKLM0003",
    "orderEmail": "woo.brendan@gmail.com",
    "levelLabel": "EVENT ENTRY",
    "levelKey": "adult",
    "amount": "7425.00",
    "fee": "0.00",
    "total": "7425.00",
    "currency": "USD",
    "status": "completed",
    "fieldData": [
                {
                    "amount": "0",
                    "label": "Fee",
                    "path": "fee"
                },
        {
                    "label": "Car Series",
                    "path": "carClass",
                    "value": "gtsSprintx"
                },
        {
                    "amount": "0",
                    "label": "GT4 America",
                    "path": "carClass.gtsSprintx",
                    "value": "true"
                },
        {
                    "label": "Championship / Class",
                    "path": "multipleChoice",
                    "value": "proAm"
                },
        {
                    "amount": "0",
                    "label": "Pro-Am",
                    "path": "multipleChoice.proAm",
                    "value": "true"
                },
        {
                    "label": "Registered Car #",
                    "path": "pwcRegisteredCarNumber",
                    "value": "123"
                },
        {
                    "label": "Is this car registered with the RaceSelect program for 2024?",
                    "path": "thisCarRegisteredWith",
                    "value": "no"
                },
        {
                    "amount": "0",
                    "label": "No",
                    "path": "thisCarRegisteredWith.no",
                    "value": "true"
                },
        {
                    "label": "Team Name",
                    "path": "temName"
                },
        {
                    "label": "CDR Valkyrie",
                    "path": "temName.CDR Valkyrie",
                    "value": "true"
                },
        {
                    "label": "GT4 Car Make/Model",
                    "path": "gt4CarMakemodel",
                    "value": "audiR8LmsGt4"
                },
        {
                    "amount": "0",
                    "label": "Audi R8 LMS GT4",
                    "path": "gt4CarMakemodel.audiR8LmsGt4",
                    "value": "true"
                },
        {
                    "label": "Car Year",
                    "path": "carYear",
                    "value": "2015"
                },
        {
                    "label": "Team Sponsors - Please seperate each Sponsor with a comma",
                    "path": "teamSponsors",
                    "value": "Sponsor - test"
                },
        {
                    "label": "PRIMARY DRIVER NAME",
                    "path": "primaryDriverName"
                },
        {
                    "label": "Charlie Luck",
                    "path": "primaryDriverName.Charlie Luck",
                    "value": "true"
                },
        {
                    "label": "PRIMARY DRIVER NATIONALITY",
                    "path": "nationality2"
                },
        {
                    "label": "CAN",
                    "path": "nationality2.CAN",
                    "value": "true"
                },
        {
                    "label": "FIA Driver Categorization",
                    "path": "fiaDriverCategorization",
                    "value": "b"
                },
        {
                    "amount": "0",
                    "label": "Silver",
                    "path": "fiaDriverCategorization.b",
                    "value": "true"
                },
        {
                    "label": "Bronze Test At This Event?",
                    "path": "bronzeTestAtThis",
                    "value": "noWillNotParticipate"
                },
        {
                    "amount": "0",
                    "label": "NO - Primary Driver Will Not Participate In Bronze Test",
                    "path": "bronzeTestAtThis.noWillNotParticipate",
                    "value": "true"
                },
        {
                    "label": "Driver Home Town",
                    "path": "driverHomeTown",
                    "value": "Toronto"
                },
        {
                    "label": "Driver Email",
                    "path": "driverEmail",
                    "value": "woo.brendan@gmail.com"
                },
        {
                    "label": "Driver Cell",
                    "path": "driverCell",
                    "value": "+12893141303"
                },
        {
                    "label": "2nd Driver Name",
                    "path": "2ndDriverName2"
                },
        {
                    "label": "Alec Udell",
                    "path": "2ndDriverName2.Alec Udell",
                    "value": "true"
                },
        {
                    "label": "FIA Driver Categorization",
                    "path": "fiaDriverCategorization2",
                    "value": "b"
                },
        {
                    "amount": "0",
                    "label": "Silver",
                    "path": "fiaDriverCategorization2.b",
                    "value": "true"
                },
        {
                    "label": "Bronze Test At This Event?",
                    "path": "bronzeTestAtThis2",
                    "value": "no2ndDriverWill"
                },
        {
                    "amount": "0",
                    "label": "NO - 2nd Driver Will Not Participate In Bronze Test",
                    "path": "bronzeTestAtThis2.no2ndDriverWill",
                    "value": "true"
                },
        {
                    "label": "2nd Driver Hometown",
                    "path": "2ndDriverHometown",
                    "value": "Vancouver"
                },
        {
                    "label": "2nd Driver Nationality",
                    "path": "nationality32"
                },
        {
                    "label": "CAN",
                    "path": "nationality32.CAN",
                    "value": "true"
                },
        {
                    "label": "2nd Driver Email",
                    "path": "2ndDriverEmail",
                    "value": "woo.brendan@gmail.com"
                },
        {
                    "label": "2nd Driver Cell",
                    "path": "2ndDriverCell",
                    "value": "+12893141303"
                }
    ],
    "eventLabel": "Sonoma Raceway",
    "metadata": None,
    "sourceType": "standard",
    "dateCreated": "2023-11-08T20:53:03Z",
    "dateUpdated": "2023-11-08T20:53:03Z"
}

gt4_expected = {
    "series": "GT4 America",
    "event": "Sonoma Raceway",
    "class": "Pro-Am",
    "number": "123",
    "team": "CDR Valkyrie",
    "driver1firstName": "Charlie",
    "driver1lastName": "Luck",
    "driver1category": "Silver",
    "driver1nationality": "CAN",
    "driver2firstName": "Alec",
    "driver2lastName": "Udell",
    "driver2category": "Silver",
    "driver2nationality": "CAN",
    "car": "Audi R8 LMS GT4",
    "manufacturer": "Audi",
    "sponsors": "Sponsor - test"
},
