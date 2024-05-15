import json

import requests

# branches
with open('kdl-branches.json', 'r', encoding='utf-8') as f:
    branches = json.load(f)

headers = {
    'Content-Type': 'application/json',
}

working_hours = [
    {
        "day": "пн",
        "open_time": "07:30",
        "close_time": "19:30"
    },
    {
        "day": "вт",
        "open_time": "07:30",
        "close_time": "19:30"
    },
    {
        "day": "ср",
        "open_time": "07:30",
        "close_time": "19:30"
    },
    {
        "day": "чт",
        "open_time": "07:30",
        "close_time": "19:30"
    },
    {
        "day": "пт",
        "open_time": "07:30",
        "close_time": "19:30"
    },
    {
        "day": "сб",
        "open_time": "07:30",
        "close_time": "19:30"
    },
    {
        "day": "вс",
        "open_time": "07:30",
        "close_time": "19:30"
    }
]

for branch in branches:
    metro_stations_ids = []
    request = requests.get(f'http://localhost:8000/api/metro-station/?name={branch["metro_station"]}', headers=headers).json()
    for station in request['results']:
        metro_stations_ids.append(station['id'])
    data_branches = {
        "medical_institution": 2,
        "working_hours": working_hours,
        "metro_stations": metro_stations_ids
    }
    request = requests.post('http://localhost:8000/api/medical-institution-branch/', json=data_branches, headers=headers)
    print(request)
