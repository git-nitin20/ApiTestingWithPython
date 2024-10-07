import requests
from configs.config import BASE_URL



def get(endpoint, headers=None):
    headers = headers or {}
    response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
    return response

def post(endpoint, data, headers=None):
    headers = headers or {}
    # headers.update({"Authorization": f"Bearer {API_TOKEN}"})
    response = requests.post(f"{BASE_URL}{endpoint}", json=data, headers=headers)
    return response

def get_token(endpoint, data, headers):
    res = post(endpoint, data, headers)
    return res