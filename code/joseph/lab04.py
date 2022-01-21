# Lab 4 - Blackjack Advice
cards_value = {
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
    'K': 10
}

print("Cards will be 2-10, J, Q, K, A")

card_one = input("What is your first card?")
card_two = input("What is your second card?")
card_three = input("What is your third card?")

card_one_value = cards_value.get(card_one)
card_two_value = cards_value.get(card_two)
card_three_value = cards_value.get(card_three)

hand = card_one_value + card_two_value + card_three_value

print("You have: ", hand)

if hand < 17:
    print("Hit it!")
elif hand >= 17 and hand < 21:
    print("Stay!")
elif hand == 21:
    print("Blackjack!")
else:
    print("You done busted!")