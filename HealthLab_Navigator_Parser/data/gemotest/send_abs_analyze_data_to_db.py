import json

import requests

# branches
with open('parsed_data/gemotest-23ec49ba-9222-45e9-9b93-50dc00d9a6bb.json', 'r', encoding='utf-8') as f:
    analysis = json.load(f)

headers = {
    'Content-Type': 'application/json',
}

for analyze in analysis:
    research_materials_id = []
    for research_material in analyze['research_material']:
        request = requests.get(f'http://localhost:8000/api/research-material/?name={research_material}', headers=headers).json()
        for research_material1 in request:
            research_materials_id.append(research_material1['id'])
    government_code_804n = analyze.get('government_code_804n', None)
    if government_code_804n is not None:
        government_code_804n = government_code_804n.split(',')
        good_government_code_804n = []
        for government_code in government_code_804n:
            good_government_code_804n.append(government_code.strip())
    else:
        good_government_code_804n = None
    data_analyze = {
        "status": "confirmed",
        "name": analyze['name'],
        "research_material": research_materials_id,
        "government_code_804n": good_government_code_804n,
    }

    request = requests.post('http://localhost:8000/api/medical-service/', json=data_analyze, headers=headers)
    print(request)
