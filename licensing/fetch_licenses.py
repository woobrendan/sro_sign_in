from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()


def fetch_licenses():

    token = os.environ.get('TKSPICE')
    form = os.environ.get('LIC_ID')

    try:
        response = requests.get(
            url="https://api.webconnex.com/v2/public/search/registrants",
            params={
                "product": "redpodium.com",
                "formId": form
            },
            headers={
                'apiKey': token
            }
        )
        if response.status_code == 200:
            data = response.json()
            print(json.dumps(data['data'], indent=4))

            return data['data']

    except requests.exceptions.RequestException:
        print(f'HTTP Request failed error {response.status_code}')
