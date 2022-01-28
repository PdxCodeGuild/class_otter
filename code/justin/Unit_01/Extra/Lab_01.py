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


city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

def update_with_least(dictionary_a, dictionary_b):
    for key, value in dictionary_b.items():
        if key not in dictionary_a:
            dictionary_a[key] = value
        else:
            current_value = dictionary_a[key]
            dictionary_a[key] = current_value if current_value < value else value
    return dictionary_a

def get_shortest_local_travel_times(city):
    connected_cities = {}
    connected_cities[city] = 0
    connected_cities.update(city_to_accessible_cities_with_travel_time[city])
    
    shortest_travel_times = {}
    for connected_city, travel_time in connected_cities.items():
        next_cities = city_to_accessible_cities_with_travel_time[connected_city]
        cities_to_add = {}
        for next_city, next_travel_time in next_cities.items():
            next_travel_time += travel_time
            if next_city not in cities_to_add:
                cities_to_add[next_city] = next_travel_time
            else:
                this_travel_time = cities_to_add[next_city]
                cities_to_add[next_city] = this_travel_time if this_travel_time < next_travel_time else next_travel_time

        shortest_travel_times = update_with_least(shortest_travel_times, cities_to_add)
    return shortest_travel_times

def get_connected_city_travel_times(city, hops=1):
    hops = 1 if hops < 1 else hops
    hops = 3 if hops > 3 else hops

    all_connected_cities = {}
    
    if hops == 1:
        all_connected_cities = city_to_accessible_cities_with_travel_time[city]
    elif hops == 2:
        all_connected_cities = get_shortest_local_travel_times(city)
    elif hops == 3:
        shortest_travel_times = {}
        local_travel_times = city_to_accessible_cities_with_travel_time[city]
        
        distant_travel_times = {}
        for next_city, local_time in local_travel_times.items():
            if next_city not in shortest_travel_times:
                shortest_travel_times[next_city] = local_time
            else:
                current_time = shortest_travel_times[next_city]
                shortest_travel_times[next_city] = current_time if current_time < local_time else local_time

            cities_to_check = get_shortest_local_travel_times(next_city)
            for city_to_check, time_to_update in cities_to_check.items():
                cities_to_check[city_to_check] = time_to_update + local_time
            distant_travel_times = update_with_least(distant_travel_times, cities_to_check)
            shortest_travel_times = update_with_least(shortest_travel_times, distant_travel_times)
        all_connected_cities = dict(shortest_travel_times)

    if city in all_connected_cities:
        all_connected_cities.pop(city)

    return all_connected_cities

def pretty_string(cities):
    result = ''
    for city, time in cities.items():
        result += f'{city} - {time}, '

    return result[:-2]

def main():
    is_running = True
    
    while is_running:
        city = input('\n\tAlbany\n\tBoston\n\tNew York\n\tPhiladelphia\n\tPortland\n\tQuit\nEnter a city: ').title()
        if city in city_to_accessible_cities_with_travel_time:
            num_hops = 0
            while num_hops < 1 or num_hops > 3:
                hop_count = input('Number of hops [1 - 3]: ')
                try:
                    num_hops = int(hop_count)
                except:
                    num_hops = 0
            
            nearby_cities = get_connected_city_travel_times(city)
            print(f'\nNearby cities: {pretty_string(nearby_cities)}\n')

            if num_hops > 1:
                distant_cities = get_connected_city_travel_times(city, num_hops)
                print(f'Within {num_hops} hops: {pretty_string(distant_cities)}\n')

        elif city == 'Q' or city == 'Quit':
            is_running = False
        else:
            print(f"\nInvalid city [{city}]; please select from the following:")

main()