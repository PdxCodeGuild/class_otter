# Full Stack Bootcamp - Unit 01 Lab 05
# Justin Hammond, 01/06/2022


'''
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters,
if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your
ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
    if 1 number matches, you win $4
    if 2 numbers match, you win $7
    if 3 numbers match, you win $100
    if 4 numbers match, you win $50,000
    if 5 numbers match, you win $1,000,000
    if 6 numbers match, you win $25,000,000

One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and
tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps
    Generate a list of 6 random numbers representing the winning tickets
    Start your balance at 0
    Loop 100,000 times, for each loop:
    Generate a list of 6 random numbers representing the ticket
    Subtract 2 from your balance (you bought a ticket)
    Find how many numbers match
    Add to your balance the winnings from your matches
    After the loop, print the final balance
'''
import random


def pick_6():
    result = []

    for _ in range(6):
        result.append(random.randint(1, 99))

    return result

def test_pick_6():
    ticket = pick_6()
    assert len(ticket) == 6
    for num in ticket:
        assert num > 0 and num < 100

def get_number_of_matches(ticket, winning_numbers):
    match_count = 0
    for index in range(len(ticket)):
        if ticket[index] == winning_numbers[index]:
            match_count += 1
    return match_count

def test_get_number_of_matches():
    winners = [56, 34, 12, 1, 85, 57]
    assert get_number_of_matches([56, 93, 84, 24, 56, 23], winners) == 1
    assert get_number_of_matches([31, 34, 12, 35, 19, 57], winners) == 3
    assert get_number_of_matches([7, 54, 19, 37, 13, 35], winners) == 0
    assert get_number_of_matches([38, 34, 73, 98, 82, 46], winners) == 1

prize_tiers = {
    1: 4,
    2: 7,
    3: 100,
    4: 50000,
    5: 1000000,
    6: 25000000
}

def get_prize(match_count):
    if match_count > 0 and match_count < 7:
        return prize_tiers[match_count]
    else:
        return 0

def test_get_prize():
    assert get_prize(1) == 4
    assert get_prize(2) == 7
    assert get_prize(3) == 100
    assert get_prize(4) == 50000
    assert get_prize(5) == 1000000
    assert get_prize(6) == 25000000

    assert get_prize(0) == 0
    assert get_prize(7) == 0
    assert get_prize(-1) == 0
    assert get_prize(33) == 0


def main():
    winning_numbers = pick_6()
    balance = 0

    for _ in range(100000):
        ticket = pick_6()
        balance -= 2
        match_count = get_number_of_matches(ticket, winning_numbers)
        balance += get_prize(match_count)

    print(balance)


main()