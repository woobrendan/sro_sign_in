from dotenv import load_dotenv
from utility.convertLicense import convertLicense
import requests
import os
import json
import httpx

load_dotenv()


def fetch_licenses(date):

    token = os.environ.get('KEY')
    form = os.environ.get('2025_REDPOD')
 
    try:
        url="https://api.webconnex.com/v2/public/search/registrants"
        params = {
            "product": "redpodium.com",
            "formId": form,
            "limit": "250",
            "status":"completed"
        }

        headers={
                'apiKey': token
            }

        if date:
            params['dateCreatedAfter'] = date

        response = httpx.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            converted = [convertLicense(entry) for entry in data['data']]
            return converted
        else:
            print('Error:', response.status_code)

    except requests.exceptions.RequestException:
        print(f'HTTP Request failed error {response.status_code}')
