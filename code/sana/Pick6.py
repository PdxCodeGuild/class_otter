import random
matches = {
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000
}
balance = 0
earnings = 0
expenses = 0
for tickets in range(100000):
    winning_ticket = []
    generated_ticket = []
    for x in range(6):
        win_nums = random.randint(1, 99)
    # print(win_nums)
        winning_ticket.append(win_nums)
    print(winning_ticket)
    for x in range(6):
        gen_nums = random.randint(1, 99)
    # print(gen_nums)
        generated_ticket.append(gen_nums)
    print(generated_ticket)
    counter = 0
    for x in range(len(winning_ticket)):
        if winning_ticket[x] == generated_ticket[x]:
            counter = counter + 1
            print(counter)
            x = x + 1
    expenses = expenses + 2
    print(expenses)
    if counter in matches:
        earnings = earnings + matches[counter]
        print(earnings)
    balance = earnings - expenses
    roi = (earnings - expenses) / expenses
print(f"This is your balance is ${balance} and ROD is {roi}")