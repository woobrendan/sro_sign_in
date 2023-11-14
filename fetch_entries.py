from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()


def fetch_entries():

    token = os.environ.get('TKSPICE')
    form = os.environ.get('FORM_ID')

    try:
        response = requests.get(
            url="https://api.webconnex.com/v2/public/search/tickets",
            params={
                "product": "ticketspice.com",
                "formId": form
            },
            headers={
                'apiKey': token
            }
        )
        if response.status_code == 200:
            data = response.json()

            print(json.dumps(data, indent=4))
    except requests.exceptions.RequestException:
        print(f'HTTP Request failed error {response.status_code}')


if __name__ == '__main__':
    fetch_entries()
