import requests


url = 'https://events.usacnation.com/api/events/events:Qsd47Qg251SxArN7zAEuu/entries?key=sro@dmin!'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
