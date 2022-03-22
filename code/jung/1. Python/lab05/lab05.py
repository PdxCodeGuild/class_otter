#Generate a list of 6 random numbers representing the winning tickets
import random

def pick6():
    numbers = []
    count = 0
    while count < 6:
        number = random.randint(1,99)
        numbers.append(number)
        count += 1
    return numbers


# Start your balance at 0
balance = 0
earnings = 0
#Loop 100,000 times, for each loop:
#Generate a list of 6 random numbers representing the ticket
#Subtract 2 from your balance (you bought a ticket)
winning = pick6()
# my_pick = pick6()

def num_matches(winning, ticket):
    count = 0
    for i in range(len(winning)):
        if winning[i] == ticket[i]:
            count += 1
    return count


for x in range(100000):
    my_pick = pick6()
    balance -= 2

    keep_track = num_matches(winning, my_pick)
    if keep_track == 1:
        earnings += 4
    elif keep_track == 2:
        earnings += 7
    elif keep_track == 3:
        earnings += 100
    elif keep_track == 4:
        earnings += 50000
    elif keep_track == 5:
        earnings += 1000000
    elif keep_track == 6:
        earnings += 25000000
print(f"Your final balance is: ${balance}")


expenses = 2 * 100000
balance = earnings - expenses
roi = (earnings - expenses)/expenses

print(f"Earnings are {earnings}")
print(f"Expenses are {expenses}")
print(f"Balance is {balance}")
print(f"ROI is {roi}")



