import requests
import json


response = requests.get("https://oq3xvtpr80.execute-api.eu-west-2.amazonaws.com/test/readings")

json_response = response.json()

data = json_response

name = data['value']

print(name)

