import pytest
from utils.api_helpers import *

@pytest.mark.smoke
def test_generate_token_success():
    endpoint = "/auth"
    payload = {"username": "admin", "password": "password123"}
    headers = {"Content-Type": "application/json"}
    res = post(endpoint, payload, headers)
    assert res.status_code == 200
    assert res.json()["token"] != "Bad credentials"


@pytest.mark.smoke
def test_generate_token_failure():
    endpoint = "/auth"
    payload = {"username": "invaliduser", "password": "wrongpass"}
    headers = {"Content-Type": "application/json"}
    res = post(endpoint, payload, headers)
    assert res.status_code == 200
    assert res.json()["reason"] == "Bad credentials"
