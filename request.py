import requests

url = 'https://avocado-prediction.herokuapp.com:5000/'

r = requests.get(url)

print(r.text)
