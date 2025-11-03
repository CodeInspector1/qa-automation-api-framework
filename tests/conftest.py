import pytest
from src.api_client import APIClient
from typing import Optional

@pytest.fixture
def api_client():
    return APIClient()