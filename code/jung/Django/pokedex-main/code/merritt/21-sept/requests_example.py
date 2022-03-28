import requests

response = requests.get('https://developer.trimet.org/ws/v2/vehicles', params={'appID': 'D065A3A5DAE4622752786CEB9', 'routes': '17,70,77'}, headers={'accept': 'application/json', 'custom_header': 'custom_value'})

list_of_vehicles = response.json()['resultSet']['vehicle']
for vehicle in list_of_vehicles:
    print(vehicle['signMessage'], vehicle['latitude'], vehicle['longitude'])

print(type(response.text))
print(type(response.json()))