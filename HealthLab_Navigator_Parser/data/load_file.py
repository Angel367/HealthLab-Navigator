import requests
from fake_useragent import UserAgent

url = "https://gemotest.ru/sitemap/ru/sitemap-iblocks/sitemap-analizes-moskva.xml"
file_name = "xml/sitemaps/sitemap.xml"  # Имя, под которым вы хотите сохранить файл

# Создание случайного User-Agent
user_agent = UserAgent().random

# Создание заголовков запроса
headers = {"User-Agent": user_agent}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open(file_name, "wb") as file:
        file.write(response.content)
    print("Файл успешно скачан как", file_name)
else:
    print("Не удалось скачать файл. Код ответа:", response.status_code)
