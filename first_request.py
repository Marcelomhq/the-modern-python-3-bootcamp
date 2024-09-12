import requests
# url = 'https://icanhazdadjoke.com'
# res = requests.get(url, headers={'Accept' : 'text/plain'})

# # print(f'Ur request to {url} was w code {res.status_code}')
# # print (res.text)

url = 'https://icanhazdadjoke.com/search'
res = requests.get(
    url,
    headers={'Accept' : 'application/json'},
    params={'limit': 1, 'term': 'notice'}
)

data = res.json()
print (dict(data['results']))