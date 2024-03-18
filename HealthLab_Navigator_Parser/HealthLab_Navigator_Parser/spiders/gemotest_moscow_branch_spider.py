import scrapy
from uuid import uuid4
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from ..utils.utils import *


class GemotestMoscowBranchSpider(scrapy.Spider):
    name = "gemotest_moscow_branch_spider"
    output_filename = f'gemotest-moscow-analysis-{uuid4()}.jsonl'
    user_agent = UserAgent().random
    headers = {"User-Agent": user_agent}
    lab = 'gemotest'

    def start_requests(self):
        url = 'https://gemotest.ru/moskva/address/'
        labs_a_elements = (BeautifulSoup(requests.get(url, headers=self.headers).text, 'html.parser').
                           findAll('a', class_='lab__address'))
        urls = []
        for lab in labs_a_elements:
            urls.append("https://gemotest.ru" + str(lab.get('href')))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response, **kwargs):
        coords = self.get_address(response)
        workings_hours = self.get_working_hours(response)
        print(workings_hours)
        yield {
            'latitude': coords.get("latitude"),
            'longitude': coords.get("longitude"),
            'address': coords.get("address"),
            'url': response.url,
            'working_hours': workings_hours,
            'lab': self.lab
        }

    @staticmethod
    def get_address(response) -> Union[None, dict]:
        coords = str(response.xpath("//a[@class='btn btn-dark btn-map btn-yandex']/@href").get())
        pattern = r"pt=(-?\d+\.\d+),(-?\d+\.\d+)"
        matches = re.search(pattern, coords)
        address = str(response.xpath("//div[@class='middle-large how_to_go i-middle part_one']/p/text()").get())
        if matches:
            return {
                "latitude": float(matches.group(2)),
                "longitude": float(matches.group(1)),
                "address": address
            }
        else:
            return None

    @staticmethod
    def get_working_hours(response) -> list:
        working_hours = (str(response.xpath("//div[@class='middle-large i-large i-middle-lg']/p/strong").getall()[1])
                         .replace("<strong>", "").replace("</strong>", "")
                         .replace("\n", "").replace("\t", ""))
        print(working_hours)
        ai_result = ai_request("Привет! Мне нужно преобразовать мой формат времени работы в следующий:"
                               "пн: HH:MM-HH:MM, вт: HH:MM-HH:MM, ср: HH:MM-HH:MM, чт: HH:MM-HH:MM, пт: HH:MM-HH:MM, "
                               "сб: HH:MM-HH:MM, вс: HH:MM-HH:MM. Поможешь? Вот часы работы в неудобном формате: "
                               f"{working_hours} В ответе пришли только часы работы в нужном формате.")
        return parse_schedule(ai_result)


def parse_schedule(schedule_string):
    days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
    schedule_list = []

    # Разбиваем строку на отдельные дни
    day_schedules = schedule_string.split(', ')

    # Обходим каждый день в расписании
    for day_schedule in day_schedules:
        # Ищем день недели и время открытия/закрытия
        match = re.match(r'(\w{2}): (\d{2}:\d{2})-(\d{2}:\d{2})', day_schedule)
        if match:
            day = match.group(1)
            open_time = match.group(2)
            close_time = match.group(3)

            # Приводим день недели к нижнему регистру
            day_lower = day.lower()

            # Добавляем информацию о дне в список словарей
            if day_lower in days:
                schedule_list.append({'day': day_lower, 'open_time': open_time, 'close_time': close_time})

    return schedule_list
