import random

def pick6():
    
    num_list = []

    for x in range(6):
       num_list.append(random.randint(1,99))
       
    return num_list

print('\nWelcome to Pick6!\n')

winning = pick6()

ticket = pick6()

print(f'Winning numbers: {winning}')
print(f'Ticket numbers : {ticket}')

def num_matches(winning,ticket):
    matches=0

    for i in range(6):
        
        if winning[i] == ticket[i]:
            matches += 1
    return matches

print(num_matches(winning,ticket))

match_val = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}


