# Lab 5 Versions 1 and 2
import random

#define plays, winnings and num,bers matched
wins = 0 # Number of plays
totalw = 0 # Total winnings
totalm = 0 # Number of numbers matched

#define match pays
pays = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000 
}

#determine winner, tie
while wins < 100000:
    def psix(): # player number selection
        return[random.randint(1,99) for _ in range(6)]
        # ticket = []
        # for _ in range(6):
        #     ticket.append(random.randint(1, 99))
        # return ticket
    def tie(): # house number selection
        nums = []
        for _ in range(6):
            nums.append(random.randint(1, 99))
        return nums
    player = psix()
    house = tie()
    
# add up matches between player and house
    matches = 0 
    for i in range(len(player)):
        if player[i] == house[i]:
            matches += 1
#def matches(player, house)
    # for win, tix in zip(winning, ticket):
    # if win == tix:
    #     matches +=
##subtract cost of ticket and add payout
    if matches == 0 and matches < 1:
        wins = wins + 1
        totalw = totalw + pays.get(matches)
    elif matches == 1 and matches < 2:
        wins = wins + 1
        totalm = totalm + matches
        totalw = totalw + pays.get(matches)    
    elif matches == 2 and matches < 3:
        wins = wins + 1
        totalm = totalm + matches
        totalw = totalw + pays.get(matches)    
    elif matches == 3 and matches < 4:
        wins = wins + 1
        totalm = totalm + matches 
        totalw = totalw + pays.get(matches)       
    elif matches == 4  and matches < 5:
        wins = wins + 1
        totalm = totalm + matches 
        totalw = totalw + pays.get(matches)
    elif matches == 5 and matches < 6:
        wins = wins + 1
        totalm = totalm + matches 
        totalw = totalw + pays.get(matches)
    elif matches == 6:
        wins = wins + 1
        totalm = totalm + matches 
        totalw = totalw + pays.get(matches)
costs = (wins * 2 )
roi = (totalw - costs)/ costs

print ("You played this many times:" , wins)
print ("You matched on this many cards:", totalm)
print ("You spent :$" , costs)
print ("You earned :$" , totalw)
print ("Your ROI is:$" , roi)