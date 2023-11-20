from dotenv import load_dotenv
from format_entry_list.functions.sortByEvent import sortByEvent
import requests
import os

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

            return data['data']

    except requests.exceptions.RequestException:
        print(f'HTTP Request failed error {response.status_code}')


if __name__ == '__main__':
    entries = fetch_entries()
    sortByEvent(entries)
