import os
import random
import re
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"
    }

    iteration_count = 18
    print(f"Всего страниц: {iteration_count}")

    for item in range(1,19):

        req = requests.get(url+f"?PAGEN_1={item}&navByBtn=true")
        src = req.text
        soup = BeautifulSoup(src, "lxml")

        articles = soup.find_all("article", class_="nl-product")
        page_urls = []

        for article in articles:
            page_url = "https://lacoste.ru" + article.find("div", class_="nl-product__content").find("a", class_="nl-product__name").get("href")
            page_urls.append(page_url)

        item_data = []

        for page_url in page_urls:
            req = requests.get(page_url)
            src = req.text
            soup = BeautifulSoup(src, "lxml")
            item_name = soup.find('span', class_='nl-breadcrumbs__content').text + " " + soup.find("span", class_="nl-product-price__color").text.strip()
            item_data.append(item_name)

            item_price = float(soup.find('span', class_="nl-product-price__price nl-product-price__price--new").text.replace('руб.','').replace(' ','').strip())
            item_data.append(item_price)

            page_datas = soup.find_all('li', class_='nl-product-about__list-item')
            pagen_data = []
            for page_data in page_datas:
                info = page_data.text.replace("\xa0", " ").replace("\n", " ").strip()
                pagen_data.append(info)
            is_found = False
            for line in pagen_data:
                if 'Состав' in line:
                    is_found = True
                    sostav = str(line)[8:len(line)]
            if not is_found:
                    sostav = 'NaN'
            item_data.append(sostav)
            is_found = False
            for line in pagen_data:
                if 'Цвет' in line:
                    is_found = True
                    color = str(line)[6:len(line)]
            if not is_found:
                    color = 'NaN'
            item_data.append(color)
            is_found = False
            for line in pagen_data:
                if 'Fit' in line:
                    is_found = True
                    fit = str(line)[5:len(line)]
            if not is_found:
                    fit = 'NaN'
            item_data.append(fit)
            is_found = False
            for line in pagen_data:
                if 'Style' in line:
                    is_found = True
                    style = str(line)[7:len(line)]
            if not is_found:
                    style = 'NaN'
            item_data.append(style)
            is_found = False
            for line in pagen_data:
                if 'Дизайн' in line:
                    is_found = True
                    design = str(line)[8:len(line)]
            if not is_found:
                    design = 'NaN'
            item_data.append(design)
            is_found = False
            for line in pagen_data:
                if 'Сезон' in line:
                    is_found = True
                    season = str(line)[7:len(line)]
            if not is_found:
                    season = 'NaN'
            item_data.append(season)

        iteration_count -= 1
        print(f"Страница {item} завершена, осталось страниц {iteration_count}")
        if iteration_count == 0:
            print("Сбор данных завершен")
        time.sleep(random.randrange(1,2))

    data = pd.DataFrame(item_data)
    data.to_csv('data_lac.csv')


get_data("https://lacoste.ru/catalog/polo-muzh/")

def data_reciever(x):
    data0 = pd.read_csv(x, index_col=False)
    data0 = pd.DataFrame(data0).drop(columns='Unnamed: 0')
    data = pd.DataFrame()
    data['name'] = data0['0'][::8].values
    data['price'] = data0['0'][1::8].values
    data['material'] = data0['0'][2::8].values
    data['color'] = data0['0'][3::8].values
    data['fit'] = data0['0'][4::8].values
    data['style'] = data0['0'][5::8].values
    data['design'] = data0['0'][6::8].values
    data['season'] = data0['0'][7::8].values
    data.to_csv('data_ready.csv')


data_reciever('data_lac.csv')
