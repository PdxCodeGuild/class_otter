"""
Lab 5: Pick 6
Version 1 and 2
"""
import random


def ticket(a = 1, b = 99):
    
    pick = []
    
    for i in range(6):
       pick.append(random.randint(a, b))
    return pick

winTic = ticket()
payouts = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}

cost = 0
payout = 0
counter = 0

while counter < 100000:
    playTic = ticket()
    score = 0
    counter += 1
    cost += 2
    
    for num in range(6):

        if winTic[num] == playTic[num]:
            score += 1
        
    payout += payouts[score]
 
roi = ((payout - cost) / cost)

print()
print(f'Payout: ${payout}')
print(f'Cost: ${cost}')
print(f'Return on Investment: ${roi}')
print()