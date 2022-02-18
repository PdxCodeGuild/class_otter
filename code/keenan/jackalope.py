# Mob Programming: Jackalope Simulator
# 01/26/2022
# Nick Corner, Scott Madden, Keenan Tabusa

# Version 1
# The goal is to calculate how many years it will take for two jackalopes (starting at age 0) to create a population of 1000.

# Jackalopes are reproductive from ages 4-8 and die at age 10.
# Gestation is instantaneous. Each gestation produces two offspring.
# Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
# With these conditions in mind, we can represent our population as a list of ints.

# this list will capture ages of each individual member of the population
population_list = [0,0]
year = 0

while len(population_list) < 1000:
    for i in range(len(population_list)):
        # if the sort function is ordered in this way we can 'skip' our index of interest by removing a line item at [0] and shifting the list order over by an index.
        # this bumps the other '10' value to index [0] and we cycle past it
        if population_list[i] == 10:
            population_list.remove(10)
            pass
        elif population_list[i] >= 3 and population_list[i] < 9:
            population_list.append(0)
        elif population_list[i] == 9:
            pass
        population_list[i] += 1
        # if age in population_list > 4 and age in population_list < 9:
        #     population_list.append(0)
        # if age > 3 and age < 9, new age 0 jackalopes is increased by 2 * the number of pairs in this age bracket
        # if age > 8, then no reproductive activity
        # if age > 9  population -= the pairs
    print(population_list)
    print(len(population_list))
    year += 1 

print(f'It would take {year} years for the population of jackalopes to exceed 1000.')
print(f'The total number of jackalopes in year {year} is {len(population_list)}.')




# Version 2
# Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. A jackalope will have the following properties:

# name
# age
# sex
# whether they're pregnant
# Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.


# year =  0
# jackalope_population = 2
# jackalope_startingpopulation = 2
# jackalope_marriage_i = 4
# jackalope_marriage_f = 8
# jackalope_list = []
# class Jackalope:
#     def __init__(self, age):
#         self.age = int(age)
# def jackalope_married(jackalope_marriage_i , jackalope_marriage_f):
#     for jackalope in jackalope_list:
#         if jackalope.age > jackalope_marriage_i:
#             if jackalope.age < jackalope_marriage_f:
#                 jackalope_list.append(Jackalope(0))
# def jackalope_aged():
#     for jackalope in jackalope_list:
        

# #population to 1000   
# # while jackalope_population < 1001:
# #     jackalope_married(jackalope_marriage_i, jackalope_marriage_f)
# #     print(len(jackalope_dict))
# #     year = year + 1

