import requests

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

city = input("city: ")
date = ("date: ")
querystring = {"q":city,"days":"3"}

headers = {
	"X-RapidAPI-Key": "f51be84b20msh28b0658f5161e7ep17c531jsnfc4024f1a1ca",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

res = response.json()

for i in range(3):
    print(res['forecast']['forecastday'][i]['date'], res['forecast']['forecastday'][i]['day']['condition']['text'], 'and', res['forecast']['forecastday'][i]['day']['avgtemp_c'], 'degrees')

# for i in range(3):

# print(res['current']['condition']['text'])