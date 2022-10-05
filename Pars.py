import requests
from bs4 import BeautifulSoup
import csv

CSV = 'tasks.csv'   #Путь файла для сохранения.
HOST = 'https://freelance.ru'
URL = 'https://freelance.ru/project/search/pro'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}


def get_html(url, params):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='box-shadow')
    tasks = []

    for item in items:
        tasks.append(
            {
                'title': item.find('div', class_='box-title').find('a').get_text(strip=True),
                'text_task': item.find('a', class_='description').get_text(strip=True),
                'cash': item.find('div', class_='cost').get_text(strip=True),
                'time': item.find('span', class_='prop').get('title'),
                'deadline': item.find('div', class_='term').get_text(strip=True),
                'link_task': HOST + item.find('h2', class_='title').find('a').get('href')
            }
        )
    return tasks


def save_doc(items, path):

    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Заголовок', 'Описание', 'Стоимость',
                        'Время публикации', 'Срок выполнения', 'Ссылка'])
        for item in items:
            writer.writerow([
                item['title'],
                item['text_task'],
                item['cash'],
                item['time'],
                item['deadline'],
                item['link_task']
            ])


def parser():


    #PAGENATION = input('Укажите количество страниц для парсинга: ')
    #PAGENATION = int(PAGENATION.strip())

    # Количество страниц для парсинга.
    PAGENATION = 2
    html = get_html(URL, params={})
    if html.status_code == 200:
        tasks = []
        for page in range(1, PAGENATION+1):
            print(f'Парсим страницу: {page}')

            # Фильтр заказов
            html = get_html(URL, params={
                'c[]': 4,  # Раздел: 4 - программирование.
                'page': page,
                'o': 1  # Показывать с договорной стоимостью
            })
            tasks.extend(get_content(html.text))
            save_doc(tasks, CSV)
            #print(tasks)
    else:
        print("Error")


parser()
