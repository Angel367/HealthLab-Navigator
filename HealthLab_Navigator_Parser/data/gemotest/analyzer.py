import json

with open("parsed_data/gemotest-23ec49ba-9222-45e9-9b93-50dc00d9a6bb.json", "r", encoding="utf-8") as f:
    data = json.load(f)

unique_research_materials = []
for item in data:
    for research_material in item['research_material']:
        if research_material not in unique_research_materials:
            unique_research_materials.append(research_material)

print(unique_research_materials)