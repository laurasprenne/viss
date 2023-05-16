import requests

# response = requests.get("https://catfact.ninja/fact")

# catFact = response.json()

# print(catFact["fact"])

# name = input("ievadi vārdu! ")

# while name != "":
#     response = requests.get("https://api.genderize.io?name=" + name)
#     res = response.json()
#     print(res)
#     # print(name, "dzīvos līdz", age, "gadu vecumam")
#     name = input("ievadi vārdu! ")

# response = requests.get("http://universities.hipolabs.com/search?country=United+States")

# schools = response.json()

# def sortParameter(e):
#     return e["name"]

# schools.sort(key=sortParameter)
    
# for skol in schools:
#     if skol["domains"][0] == "mit.edu":
#         print(skol["name"])

# text = input("input your text ")
# text = text.replace(" ", "%
# 20")

# response = requests.get("https://api.funtranslations.com/translate/yoda.json?text=" + text)

# yoda = response.json()

# print(yoda)

import requests

url = "https://love-calculator.p.rapidapi.com/getPercentage"

m = input("ievadi savu vārdu! ")
f = input("ievadi otrās pusītes vārdu! ")

querystring = {"sname":m,"fname":f}

headers = {
	"X-RapidAPI-Key": "f51be84b20msh28b0658f5161e7ep17c531jsnfc4024f1a1ca",
	"X-RapidAPI-Host": "love-calculator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()['percentage']
print(response.text)