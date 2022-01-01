# lacoste project
Идея проекта заключается в выявлении корреляции между параметрами мужских футболок поло бренда Lacoste и их ценами. 
Первично написан парсер на python, который собирает данные с динамических страниц веб сайта lacoste.ru. Код парсера находится в файле scrapper.py

Далее собранная информация будет первично обработана и анализирована для выявления корреляций, аномалий и прочего

Последний этап, при подтверждении гипотезы о наличии занчимого влияния факторов на цену - построение модели машинного обучения, способную прогнозировать доверительный интервал цены футболки по заданным параметрам