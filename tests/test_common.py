import pytest

@pytest.mark.common
def test_unknown_resource(api_client):
    response = api_client.get("/unknown/23")
    assert response.status_code == 404


@pytest.mark.common
def test_response_time(api_client):
    response = api_client.get("/users?page=2")
    assert response.elapsed.total_seconds() < 1.7