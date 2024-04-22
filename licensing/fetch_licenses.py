from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()


def fetch_licenses():

    token = os.environ.get('TKSPICE')
    form = os.environ.get('RED_POD')

    try:

        params = {
            "product": "redpodium.com",
            "formId": form,
            "limit": "250",
            "status":"completed"
        }
        response = requests.get(
            url="https://api.webconnex.com/v2/public/search/registrants",
            params=params,
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
