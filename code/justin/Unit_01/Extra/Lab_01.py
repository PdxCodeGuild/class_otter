# Full Stack Bootcamp - Unit 01 extras Lab 01 - Road Trip
# Justin Hammond, 01/27/2022


'''
Lab: Road Trip
We've mapped what cities are directly connected by roads and stored them in a dictionary:

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}
Traveling from one city to an adjacent one is called a hop. Let the user enter a city. Print out all the cities connected to that city.
Then print out all cities that could be reached through two hops.
'''

city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

def get_connected_cities(city, hops=1):
    all_connected_cities = set(city_to_accessible_cities[city])
    connected_cities = set()
    for i in range(1, hops):
        for next_city in all_connected_cities:
            connected_cities = connected_cities | set(city_to_accessible_cities[next_city])
        all_connected_cities = all_connected_cities | connected_cities
    
    return all_connected_cities

def pretty_string(cities):
    result = ''
    for city in cities:
        result += f'{city}, '

    return result[:-2]

def main():
    is_running = True
    
    while is_running:
        city = input('''\n\tAlbany\n\tBoston\n\tNew York\n\tPhiladelphia\n\tPortland\nEnter a city: ''').title()
        hop_count = 2
        if city in city_to_accessible_cities:
            nearby_cities = get_connected_cities(city)
            distant_cities = get_connected_cities(city, hop_count)
            print(f'\nNearby cities: {pretty_string(nearby_cities)}')
            print(f'Within {hop_count} hops: {pretty_string(distant_cities)}')
        elif city == 'Q' or city == 'Quit':
            is_running = False
        else:
            print(f"\nInvalid city [{city}]; please select from the following:")

main()