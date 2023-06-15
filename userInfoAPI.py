import requests
response = requests.post('http://localhost:3000/api/session', json={'username': 'fatima@gmail.com', 'password': 'fatima@123'})
session_id = response.json()['id']
headers = {'X-Metabase-Session': session_id}
print("Session ID: " + session_id)

url = 'http://localhost:3000/api/user/current'
header = {'Content-Type': 'application/json', 'X-Metabase-Session': session_id}

x = requests.get(url=url, headers=header)

assert x.status_code == 200, "Error: " + str(x.status_code)
print(x.text)
