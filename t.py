import requests

metro_data = requests.get("https://api.hh.ru/metro/1").json()

for line in metro_data['lines']:
    data_for_api = {
        "name": line['name'],
        "color": line['hex_color'],
        "number": line['id']
    }
    new_line = requests.post("http://127.0.0.1:8000/api/metro-line/", data=data_for_api).json()
    for station in line['stations']:
        data_for_api = {
            "name": station['name'],
            "line": new_line['id'],
            "latitude": station['lat'],
            "longitude": station['lng']
        }
        request = requests.post("http://127.0.0.1:8000/api/metro-station/", data=data_for_api)
        if request.status_code == 400:
            print(data_for_api)
            print(request.text)