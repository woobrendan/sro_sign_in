import requests

# turn on mongo express server from podium assistant to update entries

def fetch_all_entries():
    response = requests.get('http://localhost:2020/api/entries')

    if response.status_code == 201:
        data = response.json()
         
        return data['data']
    else:
        print(f"Error fetching from own server: {response.status_code}")