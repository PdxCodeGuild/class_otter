import random

### VERSION 1 ###

def pick6():
    ticket = []
    for x in range(6):
       ticket.append(random.randint(1,99))
       
    return ticket

def num_matches(win_tix,tix_n_play):
    matches=0
    for i in range(6):
        if win_tix[i] == tix_n_play[i]:
            matches += 1
    return matches

match_val = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}

num_x_match = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

win_tix = pick6()

ern = 0
bal = 0
expns = 0

for i in range(int(100000)):
    tix_n_play = pick6()
    expns += 2
    bal -=2
    matches = num_matches(win_tix,tix_n_play)
    num_x_match[matches] += 1
    ern += match_val[matches]
    bal += match_val[matches]
    
print('\nWelcome to Pick6!\n')
print(f'Winning numbers: {win_tix}')
print(f'Ticket numbers : {tix_n_play}')
print(f'\nNumber matches : {num_x_match}')
print(f'Earnings: {ern}')
print(f'Balance: {bal}')

### VERSION 2 ####

print(f'Return on investment:{(ern - expns)/expns}') 
