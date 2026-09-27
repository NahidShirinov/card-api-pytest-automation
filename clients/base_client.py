"""Butun client-lerin ortaq hissesi: session, base URL, timeout."""
import requests

from config.settings import BASE_URL, TIMEOUT
from utils import http_recorder


class BaseClient:
    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
        # Her cavab report ucun yadda saxlanilir
        self.session.hooks["response"].append(http_recorder.record)

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.session.get(f"{self.base_url}{path}", timeout=TIMEOUT, **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.session.post(f"{self.base_url}{path}", timeout=TIMEOUT, **kwargs)
