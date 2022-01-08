# Pick 6 Lab05
import random

payouts = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000 
}

def pick6():
    ticket = []
    for _ in range(6):
        ticket.append(random.randint(1, 99))
    return ticket

def winning_nums():
    nums = []
    for _ in range(6):
        nums.append(random.randint(1, 99))
    return nums

ticket = pick6()
win = winning_nums()

matches = 0
for i in range(len(ticket)):
    if win[i] == ticket[i]:
        matches += 1

count = 0        
winnings = 0 
if matches == 0 and matches < 1:
    count = count + 1
    winnings = winnings + payouts.get(matches)
elif matches == 1 and matches < 2:
    count = count + 1
    winnings = winnings + payouts.get(matches)    
elif matches == 2 and matches < 3:
    count = count + 1
    winnings = winnings + payouts.get(matches)    
elif matches == 3 and matches < 4:
    count = count + 1 
    winnings = winnings + payouts.get(matches)       
elif matches == 4  and matches < 5:
    count = count + 1 
    winnings = winnings + payouts.get(matches)
elif matches == 5 and matches < 6:
    count = count + 1 
    winnings = winnings + payouts.get(matches)
elif matches == 6:
    count = count + 1 
    winnings = winnings + payouts.get(matches)        
    
    
        
# winnings = ()
# payouts = {
#     0 : 0,
#     1 : 4,
#     2 : 7,
#     3 : 100,
#     4 : 50000,
#     5 : 1000000,
#     6 : 25000000
# }