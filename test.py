import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'cj'
resp = requests.get(BASE_URL+ENDPOINT)
print(resp.json())
