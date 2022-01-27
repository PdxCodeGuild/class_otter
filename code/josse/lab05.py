
# *********************************************************************
# NOTES FROM MERRITT PRACTICE!!!!!
import random


def pick6():
    ticket = []
    for _ in range(6):
        ticket.append(random.randint(1, 99))
    return ticket


def num_matches(winning, ticket):
    matches = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            matches += 1
        return matches


winnings = {6: 25000000, 5: 100000, 4: 50000, 3: 100, 2: 7, 1: 4, 0: 0}

winning_ticket = pick6()

balance = 0
earnings = 0
expenses = 0

for _ in range(100000):
    current_ticket = pick6()
    balance -= 2
    expenses += 2
    matches = num_matches(winning_ticket, current_ticket)
    balance += winnings[matches]
    earnings += winnings[matches]


print("balance:", balance)
print("earnings:", earnings)
print("expenses:", expenses)
print("roi:", (earnings - expenses)/expenses)

# ****************************************************************************
