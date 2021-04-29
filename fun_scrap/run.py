import glob
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup

session = requests.Session()

def login():
    print('Login..')
    datas = {
        'username':'user',
        'password':'user123'
    }

    res = session.post('http://127.0.0.1:5000/login', data=datas)

    soup = BeautifulSoup(res.text, 'html5lib')
    page_item = soup.find_all('li', attrs={'class':'page-item'})
    total_pages = len(page_item) - 2

    return total_pages


def get_urls(page):
    print('Getting URLs.. {}'.format(page))
    params = {
        'page':page
    }
    res = session.get('http://127.0.0.1:5000', params=params)
    # soup = BeautifulSoup(open('res.html'), 'html5lib')
    soup = BeautifulSoup(res.text, 'html5lib')

    titles = soup.find_all('h4', attrs={'class':'card-title'})
    urls = []
    for title in titles:
        url = title.find('a')['href']
        urls.append(url)

    return urls

    # f = open('res.html', 'w+')
    # f.write(res.text)
    # f.close()


def get_detail(url):
    print('Getting Detail.. {}'.format(url))
    res = session.get('http://127.0.0.1:5000/'+url)

    # f = open('res.html', 'w+')
    # f.write(res.text)
    # f.close()

    soup = BeautifulSoup(res.text, 'html5lib')
    title = soup.find('title').text.strip()
    price = soup.find('h4', attrs={'class':'card-price'}).text.strip()
    stock = soup.find('span', attrs={'class':'card-stock'}).text.strip().replace('stock: ', '')
    category = soup.find('span', attrs={'class':'card-category'}).text.strip().replace('category: ', '')
    description = soup.find('p', attrs={'class':'card-text'}).text.strip().replace('Description: ', '')

    dict_data = {
        'title': title,
        'price': price,
        'stock': stock,
        'category': category,
        'description': description
    }

    with open('./results/{}.json'.format(url.replace('/', '')), 'w') as outfile:
        json.dump(dict_data, outfile)


def create_csv():
    files = sorted(glob.glob('./results/*.json'))

    datas = []
    for file in files:
        with open(file) as json_file:
            data = json.load(json_file)
            datas.append(data)

    df = pd.DataFrame(datas)
    df.to_csv('results.csv', index=False)

    print('CSV Generated..')




def run():
    total_pages = login()

    total_urls = []
    for i in range(total_pages):
        page = i+1
        urls = get_urls(page)
        total_urls += urls #total_urls = total_urls + urls
        with open('all_urls.json', 'w') as outfile:
            json.dump(total_urls, outfile)

    with open('all_urls.json') as json_file:
        data = json.load(json_file)

        for url in data:
            get_detail(url)

    create_csv()


    # options = int(input('Input option number:\n1. Collecting all URLs\n2.Get detail all product\n3.Create CSV\nWhat you choose : '))
    # if options == 1:
    #     total_urls = []
    #     for i in range(total_pages):
    #         page = i+1
    #         urls = get_urls(page)
    #         total_urls += urls  #total_urls = total_urls + urls
    #     with open('all_urls.json', 'w') as outfile:
    #         json.dump(total_urls, outfile)
    #
    # elif options == 2:
    #     with open('all_urls.json') as json_file:
    #         data = json.load(json_file)
    #
    #     for url in data:
    #         get_detail(url)
    #
    # elif options == 3:
    #     create_csv()


if __name__ == '__main__':
    run()