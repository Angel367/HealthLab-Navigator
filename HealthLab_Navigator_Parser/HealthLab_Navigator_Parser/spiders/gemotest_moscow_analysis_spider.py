import os
import scrapy
from uuid import uuid4
from lxml import etree
from fake_useragent import UserAgent
from ..utils.utils import *
from typing import Union


class gemotestMoscowAnalysisSpider(scrapy.Spider):
    name = "gemotest_moscow_analysis_spider"
    urls_data_path = "data/gemotest/sitemaps"
    output_filename = f'gemotest-moscow-analysis-{uuid4()}.jsonl'
    user_agent = UserAgent().random
    headers = {"User-Agent": user_agent}

    def start_requests(self):
        files = os.listdir(self.urls_data_path)

        for file in files:
            filepath = os.path.join(self.urls_data_path, file)
            print(filepath)
            with open(filepath, 'r', encoding='utf-8') as f:
                xml_data = f.read()
                root = etree.fromstring(xml_data.encode('utf-8'))
                urls = root.xpath('//xmlns:loc/text()',
                                  namespaces={'xmlns': 'http://www.sitemaps.org/schemas/sitemap/0.9'})

            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response, **kwargs):
        name = str(response.xpath("//h1[@class='content__title']/text()").get())
        price = clear_price(str(response.xpath("//div[@class='analysis-cost']/text()").get()))
        duration = clear_string(
            str(response.xpath("//div[@class='analysis-conditions__item_text icn--clock']/text()").get())
        )
        government_code_804n = self.government_code_804n_handler(response)
        internal_code = str(response.xpath("//span[@class='analysis-code__code']/text()").get())
        research_material = self.research_material_handler(response)
        yield {
            'name': name,
            'price': price,
            'duration': duration,
            'government_code_804n': government_code_804n,
            'research_material': research_material,
            'internal_code': internal_code,
            'url': response.url
        }

    @staticmethod
    def government_code_804n_handler(response) -> Union[None, str]:
        value = None
        target_h3 = response.xpath('//h3[text()="Приказ МЗ РФ № 804н"]')
        if target_h3:
            next_p = target_h3.xpath('./following-sibling::p[1]/text()')
            if next_p:
                value = clear_string(next_p.get())
        return value

    @staticmethod
    def research_material_handler(response) -> Union[None, list]:
        value = None
        target_h3 = response.xpath('//h3[text()="Биоматериал"]')
        if target_h3:
            next_p = target_h3.xpath('./following-sibling::p[1]/text()')
            if next_p:
                value = clear_string(next_p.get())
        return value.split(', ')
