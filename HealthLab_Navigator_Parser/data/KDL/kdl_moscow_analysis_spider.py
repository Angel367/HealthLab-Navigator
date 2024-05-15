from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
import json

# Инициализация веб-драйвера
# driver = webdriver.Chrome()  # или другой драйвер по вашему выбору

# Открытие страницы
from bs4 import BeautifulSoup

# Открываем файл с HTML страницей
with open("Сдать анализы Москве и МО - цены на анализы в лаборатории KDL.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для работы с HTML
soup = BeautifulSoup(html_content, "html.parser")

# Находим все элементы section с классами "h-card h-card--test js-card-item"
sections = soup.find_all("section", class_="h-card h-card--test js-card-item")
links = []
# Сохраняем найденные элементы в массив
sections_array = []
for section in sections:
    sections_array.append(section)

# Выводим результаты
for section in sections_array:
    links.append(section.find('a', class_='h-card__link')['href'])

with open("kdl_moscow_analysis_links.json", "w", encoding="utf-8") as file:
    json.dump(links, file, ensure_ascii=False, indent=4)
# Определение функции для проверки наличия кнопки "Показать еще"