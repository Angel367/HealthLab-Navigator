# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json


class SaveToFilePipeline:
    allowed_spiders = ['gemotest_spider']

    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        if spider.name in self.allowed_spiders:
            self.file = open(
                f'data/{spider.name.replace("_spider", "")}/parsed_data/{spider.output_filename}', 'w', encoding='utf-8'
            )

    def close_spider(self, spider):
        if spider.name in self.allowed_spiders:
            self.file.close()

    def process_item(self, item, spider):
        if spider.name in self.allowed_spiders:
            line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
            self.file.write(line)

        return item
