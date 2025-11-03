from src.api_client import APIClient
from src.schemas.auth import LoginRequest, LoginResponse

class AuthService:
    def __init__(self, client: APIClient):
        self.client = client

    def login(self, credentials: LoginRequest) -> LoginResponse:
        resp = self.client.post("/login", json=credentials.model_dump())
        resp.raise_for_status()
        return LoginResponse(**resp.json())