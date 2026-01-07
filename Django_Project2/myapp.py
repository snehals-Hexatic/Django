import requests

URL = "http://127.0.0.1:8080/stucreate/"

data = {
    "name": "Snehal",
    "roll": 101,
    "city": "Ranchi"
}

r = requests.post(URL, json=data)
print(r.status_code)
print(r.json())
