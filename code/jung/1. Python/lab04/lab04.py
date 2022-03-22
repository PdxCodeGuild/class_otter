import random

# Create a card_list
card_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# Generate random three cards from card_list
# Create my_list to store three cards
count = 0
my_list = []
while count < 3:
    random_card = random.choice(card_list)
    my_list.append(random_card)
    count += 1
print(my_list)

# Create a dictionary of cards with appropriate score
card_score = {
    "A" : 11,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
}


# Iterate through my_list and add score 
## if card is "A", there are two options unless adding 11 over 21.

score = 0
for card in my_list:
    number = card_score[card]
    score += number

for card in my_list:
    if card == "A":
        if score > 21:
            score -= 10
print(f"score is: {score}")


if score < 17:
    print("Hit")
elif 17 <= score < 21:
    print("Stay")
elif score == 21:
    print("Blackjack!")
else:
    print("Already Busted")