import requests
from utils import config


class ApiClient:
    def __init__(self):
        self.base_url = config.BASE_URL

    def get(self, endpoint, params=None):
        response = requests.get(f'{self.base_url}/{endpoint}', params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None):
        response = requests.post(f'{self.base_url}/{endpoint}', json=data)
        response.raise_for_status()
        return response.json()
