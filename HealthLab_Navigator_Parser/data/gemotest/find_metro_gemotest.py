import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json

url = 'https://gemotest.ru/moskva/address/'
user_agent = UserAgent().random
headers = {"User-Agent": user_agent}
labs_a_elements = (BeautifulSoup(requests.get(url, headers=headers).text, 'html.parser').
                   findAll('div', class_='lab'))

data = []
for lab in labs_a_elements:
    data.append(
        {
            'metro_stations': [item.get_text().split(' —')[0] for item in lab.find('div', class_='lab__metro').findAll('span')],
            'url': "https://gemotest.ru" + str(lab.find('a').get('href'))
        }
    )

for item in data:
    for metro_station in item['metro_stations']:
        if metro_station == "":     # remove empty
            item['metro_stations'].remove(metro_station)
    item['metro_stations'] = list(set(item['metro_stations']))  # remove duplicates


with open('gemotest_metro_stations.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



