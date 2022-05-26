#API RESOURCE: https://weatherstack.com/documentation

from config import api_key
import requests
import pandas

base_url = "http://api.weatherstack.com/"

data = requests.get(base_url + "current?access_key=" + api_key + "&query=Uithoorn").json()
print(data)