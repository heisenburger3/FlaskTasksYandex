import requests

response = requests.get("http://127.0.0.1:8080/users/v2/1")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.post("http://127.0.0.1:8080/api/v2/users/", json={
    "surname": 'AAaaaa',
    "name": 'BBBBBBB',
    "age": 42,
    "position": "Aaaaaa",
    "speciality": 'aaaaaaaa',
    "address": 'module 1',
    "email": 'aaaaaaa@gmail.com',
    'hashed_password': 'adwdaw123'})
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.delete("http://127.0.0.1:8080/api/v2/users/2")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.get("http://127.0.0.1:8080/api/v2/users/aaaaa")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.post("http://127.0.0.1:8080/api/v2/users/1231")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response = requests.delete("http://127.0.0.1:8080/api/v2/users/a")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")
