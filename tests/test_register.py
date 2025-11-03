import pytest

@pytest.mark.register
def test_successful_register(api_client):
    response = api_client.post("/register", json={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    })
    assert response.status_code == 200
    data = response.json()
    assert "id" in data and "token" in data


@pytest.mark.register
def test_unsuccessful_register(api_client):
    response = api_client.post("/register", json={"email": "sydney@fife"})
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"