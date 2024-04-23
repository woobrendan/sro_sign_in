from format_entry_list.labels import license_labels
from utility.utility import getCredentialType

def convertLicense(entry):
    new_entry = {
        "id": entry["id"],
        'created': entry['dateCreated']
    }

    for label in license_labels:
        for field in entry['fieldData']:

            # Get Registrant Info
            if label == 'First Name' and field['path'] == 'name.first':
                new_entry[label] = field['value']
                break
            
            if label == 'Last Name' and field['path'] == 'name.last':
                new_entry[label] = field['value']
                break

            if label == 'ticketType':
                val = '' 
                if field['label'] == 'SINGLE EVENT - NON DRIVER (Crew, Sponsor, Staff, Media)':
                    val = "Single Event Credential"

                    if 'ultra4SingleEventsAre.' in field['path']:
                        new_entry['event'] = field['label']
                        
                    break
                
                if field['label'] == 'COMPETITION LICENSE TYPE':
                    val = getCredentialType(field['value'])
                    new_entry['event'] = "Annual"
                     
                new_entry['ticketType'] = val
                break


            #handles email, dob
            if label == field['label']:
                new_entry[label] = field['value']
                break





# {
#         "id": 54585066,
#         "displayId": "01HVQKK5ZCKXSBXAVY4",
#         "billing": {
#             "firstName": "Jason",
#             "lastName": "Daskalos",
#             "address": {
#                 "city": "Albuquerque",
#                 "country": "US",
#                 "postalCode": "87110",
#                 "state": "NM",
#                 "street1": "5319 Menaul Blvd ne"
#             }
#         },
#         "formId": 649405,
#         "formName": "2024 SRO MOTORSPORTS LICENSE",
#         "formAccRef": "2024SRLCNS",
#         "orderCustomerId": 7304118,
#         "customerId": 31940980,
#         "orderId": 47765172,
#         "orderDisplayId": "01HVQKK5YZQH5BZ05YZ",
#         "orderNumber": "2024SRLCNS-KLM0215",
#         "orderEmail": "smiller@daskalosdi.com",
#         "status": "completed",
#         "total": "171.60",
#         "amount": "171.60",
#         "outstandingAmount": "0",
#         "currency": "USD",
#         "fieldData": [
#             {
#                 "amount": "0",
#                 "label": "PERSONAL WAIVER",
#                 "path": "personalWaiver",
#                 "value": "true"
#             },
#             {
#                 "label": "WHAT DO YOU NEED TO DO TODAY?",
#                 "path": "multipleChoice",
#                 "value": "driverTest"
#             },
#             {
#                 "amount": "0",
#                 "label": "SINGLE  EVENT LICENSE ONLY",
#                 "path": "multipleChoice.driverTest",
#                 "value": "true"
#             },
#             {
#                 "label": "COMPETITION LICENSE TYPE",
#                 "path": "licenseType",
#                 "value": "singleEventNonDriver"
#             },
#             {
#                 "amount": "165",
#                 "label": "SINGLE EVENT - NON DRIVER (Crew, Sponsor, Staff, Media)",
#                 "path": "licenseType.singleEventNonDriver",
#                 "value": "true"
#             },
#             {
#                 "label": "CHOOSE EVENT",
#                 "path": "ultra4SingleEventsAre",
#                 "value": "longBeachGrandPrix"
#             },
#             {
#                 "amount": "0",
#                 "label": "LONG BEACH GRAND PRIX",
#                 "path": "ultra4SingleEventsAre.longBeachGrandPrix",
#                 "value": "true"
#             },
#             {
#                 "label": "First Name",
#                 "path": "name.first",
#                 "value": "Tim"
#             },
#             {
#                 "label": "Last Name",
#                 "path": "name.last",
#                 "value": "McNaney"
#             },
#             {
#                 "label": "ZIP/Postal Code",
#                 "path": "address.postalCode",
#                 "value": "87110"
#             },
#             {
#                 "label": "State",
#                 "path": "address.state",
#                 "value": "NM"
#             },
#             {
#                 "label": "Street Address",
#                 "path": "address.street1",
#                 "value": "5319 Menaul Blvd ne"
#             },
#             {
#                 "label": "City",
#                 "path": "address.city",
#                 "value": "Albuquerque "
#             },
#             {
#                 "label": "Country",
#                 "path": "address.country",
#                 "value": "US"
#             },
#             {
#                 "label": "Email",
#                 "path": "email",
#                 "value": "tmcnaney@twilighthomesnm.com"
#             },
#             {
#                 "label": "TEXT  Number",
#                 "path": "textNumber",
#                 "value": "+15059751154"
#             },
#             {
#                 "label": "Date of Birth",
#                 "path": "dateOfBirth",
#                 "value": "1969-08-14"
#             },
#             {
#                 "label": "ANNUAL RELEASE AND WAIVER OF LIABILITY, ASSUMPTION OF RISK & INDEMNITY AGREEMENT",
#                 "path": "annualReleaseAndWaiver",
#                 "value": "2TZ1000Y3_2z79be7_1T59gid95_1T10Z34443_4wZ422Y76588799a56_2H886Z61Y100061123_9NZ50100Y1311025b4697_2Gcdb7Z6eebY6b85Z98Y440_bXZ654Y9gZa_2X5641Z9Y6_dOZ5221Y74105cfd86bo1wmfd7a_1Rah97Za6Y6984200021Z230Y157"
#             },
#             {
#                 "label": "First Name",
#                 "path": "name3.first",
#                 "value": "Tim"
#             },
#             {
#                 "label": "Last Name",
#                 "path": "name3.last",
#                 "value": "McNaney"
#             },
#             {
#                 "label": "State Of Residence",
#                 "path": "stateOfResidence",
#                 "value": "New Mexico "
#             },
#             {
#                 "label": "WAIVER VERIFICATION",
#                 "path": "waiverVerification",
#                 "value": "byText"
#             },
#             {
#                 "amount": "0",
#                 "label": "By Text (Easiest & Fastest)",
#                 "path": "waiverVerification.byText",
#                 "value": "true"
#             },
#             {
#                 "label": "TEXT NUMBER",
#                 "path": "textNumber2",
#                 "value": "+15059751154"
#             },
#             {
#                 "amount": "6.6",
#                 "label": "Bank CC Fee's",
#                 "path": "lineItem"
#             },
#             {
#                 "amount": "6.6",
#                 "path": "lineItem.lineItemFee"
#             },
#             {
#                 "label": "Coupon Code",
#                 "path": "couponCode",
#                 "value": ""
#             }
#         ],
#         "metadata": null,
#         "checkedIn": false,
#         "sourceType": "standard",
#         "dateCreated": "2024-04-18T03:21:53Z",
#         "dateUpdated": "2024-04-18T03:21:54Z"
#     }


###### Driver annual

# {
#                 "label": "COMPETITION LICENSE TYPE",
#                 "path": "licenseType",
#                 "value": "sroDriverAnnual"
#             },
#             {
#                 "amount": "880",
#                 "label": "DRIVER - ANNUAL",
#                 "path": "licenseType.sroDriverAnnual",
#                 "value": "true"
#             },


## Crew Annual

# {
            #     "label": "COMPETITION LICENSE TYPE",
            #     "path": "licenseType",
            #     "value": "sroCrewAnnual"
            # },
            # {
            #     "amount": "550",
            #     "label": "CREW - ANNUAL",
            #     "path": "licenseType.sroCrewAnnual",
            #     "value": "true"
            # },