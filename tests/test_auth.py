import pytest
from src.services.auth_service import AuthService
from src.schemas.auth import LoginRequest
from requests import Response


@pytest.mark.auth
def test_successful_login(api_client):
    service = AuthService(api_client)
    payload = LoginRequest(email='eve.holt@reqres.in', password='cityslicka')

    response = service.login(payload) 

    assert response.token  
    assert isinstance(response.token, str)
    assert len(response.token) > 0


@pytest.mark.auth
def test_login_missing_password(api_client):
    response: Response = api_client.post("/login", json={"email": "eve.holt@reqres.in"})
    assert response.status_code == 400
    data = response.json()
    assert data["error"] == "Missing password"


@pytest.mark.auth
def test_login_invalid_user(api_client):
    response: Response = api_client.post("/login", json={
        "email": "fake@reqres.in",
        "password": "123"
    })
    assert response.status_code == 400
    data = response.json()
    assert "error" in data
    assert data["error"] in ("user not found", "Missing password", "Missing email")  
