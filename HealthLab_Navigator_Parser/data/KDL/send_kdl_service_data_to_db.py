import json
import random

import requests

# branches
with open('kdl-moscow-analysis-final.json', 'r', encoding='utf-8') as f:
    analysis = json.load(f)




headers = {
    'Content-Type': 'application/json',
}
bad_count = 0
good_count = 0

def convert_duration(duration):
    if 'д' in duration:
        result = int(duration[1]) * 24 * 60 * 60
        return result
    else:
        return None

for analyze in analysis:
    try:
        abs_medical_service_id =\
            requests.get(f"http://127.0.0.1:8000/api/medical-service/?name=&exact_name={analyze['name']}&similar_name=").\
                json()['results'][0]['id']

        time_to_complete = convert_duration(analyze['duration'])
        data_to_send = {
            "medical_institution": 2,
            "service": abs_medical_service_id,
            "price": analyze['price'],
            "time_to_complete": time_to_complete,
            "internal_code": analyze['internal_code'],
            "is_available_at_home": analyze['is_available_at_home'],
            "is_available_oms": True,
            "is_available_dms": True
        }
        t = requests.post("http://127.0.0.1:8000/api/medical-institution-service/", headers=headers, data=json.dumps(data_to_send))
        if t.status_code != 201:
            print(t.status_code)
            print(t.text)
            bad_count += 1
        else:
            good_count += 1

    except Exception as e:
        print(e)
        bad_count += 1

print(len(analysis), good_count, bad_count)