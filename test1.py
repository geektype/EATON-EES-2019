import requests
import json


url = "https://oq3xvtpr80.execute-api.eu-west-2.amazonaws.com/ees/store-reading"

req = requests.post(url, json={"sen_var": "sensor2", "value": 50})

print(req.status_code)
