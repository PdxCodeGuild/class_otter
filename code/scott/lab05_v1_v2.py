# Pick 6 Lab05 Version 1 and 2 - Scott Madden
import random
count = 0 # Number of times tickets are matched to house
winnings = 0 # Winnings total
total_matched = 0 # total of numbers matched
#Match payout amounts
payouts = {
    0 : 0,
    1 : 4,
    2 : 7,
    3 : 100,
    4 : 50000,
    5 : 1000000,
    6 : 25000000 
}

while count < 100000:
    def pick6(): # player ticket number selection
        return[random.randint(1,99) for _ in range(6)]
        # ticket = []
        # for _ in range(6):
        #     ticket.append(random.randint(1, 99))
        # return ticket
    def draw(): # House number selection
        nums = []
        for _ in range(6):
            nums.append(random.randint(1, 99))
        return nums
    play = pick6()
    house = draw()
    
# Tally number matches between ticket and house
    matches = 0 
    for i in range(len(play)):
        if play[i] == house[i]:
            matches += 1
#def matches(play, house)
    # for win, tix in zip(winning, ticket):
    # if win == tix:
    #     matches +=
##subtract cost of ticket and add payout
    if matches == 0 and matches < 1:
        count = count + 1
        winnings = winnings + payouts.get(matches)
    elif matches == 1 and matches < 2:
        count = count + 1
        total_matched = total_matched + matches
        winnings = winnings + payouts.get(matches)    
    elif matches == 2 and matches < 3:
        count = count + 1
        total_matched = total_matched + matches
        winnings = winnings + payouts.get(matches)    
    elif matches == 3 and matches < 4:
        count = count + 1
        total_matched = total_matched + matches 
        winnings = winnings + payouts.get(matches)       
    elif matches == 4  and matches < 5:
        count = count + 1
        total_matched = total_matched + matches 
        winnings = winnings + payouts.get(matches)
    elif matches == 5 and matches < 6:
        count = count + 1
        total_matched = total_matched + matches 
        winnings = winnings + payouts.get(matches)
    elif matches == 6:
        count = count + 1
        total_matched = total_matched + matches 
        winnings = winnings + payouts.get(matches)
costs = (count * 2 )
roi = (winnings - costs)/ costs

print ('\ntimes played' , count)
print ('Cards Matched', total_matched)
print ('Player Expenses $' , costs)
print ('Player Earnings $' , winnings)
print ('Your Return On Investment is:' , roi)

