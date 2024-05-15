import json
import os
import scrapy
from uuid import uuid4
from lxml import etree
from fake_useragent import UserAgent
from typing import Union
from bs4 import BeautifulSoup


class KdlMoscowAnalysisSpider(scrapy.Spider):
    name = "KdlMoscowAnalysisSpider"
    urls_data_path = "data/KDL/kdl_moscow_analysis_links.json"
    output_filename = f'kdl-moscow-analysis-{uuid4()}.jsonl'
    user_agent = UserAgent().random
    headers = {"User-Agent": user_agent}
    lab = 'gemotest'

    def start_requests(self):
        with open(self.urls_data_path, 'r', encoding='utf-8') as f:
            urls = json.load(f)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response, **kwargs):
        if "Доступен вы" in response.text:
            is_available_at_home = True
        else:
            is_available_at_home = False
        internal_code = response.xpath("//div[@class='analysis__kind complex']/text()").get()[2:]   # Нет
        name = response.xpath("//div[@class='analysis__desc']/text()").get()    # Да
        duration = BeautifulSoup(response.xpath("//div[@class='analysis__time']").get(), 'html.parser'). \
            find('div', class_='analysis__time').text.strip().replace("СРОК", "").replace('\n', '')
        while duration.find('  ') != -1:
            duration = duration.replace('  ', ' ')
        research_material = response.xpath("//div[@class='analysis__type']/text()").get()       # Да
        government_code_804n = response.xpath("//div[@class='analysis-nmu-codes']/text()").getall()[1].replace('\n', '').strip()
        price = response.xpath("//div[@class='analysis-price__number']/text()").get().replace(" ", "").replace("₽", "").replace('\n', '')   # Да
        yield {
            'is_available_at_home': is_available_at_home,
            'internal_code': internal_code,
            'name': name,
            'duration': duration,
            'research_material': research_material,
            'government_code_804n': government_code_804n,
            'price': price
        }
