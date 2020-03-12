import requests

url = 'https://avocado-prediction.herokuapp.com'

r = requests.get(url)

print(r.text)
