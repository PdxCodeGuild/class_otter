# Mob Programming: Jackalope Simulator
# 01/26/2022
# Nick Corner, Scott Madden, Keenan Tabusa

# Version 1
# The goal is to calculate how many years it will take for two jackalopes (starting at age 0) to create a population of 1000.

# Jackalopes are reproductive from ages 4-8 and die at age 10.
# Gestation is instantaneous. Each gestation produces two offspring.
# Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
# With these conditions in mind, we can represent our population as a list of ints.


population_list = [0,0]
year = 0

while len(population_list) < 1000:
    for i in range(len(population_list)):
        population_list[i] += 1
    # for ele in population_list:
    #     if population_list [i] == 10:
    #         population_list.remove(10)
    for i in range(len(population_list)-1-1-1):
        if population_list [i] == 10:
            population_list.pop(i)
        
            # population_list.remove(population_list[i])
    for i in range(len(population_list)):  
        if population_list[i] >= 4 and population_list[i] <= 8:
         population_list.append(0)
    year += 1

        

        # if age in population_list > 4 and age in population_list < 9:
        #     population_list.append(0)
        # if age > 3 and age < 9, new age 0 jackalopes is increased by 2 * the number of pairs in this age bracket
        # if age > 8, then no reproductive activity
    #     # if age > 9  population -= the pairs
print(population_list)
    print('\npopulation:',len(population_list))
    # year += 1 
print('Year:', year)


# Version 2
# Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. A jackalope will have the following properties:

# name
# age
# sex
# whether they're pregnant
# Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.