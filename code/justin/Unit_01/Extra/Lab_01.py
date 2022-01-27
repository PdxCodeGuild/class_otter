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

Version 2 (optional)
Let the user enter a city and a number of hops. Print out all cities that could be reached through that number of hops.

We've also mapped the travel time of each hop. When the user enters a city and a number of hops, print out the shortest travel times to
each city. Paths with fewer hops are not necessarily those with the shorter travel times.

city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}
'''
import sys


city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

def get_connected_cities(city, hops=1):
    all_connected_cities = {}
    connected_cities = city_to_accessible_cities_with_travel_time[city]

    for _ in range(0, hops):
        for next_city, distance in connected_cities.items():
            if next_city in all_connected_cities:
                all_connected_cities[next_city] += distance
            else:
                all_connected_cities[next_city] = distance
        

    if city in all_connected_cities:
        all_connected_cities.pop(city)

    return all_connected_cities

def pretty_string(cities):
    result = ''
    for city in cities:
        result += f'{city} - {cities[city]}, '

    return result[:-2]

def main():
    is_running = True
    
    while is_running:
        city = input('\n\tAlbany\n\tBoston\n\tNew York\n\tPhiladelphia\n\tPortland\nEnter a city: ').title()
        if city in city_to_accessible_cities_with_travel_time:
            hop_count = ''
            try:
                hop_count = input('Number of hops: ')
                num_hops = int(hop_count)
                
                nearby_cities = get_connected_cities(city)
                print(f'\nNearby cities: {pretty_string(nearby_cities)}')

                # distant_cities = get_connected_cities(city, num_hops)
                # print(f'Within {num_hops} hops: {pretty_string(distant_cities)}')
            except Exception as e:
                print(f'\nInvalid hop count [{hop_count}]')
                print(sys.exc_info()[0])
        elif city == 'Q' or city == 'Quit':
            is_running = False
        else:
            print(f"\nInvalid city [{city}]; please select from the following:")

main()