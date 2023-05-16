import requests

url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"

querystring = {"market":"classic","iso_date":"2022-12-07"}

headers = {
	"X-RapidAPI-Key": "f51be84b20msh28b0658f5161e7ep17c531jsnfc4024f1a1ca",
	"X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


for data in response.json()["data"]:
    print(data["home_team"], "vs", data["away_team"], data["prediction"])