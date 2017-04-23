import json, requests
TOKEN = ""
headers = {'Authorization': TOKEN}
clouds = requests.get('https://mist.io/api/v1/clouds', headers=headers)
print clouds.text
