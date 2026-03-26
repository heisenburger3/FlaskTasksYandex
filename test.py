import requests


response = requests.get("http://127.0.0.1:8080/api/jobs")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")


response = requests.get("http://127.0.0.1:8080/api/jobs/1")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")


response = requests.get("http://127.0.0.1:8080/api/jobs/42")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")


response = requests.get("http://127.0.0.1:8080/api/jobs/first_job")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")