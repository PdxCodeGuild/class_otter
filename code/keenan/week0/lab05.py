# Lab 5: Pick6 Lottery Simulation
# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and
# the winning numbers determines the payoff. Order matters, if the winning numbers are 
# [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning 
# numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. 
# Calculate your net winnings (the sum of all expenses and earnings).


import random

# Note: official python documentation is to use a '_' for a variable that will not be 
# used elsewhere (instead of x or i)
# Note: this code below can also be updated with list comprehensions
# list comp: taking a list and appending things to it
# define what we want to do first, or define a variable
#   return [random.randint(1,99) for _ in range(6)]

def pick6():
    list = [] 
    for i in range(6):
        num = random.randint(1,99)
        list.append(num)
    return list



# define a function to compare the winning numbers to the ticket numbers
def num_matches(winning, ticket):
    matches = 0
    for i in range(6):
        if winning[i] == ticket[i]:
            matches += 1
    return matches
# list comprehension won't work here, this section of code just generates a single number
# this would use a function called reduce.



# dictionary containing the number of matches to the corresponding dollar amount of winnings
winnings = {
    0: 0,
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
    }

# creating a dictionary to capture the distribution of the matches
number_of_matches = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

winning_nums = pick6()

balance = 0
earnings = 0
expenses = 0

# loop through 100k tickets to see what the earnings and balance were
for i in range (100000):
    ticket_nums = pick6()
    balance -= 2
    expenses += 2
    matches = num_matches(winning_nums, ticket_nums)
    balance += winnings[matches]
    earnings += winnings[matches]
    number_of_matches[matches] += 1

# Version 2: The ROI is defined as (earnings - expenses)/expenses.
# Calculate your ROI and print it out along with earnings and expenses.

roi = round((earnings - expenses) / expenses * 100, 2)

print(f'\n${earnings} is your earnings')
print(f'Expenses were ${expenses}')
print(f'Your return on investment was {roi}%')
print("Here is the distribution of the matches: ", number_of_matches)

# print("balance: ", balance)
# print("earnings: ", earnings)
# print("expenses: ", expenses)
# print("roi: ", roi, '%')