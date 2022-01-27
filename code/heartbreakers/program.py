# Version 1
# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.
#     Jackalopes are reproductive from ages 4-8 and die at age 10.
#     Gestation is instantaneous. Each gestation produces two offspring.
#     Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
#     With these conditions in mind, we can represent our population as a list of ints.

# Version 2
# Now let's give the jackalopes distinct sexes and extend their gestation period to one year.
# We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries.
# A jackalope will have the following properties:
    # jackalope = {'name': 'a', 'age': int, 'gender': 'a', 'pregnant': bool}
    # population = [{},{}]
    # name
    # age
    # sex
    # whether they're pregnant
# Jackalopes can only mate with those immediately around them (within one year of their age).
# Every generation Jackalopes are randomly shuffled.

# def increment_population(population_list):
#     for i in range(len(population_list) - 1, 0, -1):
#         population_list[i] = population_list[i - 1]
#     population_list[0] = 0
#     return population_list

import random
import string

def increment_population_age(population_list):
    result_list = []
    for jackalope in population_list:
        jackalope['age'] += 1
        if jackalope['age'] <= 10:
            result_list.append(jackalope)
    return result_list

def create_jackalope():
    return {'name': random.choice(string.ascii_uppercase), 'age': 0, 'gender': random.choice('mf'), 'pregnant': False}


# Gestation of year.
gestation_period = 1

# population = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
population = [{'name': random.choice(string.ascii_uppercase), 'age': 0, 'gender': 'm', 'pregnant': False}, {'name': random.choice(string.ascii_uppercase), 'age': 0, 'gender': 'f', 'pregnant': False}]

year_counter = 0

reproductive_age_low = 3
reproductive_age_high = 9

while len(population) < 1000 and year_counter < 100:
    year_counter += 1
    print(f'\n\nYear: {year_counter}\n')
    # We create babies.
    temp_population = []
    for jackalope in population:
        if jackalope['pregnant']:
            jackalope['pregnant'] = False
            # Create two baby jackalopes and add them to the population
            temp_population.append(create_jackalope())
            temp_population.append(create_jackalope())

    print(f'New babies: {len(temp_population)}')
    population.extend(temp_population)

    # increment population age groups
    population = increment_population_age(population)
    print(f'Current population: {len(population)}')

    # calculate population in reproductive range
    # Need to get population of idices 4 through 8 inclusive.
    # for i in range(4, 9):
    #     reproductive_population += population[i]
    # Will need to track m/f population.
    reproductive_population = [0,0,0,0,0]
    number_reproductive_males = [0,0,0,0,0]
    number_reproductive_females = [0,0,0,0,0]
    for jackalope in population:
        # Use functions to test: use function with print (or something) for each expression in the condition.
        # See if all expressions are evaluated even if first conditional is false.
        age_of_this_jackalope = jackalope['age']
        if reproductive_age_low < age_of_this_jackalope < reproductive_age_high:
            # reproductive_population += 1
            if jackalope['gender'] == 'm':
                number_reproductive_males[age_of_this_jackalope - 4] += 1
            else:
                number_reproductive_females[age_of_this_jackalope - 4] += 1
    
    for i in range(5):
        reproductive_population[i] = min(number_reproductive_males[i], number_reproductive_females[i])

    print(f'Mating jackalopes - Male: {len(number_reproductive_males)} Female: {len(number_reproductive_females)}')
    temp_counter = sum(reproductive_population)
    for jackalope in population:
        if temp_counter <= 0:
            break
        elif jackalope['gender'] == 'f':
            jackalope['pregnant'] = True
            temp_counter -= 1

# Let's get the final population:
print(f'''
It's this many years:
{year_counter}!!!
{len(population)}
''')

# It's this many years:
# 24!!!
# [314, 236, 178, 134, 102, 76, 58, 44, 34, 24, 18]
# 1218

