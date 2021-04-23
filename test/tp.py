import requests

url = "https://tokopedia.com"

try:
    response = requests.get(url, auth=('candradewa1981@gmail.com', 'be_yourself12'))
    print(f'Success! {response}')
except Exception as e:
    print(f'There is an error {e}')