import json

import requests

# branches
branches = []
with open('parsed_data/gemotest-moscow-analysis-d7137028-c199-4ce7-ae14-07439fdace7c.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        branches.append(json.loads(line))

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzNzIwNTUzLCJpYXQiOjE3MTM3MjAyNTMsImp0aSI6IjE5NDQ2NGEyZDlkZjQ0N2RiYzY0N2Q4MDc1MDM0MmQyIiwidXNlcl9pZCI6MX0.J5v61np52FStuG6kWj9H3o0cCq10zCIHccohgT-UoA8'
}
for branch in branches:

    data_branches = {
        "medical_institution": 1,
        "name": branch['name'],
        "latitude": branch['latitude'],
        "longitude": branch['longitude'],
        "working_hours": branch['working_hours'],
        "url": branch['url']
    }
    request = requests.post('http://localhost:8000/api/medical-service/', json=data_branches, headers=headers)
    print(request)
