import requests
r = requests.post("http://localhost/", data={'number': 12524})
print(r.status_code, r.reason)
print(r.text)

