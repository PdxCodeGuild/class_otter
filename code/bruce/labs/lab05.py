# ************************************ #
#                Pick6                 #
#   Make big money on the lottery!!!   #
#             Version: 1.0             #
#         Author: Bruce Stull          #
#              2022-01-07              #
# ************************************ #

# Assignment
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/05%20Pick%206.md

import random

# Function to generate a list of 6 random numbers between and including 1 and 99.
def generate_ticket(number_of_picks = 6, low = 1, hi = 99):
    '''Function to generate list of 6 numbers between low and hi numbers.'''
    ticket = []
    for _ in range(number_of_picks):
        ticket.append(random.randint(low,hi))
    return ticket

def test_generate_ticket():
    assert len(generate_ticket(7)) == 7
    assert len(generate_ticket(6)) == 6
    assert len(generate_ticket()) == 6
    assert len(generate_ticket(5)) == 5

def generate_customer_ticket(number_of_picks = 6):
    '''Function to generate a customer list of numbers by using generate_ticket. Default is a list of 6 items.'''
    return generate_ticket(number_of_picks)

def test_generate_customer_ticket():
    assert len(generate_customer_ticket()) == 6
    assert len(generate_customer_ticket(6)) == 6
    assert len(generate_customer_ticket(7)) == 7
    assert len(generate_customer_ticket(5)) == 5
    
def generate_winning_ticket(number_of_picks = 6):
    '''Function to generate a winning list of numbers by using generate_ticket. Default is a list of 6 items.'''
    return generate_ticket(number_of_picks)

def test_generate_winning_ticket():
    assert len(generate_winning_ticket()) == 6
    assert len(generate_winning_ticket(6)) == 6
    assert len(generate_winning_ticket(7)) == 7
    assert len(generate_winning_ticket(5)) == 5

def how_many_matches(customer_ticket = [], winning_ticket = []):
    '''Returns how many ordered matches of customer_ticket in winning_ticket.'''
    # ### My solution ###
    # matches = 0
    # for i, number in enumerate(customer_ticket):
    #     if number == winning_ticket[i]:
    #         matches += 1
    # return matches
    # ###################

    ### Alternate solutions ###
    # https://github.com/PdxCodeGuild/class_otter/blob/bruce/code/merritt/22-jan/lab05.py
    # Uses zip().
    matches = 0
    # for i in range(len(winning)):
    #     if winning[i] == ticket[i]:
    #         matches += 1
    for customer_number, win_number in zip(customer_ticket, winning_ticket):
        if customer_number == win_number:
            matches += 1
    return matches
    ###########################

def test_how_many_matches():
    assert how_many_matches() == 0
    assert how_many_matches([1, 2, 3, 4],[2, 3, 4, 5, 6, 7]) == 0
    assert how_many_matches([1, 2, 3],[1, 4, 5, 6, 7, 8]) == 1
    assert how_many_matches([1, 2, 3, 4],[7, 2, 5, 4, 1 , 1]) == 2
    assert how_many_matches([2, 4, 6, 8, 10, 12],[2, 4, 5, 5, 10, 12]) == 4
    assert how_many_matches([11, 22, 33, 44, 55, 66],[11, 22, 33, 44, 55, 66]) == 6
    assert how_many_matches([1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]) == 0
    assert how_many_matches([1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 6]) == 1
    assert how_many_matches([1, 2, 3, 10, 5, 6],[7, 8, 9, 10, 11, 6]) == 2
    assert how_many_matches([1, 2, 3, 4, 11, 6],[7, 8, 9, 10, 11, 6]) == 2

# Cost per ticket.
cost_per_ticket = 2

# Dictionary of winnings for given number of matches.
# LOL!!! forgot to include $0.00 winnings for zero matches.
winnings = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}

def winnings_for_ticket(number_of_matches):
    '''Returns the winnings for a given number of matches.'''
    return winnings[number_of_matches]

def test_winnings_for_ticket():
    assert winnings_for_ticket(0) == 0
    assert winnings_for_ticket(1) == 4
    assert winnings_for_ticket(2) == 7
    assert winnings_for_ticket(3) == 100
    assert winnings_for_ticket(4) == 50000
    assert winnings_for_ticket(5) == 1000000
    assert winnings_for_ticket(6) == 25000000

# TODO: Use a dictionary or list to keep track of how many wins of each type of match.
number_of_matches = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

def main():
    # winning_ticket = generate_winning_ticket()
    winning_ticket = generate_ticket()
    initial_balance = 0
    balance = initial_balance
    how_many_tickets_i_can_buy = 10000000000

    earnings = 0
    expenses = 0

    for _ in range(how_many_tickets_i_can_buy):
        # Buy a ticket
        balance -= 2
        expenses += 2
        # customer_ticket = generate_customer_ticket()
        customer_ticket = generate_ticket()
        # Determine winnings.
        i_wish_this_wasnt_so_often_so_close_to_zero = winnings_for_ticket(how_many_matches(customer_ticket,winning_ticket))
        earnings += i_wish_this_wasnt_so_often_so_close_to_zero
        balance += i_wish_this_wasnt_so_often_so_close_to_zero

        number_of_matches[how_many_matches(customer_ticket, winning_ticket)] += 1
    

    # LOL Calculate ROI.
    return_on_investment = (earnings - expenses) / expenses

    results = f"I started with ${initial_balance}.00, then bought {how_many_tickets_i_can_buy} tickets, and I now have ${balance}.00.\nExpenses: ${round(expenses)}\nEarnings: ${round(earnings)}\nA ROI of {return_on_investment}!!!"
    print(results)
    print(number_of_matches)

main()

# LOL One test of 1000000 tickets:
# I started with $0.00, then bought 10000000 tickets, and I now have $-17526075.00.

# Time lapse in powershell:
# Measure-Command { python .\lab05.py }

# Example Measure-Command output:
# PS C:\Users\Bruce\programming\class_otter\code\bruce\week_01> Measure-Command { python .\lab05.py }

# Days              : 0
# Hours             : 0
# Minutes           : 0
# Seconds           : 10
# Milliseconds      : 181
# Ticks             : 101816043
# TotalDays         : 0.000117842642361111
# TotalHours        : 0.00282822341666667
# TotalMinutes      : 0.169693405
# TotalSeconds      : 10.1816043
# TotalMilliseconds : 10181.6043

# Best results I've seen:

# I started with $0.00, then bought 1000000 tickets, and I now have $-1706576.00.
# Expenses: $2000000
# Earnings: $293424
# A ROI of -0.853288!!!

# I started with $0.00, then bought 1000000 tickets, and I now have $-1706621.00.
# Expenses: $2000000
# Earnings: $293379
# A ROI of -0.8533105!!!
# {0: 940679, 1: 57876, 2: 1425, 3: 19, 4: 1, 5: 0, 6: 0}

# I started with $0.00, then bought 1000000 tickets, and I now have $-1706992.00.
# Expenses: $2000000
# Earnings: $293008
# A ROI of -0.853496!!!
# {0: 940879, 1: 57626, 2: 1472, 3: 22, 4: 1, 5: 0, 6: 0}

######################## Large data sets ########################
# I started with $0.00, then bought 10000000 tickets, and I now have $-17572943.00.
# Expenses: $20000000
# Earnings: $2427057
# A ROI of -0.87864715!!!
# {0: 9408595, 1: 576568, 2: 14655, 3: 182, 4: 0, 5: 0, 6: 0}

# I started with $0.00, then bought 100000000 tickets, and I now have $-175014307.00.
# Expenses: $200000000
# Earnings: $24985693
# A ROI of -0.875071535!!!
# {0: 94086755, 1: 5763967, 2: 147275, 3: 1989, 4: 14, 5: 0, 6: 0}

# I started with $0.00, then bought 1000000000 tickets, and I now have $-1748190431.00.
# Expenses: $2000000000
# Earnings: $251809569
# A ROI of -0.8740952155!!!
# {0: 940895299, 1: 57614127, 2: 1470323, 3: 20108, 4: 141, 5: 2, 6: 0}

#################################################################