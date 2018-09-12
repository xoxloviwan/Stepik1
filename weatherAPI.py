# import json
#
# with open('city.list.json', 'r', encoding='utf-8') as f:
#     cities = json.load(f)
# i = iter(cities)
# t = 0.2
# for city in cities:
#         print(city)
import requests
city = input()
myCitiesID = {'Киров': 548408, 'сад': 532860, 'СПб': 498817}
API_URL = 'http://api.openweathermap.org/data/2.5/weather'
APIkey = 'df91cbd2f7f0f815d6ec5adab99285e1'
params = {
    'id': myCitiesID[city],
    'appid': APIkey,
    'units': 'metric'
}
res = requests.get(API_URL, params)
# print(res.status_code)
# print(res.headers['Content-Type'])
data = res.json()
# print(data)
template = 'В {city}е сейчас {temp} градусов'
print(template.format(city=city, temp=data['main']['temp']))
