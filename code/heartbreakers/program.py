# Version 1
# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

#     Jackalopes are reproductive from ages 4-8 and die at age 10.
#     Gestation is instantaneous. Each gestation produces two offspring.
#     Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
#     With these conditions in mind, we can represent our population as a list of ints.

def increment_population(population_list):
    for i in range(len(population_list) - 1, 0, -1):
        population_list[i] = population_list[i - 1]
    population_list[0] = 0
    return population_list


population = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

year_counter = 0

while sum(population) < 1000:
    year_counter += 1

    # increment population age groups
    population = increment_population(population)

    # calculate population in reproductive range
    reproductive_population = 0
    # Need to get population of idices 4 through 8 inclusive.
    for i in range(4, 9):
        reproductive_population += population[i]
    
    if reproductive_population  > 0:
        # if odd, remove 1
        if reproductive_population % 2 == 1:
            reproductive_population -= 1
        # make babies; update population count
        # Every pair of parents are going to have two offspring. So...
        # Number of babies is going to equal number of parents.
        population[0] = reproductive_population

# Let's get the final population:
print(f'''
It's this many years:
{year_counter}!!!
{population}
{sum(population)}
''')