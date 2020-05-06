import requests

URL = 'http://localhost:5000/api/profit/'

#   making an api call and passing in the data as a json object
response = requests.post(url = URL, json = {'res_dev': 100, 'admin': 200, 'marketing': 300})

print(response.json())