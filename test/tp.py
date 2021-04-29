import requests

url = "https://www.tokopedia.com/search?navsource=home&rt=4%2C5&source=universe&st=product&q=iphone%2011"

# try:
#     response = requests.get(url)
#     print(f'Success! {response}')
# except Exception as e:
#     print(f'There is an error {e}')

content = requests.get(url)
print(content.text)