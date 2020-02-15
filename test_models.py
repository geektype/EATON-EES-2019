import unittest
from models import storeReadings
import datetime
import requests

class TestDatabase(unittest.TestCase):
    def test_insert_reading(self):
        url = "https://oq3xvtpr80.execute-api.eu-west-2.amazonaws.com/ees/store-reading"
        req = requests.post(url, json={"sen_var": "test_var", "value":1.234})
        self.assertEqual(req.status_code, 200, "Error storing reading")

        

