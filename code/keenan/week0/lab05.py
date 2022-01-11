# Lab 5: Pick6 Lottery Simulation
# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and
# the winning numbers determines the payoff. Order matters, if the winning numbers are 
# [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning 
# numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. 
# Calculate your net winnings (the sum of all expenses and earnings).


import random

ticket_cost = 2
balance = 0


# dictionary containing the number of matches to the corresponding dollar amount of winnings
winnings = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000,
    }

# define a function that will generate a 5 member list with random nums 1-99
def pick6():
    list = [] 
    for i in range(7):
        num = random.randint(1,99)
        list.append(num)
    return list

matches = 0
# define a function to compare the winning numbers to the ticket numbers
def num_matches(winning, ticket):
    matches = 0
    for i in range(7):
        if winning[i] == ticket[i]:
            matches += 1
    return matches

for i in range (100000):
    winning_nums = pick6()
    ticket_nums = pick6()
    balance -= 2
    matches = num_matches(winning_nums, ticket_nums)
    balance += winnings[matches]


expenses = 100000 * ticket_cost
earnings = 200000 + balance
roi = (earnings - expenses) / expenses * 100
roi = round(roi, 3)


# print(f'{earnings} dollars earned.')

# # Version 2: The ROI is defined as (earnings - expenses)/expenses.
# # Calculate your ROI and print it out along with earnings and expenses.

print(f'\n${earnings} is your earnings')
print(f'Expenses were $200000')
print(f'Your return on investment was {roi}%')

