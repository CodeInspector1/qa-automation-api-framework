import pytest
from src.schemas.user import User, UserCreateRequest, UserCreateResponse

@pytest.mark.users
def test_get_single_user(api_client):
    response = api_client.get("/users/2")
    assert response.status_code == 200
    data = response.json()["data"]
    user = User(**data)
    assert user.id == 2
    assert user.email.endswith("@reqres.in")


@pytest.mark.users
def test_get_users_list(api_client):
    response = api_client.get("/users?page=1")
    assert response.status_code == 200
    users = [User(**u) for u in response.json()["data"]]
    assert len(users) > 0


@pytest.mark.users
def test_create_user(api_client):
    payload = UserCreateRequest(name="morpheus", job="leader")
    response = api_client.post("/users", json=payload.model_dump())
    assert response.status_code == 201
    data = response.json()
    user = UserCreateResponse(**data)
    assert user.name == "morpheus"
    assert user.job == "leader"


@pytest.mark.users
def test_update_user(api_client):
    updated_data = {"name": "Alice Updated", "job": "Lead QA"}
    response = api_client.put("/users/2", json=updated_data)
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Alice Updated"
    assert data["job"] == "Lead QA"
    assert "updatedAt" in data


@pytest.mark.users
def test_delete_user(api_client):
    response = api_client.delete("/users/2")
    assert response.status_code == 204


@pytest.mark.users
def test_pagination(api_client):
    response = api_client.get("/users?page=2")
    assert response.status_code == 200

    data = response.json()
    assert data["page"] == 2
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0