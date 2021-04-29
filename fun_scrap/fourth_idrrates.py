import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.8829710693892e-5,"date":"Sat, 24 Apr 2021 00:00:01 GMT","inverseRate":14528.609664616},
             "eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.7067477781518e-5,"date":"Sat, 24 Apr 2021 00:00:01 GMT","inverseRate":17523.115421861}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])