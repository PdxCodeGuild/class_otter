population_list = [0,0]
year = 0

while year < 12:
    for i in range(len(population_list)):
        if population_list[i] == 10:  
            population_list.remove(int(10))
        if population_list[i] >= 4 and population_list[i]<9:
            population_list.append(0)

        # elif population_list[i] == 10:
            # population_list.remove(10)
        
        population_list[i] += 1

        # if age in population_list > 4 and age in population_list < 9:
        #     population_list.append(0)
        # if age > 3 and age < 9, new age 0 jackalopes is increased by 2 * the number of pairs in this age bracket
        # if age > 8, then no reproductive activity
        # if age > 9  population -= the pairs
    print(population_list)
    print('\npopulation:',len(population_list))
    year += 1 
    print('\nYear:', year)