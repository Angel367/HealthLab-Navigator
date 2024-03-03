from typing import Union

import requests
import scrapy
from uuid import uuid4
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from ..utils.utils import *


class gemotestMoscowBranchSpider(scrapy.Spider):
    name = "gemotest_moscow_branch_spider"
    output_filename = f'gemotest-moscow-analysis-{uuid4()}.jsonl'
    user_agent = UserAgent().random
    headers = {"User-Agent": user_agent}

    def start_requests(self):
        url = 'https://gemotest.ru/moskva/address/'
        labs_a_elements = (BeautifulSoup(requests.get(url, headers=self.headers).text, 'html.parser').
                           findAll('a', class_='lab__address'))
        urls = []
        for lab in labs_a_elements:
            urls.append("https://gemotest.ru"+str(lab.get('href')))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response, **kwargs):
        coords = self.get_coords(response)

        yield {
            'latitude': coords.get("latitude"),
            'longitude': coords.get("longitude"),
            'url': response.url
        }

    @staticmethod
    def get_coords(response) -> Union[None, dict]:
        coords = str(response.xpath("//a[@class='btn btn-dark btn-map btn-yandex']/@href").get())
        pattern = r"pt=(-?\d+\.\d+),(-?\d+\.\d+)"
        matches = re.search(pattern, coords)
        if matches:
            return {
                "latitude": float(matches.group(2)),
                "longitude": float(matches.group(1))
            }
        else:
            return None
