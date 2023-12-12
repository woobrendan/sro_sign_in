from dotenv import load_dotenv
from utility.sortFuncs import sortByEvent
import requests
import os

load_dotenv()


def fetch_entries():

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

            return data['data']

    except requests.exceptions.RequestException:
        print(f'HTTP Request failed error {response.status_code}')


if __name__ == '__main__':
    entries = fetch_entries()
    sortByEvent(entries)
