import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! Response = {response.status_code}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil pemanggilan {url}')
        print(f'Title : {soup.title.string}')
    else:
        print(f'Ada kesalahan {response.status_code}')

except Exception as e:
    print('There is an error', e)
    print('Pogram ended!')