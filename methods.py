import requests
from const import *


class ApiMethods:

    def send_post(self, req_type, req_data):
        url = "{}/get_config".format(URL)
        body = {
            "Data": req_data,
            "Type": req_type
        }
        r = requests.post(url, json=body, headers=HEADERS)
        return r
