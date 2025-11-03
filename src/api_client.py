import requests
import os
from typing import Optional  
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("REQRES_API_KEY")

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.default_headers = {
            "Content-Type": "application/json",
            "x-api-key": API_KEY
        }

    def _get_headers(self, token: Optional[str] = None):
        headers = self.default_headers.copy()
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    def post(self, endpoint: str, json: dict, token: Optional[str] = None):
        return self.session.post(
            f"{BASE_URL}{endpoint}",
            json=json,
            headers=self._get_headers(token)
        )

    def get(self, endpoint: str, token: Optional[str] = None):
        return self.session.get(
            f"{BASE_URL}{endpoint}",
            headers=self._get_headers(token)
        )

    def put(self, endpoint: str, json: dict, token: Optional[str] = None):
        return self.session.put(
            f"{BASE_URL}{endpoint}",
            json=json,
            headers=self._get_headers(token)
        )

    def delete(self, endpoint: str, token: Optional[str] = None):
        return self.session.delete(
            f"{BASE_URL}{endpoint}",
            headers=self._get_headers(token)
        )