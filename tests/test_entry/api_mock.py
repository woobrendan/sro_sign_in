gt4_api = {
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
    "event": "Sonoma Raceway",
    "series": "GT4 America",
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
}

gt3_api = {
    "id": 55666945,
    "displayId": "01HE36XVNZ1972QT4P2",
    "formId": 656178,
    "formName": "2024 SRO MOTORSPORTS ENTRY",
    "formAccRef": "2024SRMTRSPRT",
    "orderCustomerId": 21610113,
    "customerId": 21610113,
    "orderId": 42603460,
    "orderDisplayId": "01HE36XVNN4ZB8NG8YE",
    "orderNumber": "2024SRMTRSPRTKLM0001",
    "orderEmail": "wes@usacnation.com",
    "levelLabel": "EVENT ENTRY",
    "levelKey": "adult",
    "amount": "54900.00",
    "fee": "0.00",
    "total": "54900.00",
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
            "value": "sprintX"
        },
        {
            "amount": "0",
            "label": "FGTWCA",
            "path": "carClass.sprintX",
            "value": "true"
        },
        {
            "label": "Championship / Class",
            "path": "multipleChoice",
            "value": "proPro"
        },
        {
            "amount": "0",
            "label": "Pro",
            "path": "multipleChoice.proPro",
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
            "label": "ACI Motorsports",
            "path": "temName.ACI Motorsports",
            "value": "true"
        },
        {
            "label": "FGTWCA Car Make / Model",
            "path": "carMakeModel2",
            "value": "acuraNsxGt3Evo22"
        },
        {
            "amount": "0",
            "label": "Acura NSX GT3 EVO22",
            "path": "carMakeModel2.acuraNsxGt3Evo22",
            "value": "true"
        },
        {
            "label": "Car Year",
            "path": "carYear",
            "value": "2022"
        },
        {
            "label": "Team Sponsors - Please seperate each Sponsor with a comma",
            "path": "teamSponsors",
            "value": ""
        },
        {
            "label": "PRIMARY DRIVER NAME",
            "path": "primaryDriverName"
        },
        {
            "label": "Aaron Kaplan",
            "path": "primaryDriverName.Aaron Kaplan",
            "value": "true"
        },
        {
            "label": "Nationality 2",
            "path": "nationality2"
        },
        {
            "label": "Ireland",
            "path": "nationality2.IRL",
            "value": "true"
        },
        {
            "label": "FIA Driver Categorization",
            "path": "fiaDriverCategorization",
            "value": "multipleChoiceOption"
        },
        {
            "amount": "0",
            "label": "Bronze",
            "path": "fiaDriverCategorization.multipleChoiceOption",
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
            "value": "Corona"
        },
        {
            "label": "Driver Email",
            "path": "driverEmail",
            "value": "wes@usacnation.com"
        },
        {
            "label": "Driver Cell",
            "path": "driverCell",
            "value": "+15044002770"
        },
        {
            "label": "2nd Driver Name",
            "path": "2ndDriverName2"
        },
        {
            "label": "Aaron Povoledo",
            "path": "2ndDriverName2.Aaron Povoledo",
            "value": "true"
        },
        {
            "label": "FIA Driver Categorization",
            "path": "fiaDriverCategorization2",
            "value": "none"
        },
        {
            "amount": "0",
            "label": "Platinum",
            "path": "fiaDriverCategorization2.none",
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
            "value": "Corona"
        },
        {
            "label": "Nationality 3",
            "path": "nationality32"
        },
        {
            "label": "United States of America",
            "path": "nationality32.USA",
            "value": "true"
        },
        {
            "label": "2nd Driver Email",
            "path": "2ndDriverEmail",
            "value": "wes@usacnation.com"
        },
        {
            "label": "2nd Driver Cell",
            "path": "2ndDriverCell",
            "value": "+15044002770"
        }
    ],
    "eventLabel": "FULL SEASON ENTRY",
    "metadata": None,
    "sourceType": "standard",
    "dateCreated": "2023-10-31T15:51:39Z",
    "dateUpdated": "2023-10-31T15:51:39Z"
}


gt3_expected = {
    "event": "FULL SEASON ENTRY",
    "series": "GT World Challenge America",
    "class": "Pro",
    "number": "123",
    "team": "ACI Motorsports",
    "driver1firstName": "Aaron",
    "driver1lastName": "Kaplan",
    "driver1category": "Bronze",
    "driver1nationality": "IRL",
    "driver2firstName": "Aaron",
    "driver2lastName": "Povoledo",
    "driver2category": "Platinum",
    "driver2nationality": "USA",
    "car": "Acura NSX GT3 EVO22",
    "manufacturer": "Acura",
    "sponsors": ""
}

gtam_api = {
    "id": 55932702,
    "displayId": "01HEDCWVAR21CR94KQV",
    "formId": 656178,
    "formName": "2024 SRO MOTORSPORTS ENTRY",
    "formAccRef": "2024SRMTRSPRT",
    "orderCustomerId": 16638581,
    "customerId": 22845875,
    "orderId": 42756521,
    "orderDisplayId": "01HEDCWVABAA1PVVYEQ",
    "orderNumber": "2024SRMTRSPRTKLM0002",
    "orderEmail": "meldhart@aol.com",
    "levelLabel": "EVENT ENTRY",
    "levelKey": "adult",
    "amount": "7500.00",
    "fee": "0.00",
    "total": "7750.00",
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
            "value": "gtSportsClub"
        },
        {
            "amount": "0",
            "label": "GT America",
            "path": "carClass.gtSportsClub",
            "value": "true"
        },
        {
            "label": "Championship / Class",
            "path": "multipleChoice",
            "value": "sro3"
        },
        {
            "amount": "0",
            "label": "SRO3",
            "path": "multipleChoice.sro3",
            "value": "true"
        },
        {
            "label": "Registered Car #",
            "path": "pwcRegisteredCarNumber",
            "value": "3"
        },
        {
            "label": "Is this car registered with the RaceSelect program for 2024?",
            "path": "thisCarRegisteredWith",
            "value": "yes"
        },
        {
            "amount": "0",
            "label": "Yes",
            "path": "thisCarRegisteredWith.yes",
            "value": "true"
        },
        {
            "label": "Team Name",
            "path": "temName"
        },
        {
            "label": "SKI Autosports",
            "path": "temName.SKI Autosports",
            "value": "true"
        },
        {
            "label": "GTA Car Make/Model",
            "path": "gtSportsClubMakemodel",
            "value": "audiR8Lms"
        },
        {
            "amount": "0",
            "label": "Audi R8 LMS",
            "path": "gtSportsClubMakemodel.audiR8Lms",
            "value": "true"
        },
        {
            "label": "Car Year",
            "path": "carYear",
            "value": "2022"
        },
        {
            "label": "Team Sponsors - Please seperate each Sponsor with a comma",
            "path": "teamSponsors",
            "value": "SKI Autosports"
        },
        {
            "label": "PRIMARY DRIVER NAME",
            "path": "primaryDriverName"
        },
        {
            "label": "Johnny O'Connell",
            "path": "primaryDriverName.Johnny O'Connell",
            "value": "true"
        },
        {
            "label": "PRIMARY DRIVER NATIONALITY",
            "path": "nationality2"
        },
        {
            "label": "USA",
            "path": "nationality2.USA",
            "value": "true"
        },
        {
            "label": "Bronze Test At This Event?",
            "path": "bronzeTestAtThis",
            "value": "yesWillParticipateIn"
        },
        {
            "amount": "250",
            "label": "YES - Primary Driver Will Participate In Bronze Test",
            "path": "bronzeTestAtThis.yesWillParticipateIn",
            "value": "true"
        },
        {
            "label": "Driver Home Town",
            "path": "driverHomeTown",
            "value": "Oakwood"
        },
        {
            "label": "Driver Email",
            "path": "driverEmail",
            "value": "johnny.oconnell3@gmail.com"
        },
        {
            "label": "Driver Cell",
            "path": "driverCell",
            "value": "+14049181428"
        }
    ],
    "eventLabel": "Long Beach Grand Prix",
    "metadata": None,
    "sourceType": "standard",
    "dateCreated": "2023-11-04T14:48:21Z",
    "dateUpdated": "2023-11-04T14:48:24Z"
}

gtam_expected = {
    "event": "Long Beach Grand Prix",
    "series": "GT America",
    "class": "SRO3",
    "number": "3",
    "team": "SKI Autosports",
    "driver1firstName": "Johnny",
    "driver1lastName": "O'Connell",
    "driver1nationality": "USA",
    "car": "Audi R8 LMS",
    "manufacturer": "Audi",
    "sponsors": "SKI Autosports"
}

tcx_api = {
    "id": 56285670,
    "displayId": "01HEX9SWE04WKEH9JNC",
    "formId": 656178,
    "formName": "2024 SRO MOTORSPORTS ENTRY",
    "formAccRef": "2024SRMTRSPRT",
    "orderCustomerId": 879444,
    "customerId": 28984564,
    "orderId": 42957948,
    "orderDisplayId": "01HEX9SWDF8PF5HE5TQ",
    "orderNumber": "2024SRMTRSPRTKLM0004",
    "orderEmail": "woo.brendan@gmail.com",
    "levelLabel": "EVENT ENTRY",
    "levelKey": "adult",
    "amount": "5170",
    "fee": "0",
    "total": "5170",
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
            "value": "tc"
        },
        {
            "amount": "0",
            "label": "TC America",
            "path": "carClass.tc",
            "value": "true"
        },
        {
            "label": "Car Class",
            "path": "carType",
            "value": "tca"
        },
        {
            "amount": "0",
            "label": "TCX",
            "path": "carType.tca",
            "value": "true"
        },
        {
            "label": "Registered Car #",
            "path": "pwcRegisteredCarNumber",
            "value": "789"
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
            "label": "DXDT Racing",
            "path": "temName.DXDT Racing",
            "value": "true"
        },
        {
            "label": "TCX Car Make / Model",
            "path": "tcCarMaleModel",
            "value": "acuraIntegraTypeS"
        },
        {
            "amount": "0",
            "label": "Acura Integra Type S TCX",
            "path": "tcCarMaleModel.acuraIntegraTypeS",
            "value": "true"
        },
        {
            "label": "Car Year",
            "path": "carYear",
            "value": "1"
        },
        {
            "label": "Team Sponsors - Please seperate each Sponsor with a comma",
            "path": "teamSponsors",
            "value": "TEST"
        },
        {
            "label": "PRIMARY DRIVER NAME",
            "path": "primaryDriverName"
        },
        {
            "label": "Aaron Kaplan",
            "path": "primaryDriverName.Aaron Kaplan",
            "value": "true"
        },
        {
            "label": "PRIMARY DRIVER NATIONALITY",
            "path": "nationality2"
        },
        {
            "label": "ABW",
            "path": "nationality2.ABW",
            "value": "true"
        },
        {
            "label": "Driver Home Town",
            "path": "driverHomeTown",
            "value": "Test"
        },
        {
            "label": "Driver Email",
            "path": "driverEmail",
            "value": "test@me.com"
        },
        {
            "label": "Driver Cell",
            "path": "driverCell",
            "value": "+12893141303"
        }
    ],
    "eventLabel": "Sonoma Raceway",
    "sourceType": "standard",
    "dateCreated": "2023-11-10T19:02:10Z",
    "dateUpdated": "2023-11-16T18:18:47Z"
}

tcx_expected = {
    "event": "Sonoma Raceway",
    "series": "TC America",
    "class": "TCX",
    "number": "789",
    "team": "DXDT Racing",
    "driver1firstName": "Aaron",
    "driver1lastName": "Kaplan",
    "driver1nationality": "ABW",
    "car": "Acura Integra Type S TCX",
    "manufacturer": "Acura",
    "sponsors": "TEST"
}
