import json

final_data = []

with open('gemotest_metro_stations.json', 'r', encoding='utf-8') as f:
    metro_data = json.load(f)

with open('gemotest-moscow-branches1.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        branch = json.loads(line)
        for item in metro_data:
            if item['url'] == branch['url']:
                branch['metro_stations'] = item['metro_stations']
                break
        print(json.dumps(branch, ensure_ascii=False, indent=4))
        final_data.append(branch)

with open('gemotest-moscow-branches-with-metro.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=4)



