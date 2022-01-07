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
def generate_list(number_of_picks = 6, low = 1, hi = 99):
    '''Function to generate list of 6 numbers between low and hi numbers.'''
    list_of_numbers = []
    for i in range(number_of_picks):
        list_of_numbers.append(random.randint(low,hi))
    return list_of_numbers

def test_generate_list():
    assert len(generate_list(7)) == 7
    assert len(generate_list(6)) == 6
    assert len(generate_list()) == 6
    assert len(generate_list(5)) == 5

def generate_customer_list(number_of_picks = 6):
    '''Function to generate a customer list of numbers by using generate_list. Default is a list of 6 items.'''
    return generate_list(number_of_picks)

def test_generate_customer_list():
    assert len(generate_customer_list()) == 6
    assert len(generate_customer_list(6)) == 6
    assert len(generate_customer_list(7)) == 7
    assert len(generate_customer_list(5)) == 5
    
def generate_winning_list(number_of_picks = 6):
    '''Function to generate a winning list of numbers by using generate_list. Default is a list of 6 items.'''
    return generate_list(number_of_picks)

def test_generate_winning_list():
    assert len(generate_winning_list()) == 6
    assert len(generate_winning_list(6)) == 6
    assert len(generate_winning_list(7)) == 7
    assert len(generate_winning_list(5)) == 5

def how_many_matches(customer_list = [], winning_list = []):
    '''Returns how many ordered matches of customer_list in winning_list.'''
    matches = 0
    for i, number in enumerate(customer_list):
        if number == winning_list[i]:
            matches += 1
    return matches

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

def main():
    winning_list = generate_winning_list()
    initial_balance = 0
    balance = initial_balance
    how_many_tickets_i_can_buy = 100000

    earnings = 0
    expenses = 0

    for number_of_tickets in range(how_many_tickets_i_can_buy):
        # Buy a ticket
        balance -= 2
        expenses += 2
        customer_list = generate_customer_list()
        # Determine winnings.
        i_wish_this_wasnt_so_often_so_close_to_zero = winnings_for_ticket(how_many_matches(customer_list,winning_list))
        earnings += i_wish_this_wasnt_so_often_so_close_to_zero
        balance += i_wish_this_wasnt_so_often_so_close_to_zero

    # LOL Calculate ROI.
    return_on_investment = (earnings - expenses) / expenses

    results = f"I started with ${initial_balance}.00, then bought {how_many_tickets_i_can_buy} tickets, and I now have ${balance}.00.\nExpenses: ${round(expenses)}\nEarnings: ${round(earnings)}\nA ROI of {return_on_investment}!!!"
    print(results)

main()

# LOL One test of 1000000 tickets:
# I started with $0.00, then bought 10000000 tickets, and I now have $-17526075.00.