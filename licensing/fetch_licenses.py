from dotenv import load_dotenv
from utility.convertLicense import convertLicense
import requests
import os

load_dotenv()


def fetch_licenses(date):

    token = os.environ.get('TKSPICE')
    form = os.environ.get('RED_POD')

    try:

        params = {
            "product": "redpodium.com",
            "formId": form,
            "limit": "250",
            "status":"completed"
        }

        if date:
            params['dateCreatedAfter'] = date
            
        response = requests.get(
            url="https://api.webconnex.com/v2/public/search/registrants",
            params=params,
            headers={
                'apiKey': token
            }
        )
        if response.status_code == 200:
            data = response.json()
            converted = [convertLicense(entry) for entry in data['data']]
            return converted

    except requests.exceptions.RequestException:
        print(f'HTTP Request failed error {response.status_code}')
