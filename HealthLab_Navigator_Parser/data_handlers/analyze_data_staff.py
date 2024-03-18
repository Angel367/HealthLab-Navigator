import json

with open("../data/gemotest/parsed_data/gemotest-23ec49ba-9222-45e9-9b93-50dc00d9a6bb.json", encoding='utf-8') as f:
    json_data = json.load(f)

unique_research_materials = []

for el in json_data:
    if el.get('research_material', None) is not None:
        for rm in el.get('research_material'):
            if rm not in unique_research_materials:
                unique_research_materials.append(rm)

print(unique_research_materials)