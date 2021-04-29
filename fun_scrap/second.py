import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.detik.com/terpopuler', params={'tag_from':'wp_cb_mostPopular_more'})
soup = BeautifulSoup(url.text, 'html.parser')

populer_area = soup.find(attrs={'class': 'grid-row list-content'})
titles = populer_area.find_all(attrs={'class': 'media__title'})
images = populer_area.find_all(attrs={'class': 'media__image'})

for image in images:
    print(image.find('a').find('img')['title'])

# print(title)