import requests
import json

from src.services.BaseService import BaseService


class CallModelService(BaseService):
    headers = None
    params = None

    def set_config(self, headers, params):
        self.headers = headers
        self.params = params

    def call(self, url, data):
        self.logger.info("request post  :" + json.dumps(data))
        result = requests.post(url, json=data)
        self.logger.info("response post :" + json.dumps(result.json()))
        return result.json()
