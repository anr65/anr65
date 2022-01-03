# lacoste project
Идея проекта заключается в выявлении корреляции между параметрами мужских футболок поло бренда Lacoste и их ценами. 

Первично написан парсер на python, который собирает данные с динамических страниц веб сайта lacoste.ru. Код парсера находится в файле scrapper.py

Далее собранная информация будет первично обработана и анализирована для выявления корреляций, аномалий и прочего

Последний этап, при подтверждении гипотезы о наличии занчимого влияния факторов на цену - построение модели машинного обучения, способную прогнозировать доверительный интервал цены футболки по заданным параметрам

Инструкция по установке и запуску некоторых файлов с репозитория на локальный компьютер

*For mac or unix based systems only*

1.  Open terminal
2.  Go to the directory you want to repo copied in
3.  Clone repo by entering `git clone git@github.com:anr65/main`
4.  Now enter `python scrapper.py` which will run the scrapper code
5.  Wait until scrapper finishes parsing the data and it'll create two files in the current diretory 
6.  *data_lac.csv* is the raw scrapped data, *data_ready.csv* is the ready to analyze data which next is going to be enhanced
