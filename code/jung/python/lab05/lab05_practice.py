import random
# Create a function of pick6 to generate 6 random numbers between 1-99
def pick6():
    count = 0
    list = []
    while count < 6:
        number = random.randint(1,99)
        list.append(number)
        count += 1
    return list

# Assign winning number   
winning = pick6()

def num_matches(winning, my_pick):
    match = 0
    for i in range(len(winning)):
        if my_pick[i] == winning[i]:
            match += 1
        return match
        


# Loop 100,000 times of pick6
# every time it loops, the cost is $2
balance = 0
for trial in range(100000):
    my_pick = pick6()
    balance -= 2
    matches = num_matches(winning, my_pick)
    if matches == 1:
        balance += 4
    elif matches == 2:
        balance += 7
    elif matches == 3:
        balance += 100
    elif matches == 4:
        balance += 50000
    elif matches == 5:
        balance += 1000000
    elif matches == 6:
        balance += 25000000 
print(f"your balance is: {balance}")

# if number in pick 6 matches winning number,
## add it to balance

# Final balance