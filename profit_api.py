import requests

URL = 'http://localhost:5000/api/profit/'

response = requests.post(url = URL, json = {'r-d': 100, 'admin': 200, 'marketing': 300})

print(response.json())