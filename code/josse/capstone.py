import requests
# import pprint

response = requests.get(
    'https://api.nasa.gov/neo/rest/v1/feed?start_date=2022-01-28&end_date=2022-01-28&api_key=ectXZLeYtMwMQJtm4NTX5fKhuKJ1mWMsor8hNWtn')


# response = requests.get('https://api.nasa.gov/planetary/apod?api_key=ectXZLeYtMwMQJtm4NTX5fKhuKJ1mWMsor8hNWtn')
# headers={'Authorization': 'Token token="ectXZLeYtMwMQJtm4NTX5fKhuKJ1mWMsor8hNWtn"'})

space = response.json()
# pprint.pprint(space)
print(space)
