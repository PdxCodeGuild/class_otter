import random

def pick6():
    return [random.randint(1,99) for _ in range(6)]
    # ticket = []
    # for _ in range(6):
    #     ticket.append(random.randint(1,99))
    # return ticket

def num_matches(winning, ticket):
    matches = 0
    # for i in range(len(winning)):
    #     if winning[i] == ticket[i]:
    #         matches += 1
    for win, tix in zip(winning, ticket):
        if win == tix:
            matches += 1
    return matches

winnings = {6: 25000000, 5: 1000000, 4: 50000, 3: 100, 2: 7, 1: 4, 0: 0}

number_of_matches = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

winning_ticket = pick6()

balance = 0
earnings = 0
expenses = 0

for _ in range(int(1e9)):
    current_ticket = pick6()
    balance -= 2
    expenses += 2
    matches = num_matches(winning_ticket, current_ticket)
    balance += winnings[matches]
    earnings += winnings[matches]
    number_of_matches[matches] += 1

print("balance:", balance)
print("earnings:", earnings)
print("expenses", expenses)
print("roi:", (earnings - expenses)/expenses)
print(number_of_matches)