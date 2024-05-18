import json

import requests

# branches
with open('parsed_data/gemotest-23ec49ba-9222-45e9-9b93-50dc00d9a6bb.json', 'r', encoding='utf-8') as f:
    analysis = json.load(f)

headers = {
    'Content-Type': 'application/json',
}

for analyze in analysis:
    research_materials = analyze['research_material']
    for research_material in research_materials:
        print(research_material)
        t = requests.get(f"http://127.0.0.1:8000/api/research-material/?name={research_material}").json()
        if t == []:
            data = {
                "name": research_material
            }
            data = json.dumps(data)
            request = requests.post('http://127.0.0.1:8000/api/research-material/', data=data, headers=headers)
            print(request.status_code)
        else:
            print("Research material already exists")