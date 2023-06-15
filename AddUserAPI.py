import requests
response = requests.post('http://localhost:3000/api/session',
                         json={'username': 'l201371@lhr.nu.edu.pk', 'password': 'khizerali123'})
session_id = response.json()['id']
headers = {'X-Metabase-Session': session_id}
print("Session ID: " + session_id)

url = 'http://localhost:3000/api/user'
data = {'first_name': 'Basic', 'last_name': 'User', 'email': 'basic@somewhere.com', 'password': 'Sup3rS3cure_:}'}
header = {'Content-Type': 'application/json', 'X-Metabase-Session': session_id}

x = requests.post(url=url, json=data, headers=header)

assert x.status_code == 200, "Error: " + str(x.status_code)
print(x.text)
