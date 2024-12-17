import requests


api_key = "820f61e5e50b48dc8ebb15bc5826c955"
url = "https://finance.yahoo.com"

request = requests.get(url)

content = request.json()
print(type(content))