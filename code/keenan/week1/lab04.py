# Lab 4: Blackjack Advice
# 01/10/2022

# Let's write a python program to give basic blackjack playing advice during a
# game by asking the player for cards. First, ask the user for three playing
# cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point
# value of each card individually. Number cards are worth their number, all
# face cards are worth 10. At this point, assume aces are worth 1.


# Use the following rules to determine the advice:
# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.

# dictionary of card values
value_dictionary = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}

print("\n Note: Card selections should be: 2 through 10, and A, J, Q, or K\n")

hand = []

# get user inputs for the cards in hand and add them to a list
hand.append(input("What's your first card: "))
hand.append(input("What's your second card: "))
hand.append(input("What's your third card: "))


value = 0

# can add an if '' in value_dictionary, to verify that the inputs are valid
i = 0
while i < 3:
    value += value_dictionary[hand[i]]
    i += 1

if value == 21:
    output = str(value) + ' Blackjack!'
elif value < 21 and value >= 17:
    output = str(value) + ' Stay'
elif value < 17:
    output = str(value) + ' Hit'
if value > 21:
    output = str(value) + ' Already Busted'

print(output)
