import bs4
import requests

url = 'http://jadwalsholat.pkpu.or.id/monthly.php?id=36'
content = requests.get(url)

response = bs4.BeautifulSoup(content.text, "html.parser")
data = response.find_all('tr', 'table_highlight')
data = data[0]

sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat['Subuh'] = d.get_text()
    elif i == 2:
        sholat['Dzuhur'] = d.get_text()
    elif i == 3:
        sholat['Ashar'] = d.get_text()
    elif i == 4:
        sholat['Magrib'] = d.get_text()
    elif i == 5:
        sholat['Isya'] = d.get_text()
    i += 1

print(sholat)