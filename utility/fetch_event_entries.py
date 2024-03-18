from dotenv import load_dotenv
from utility.sortFuncs import sortByEvent
import requests
import os

load_dotenv()


def fetch_event_entries():

    token = os.environ.get('TKSPICE')
    form = os.environ.get('FORM_ID')

    try:
        params = {
            "product": "ticketspice.com",
            "formId": form,
            "limit": "250",
            "status": "completed"
        }
        # take in date param to limit fetched order num
        #if date is not None:
        #    params["date"] = date
            
        response = requests.get(
            url="https://api.webconnex.com/v2/public/search/tickets",
            params=params,
            headers={ 'apiKey': token }
        )
        
        if response.status_code == 200:
            data = response.json()
         
            entries = data['data']
    
            filtered = [entry for entry in entries if entry['levelLabel'] == "EVENT ENTRY"]
            return filtered

    except requests.exceptions.RequestException:
        print(f'HTTP Request failed error {response.status_code}')

