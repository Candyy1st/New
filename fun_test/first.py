import requests

r = requests.get('https://google.com')
print(r.status_code)

try:
    if r.status_code == 200:
        print(r.text)
except Exception as e:
    print('Ada Error', e)