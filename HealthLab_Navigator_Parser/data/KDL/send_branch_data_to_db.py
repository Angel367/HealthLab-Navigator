import json
import time

import requests
from geopy.geocoders import ArcGIS

# branches
with open('kdl-branches.json', 'r', encoding='utf-8') as f:
    branches = json.load(f)

headers = {
    'Content-Type': 'application/json',
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1Nzg3ODQ0LCJpYXQiOjE3MTU3ODQyNDQsImp0aSI6ImJiNzEzMzI5NDU5MTQ0MTlhNTRmOTg0ZWYwMzlkMTQ4IiwidXNlcl9pZCI6Mn0.43hbX6ImWzLE5IMkAy1ifwsa0zvGAq5B5GuH3XYdPMU"
}

def get_coordinates(address):
    # Создаем объект геокодера ArcGIS
    try:
        geolocator = ArcGIS()

        # Пытаемся найти координаты по заданному адресу
        location = geolocator.geocode(address)

        if location:
            # Если адрес найден, возвращаем его координаты
            return {"latitude": location.latitude, "longitude": location.longitude}
        else:
            # Если адрес не найден, возвращаем None
            return {"latitude": None, "longitude": None}
    except Exception as e:
        return get_coordinates(address)

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
    coords = get_coordinates(branch['address'])
    latitude = coords['latitude']
    longitude = coords['longitude']

    data_branches = {
        "medical_institution": 2,
        "working_hours": working_hours,
        "metro_stations": metro_stations_ids,
        "address": branch['address'],
        "latitude": latitude,
        "longitude": longitude
    }
    print(data_branches)
    request = requests.post('http://localhost:8000/api/medical-institution-branch/', json=data_branches, headers=headers)
    print(request)
    time.sleep(1)
