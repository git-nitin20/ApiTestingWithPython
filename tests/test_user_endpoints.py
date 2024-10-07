import pytest
# from utils.api_helpers import get


def test_get_user_profile():
    response = get("/users/1")

    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
