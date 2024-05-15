import json

import requests

with open('kdl-moscow-analysis-final.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print(len(data))