import requests
response = requests.post('http://localhost:3000/api/session', json={'username': 'l201274@lhr.nu.edu.pk', 'password': 'naima12345'})
session_id = response.json()['id']
headers = {'X-Metabase-Session': session_id}
print("Session ID: " + session_id)

url = 'http://localhost:3000/api/collection/root'
header = {'Content-Type': 'application/json', 'X-Metabase-Session': session_id}

x = requests.get(url=url, headers=header)

assert x.status_code == 200, "Error: " + str(x.status_code)
print(x.text)
