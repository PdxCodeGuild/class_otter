import requests
import pprint

route_to_search = input("What route number would you like to seach by? ")
url_params = {
    'appID': 'D065A3A5DAE4622752786CEB9',
    'routes': route_to_search
}
response = requests.get('https://developer.trimet.org/ws/v2/vehicles', params=url_params)
print(response.url)
print(response.text) # 76.105.187.182
pprint.pprint(response.json()) # 76.105.187.182
print(response.status_code) # 200
print(response.encoding) # ISO-8859-1
print(response.headers) # {'Content-Type': 'text/plain', 'Content-Length': '14', ...}
print('\n\n\n')
for bus in response.json()['resultSet']['vehicle']:
    print(bus['signMessageLong'])
    print(bus['latitude'], bus['longitude'])