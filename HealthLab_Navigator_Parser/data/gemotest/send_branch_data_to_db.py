import json

import requests

# branches
with open('parsed_data/gemotest-moscow-branches-with-metro.json', 'r', encoding='utf-8') as f:
    branches = json.load(f)

headers = {
    'Content-Type': 'application/json',
}

for branch in branches:
    metro_stations_ids = []
    for station in branch['metro_stations']:
        request = requests.get(f'http://localhost:8000/api/metro-station/?name={station}', headers=headers).json()
        for station1 in request:
            metro_stations_ids.append(station1['id'])
    data_branches = {
        "medical_institution": 1,
        "latitude": branch['latitude'],
        "longitude": branch['longitude'],
        "working_hours": branch['working_hours'],
        "metro_stations": metro_stations_ids,
        "url": branch['url']
    }
    request = requests.post('http://localhost:8000/api/medical-institution-branch/', json=data_branches, headers=headers)
    print(request)
