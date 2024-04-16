import requests


# turn on mongo express server from podium assistant to update entries

def fetch_all_entries():
    response = requests.get('http://localhost:2020/api/entries')

    if response.status_code == 201:
        data = response.json()
         
        return data['entry']
    else:
        print(f"Error fetching from own server: {response.status_code}")


def fetch_event_entries(event):
    response = requests.get(f'http://localhost:2020/api/entries/events/{event}')

    if response.status_code == 200:
        data = response.json()
         
        return data['entries']
    else:
        print(f"Error fetching from own server: {response.status_code}")