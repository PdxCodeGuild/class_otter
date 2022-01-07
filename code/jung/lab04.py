# import random

# cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# numbers = []
# card = 0
# while card < 3:
#     chosen_card = random.choice(cards)
#     if chosen_card not in numbers:
#         numbers.append(chosen_card)
#         card += 1
#     else:
#         continue
# print(numbers)

first_card = input("What's your first card? ")
second_card = input("What's your second card? ")
third_card = input("What's your third card? ")

numbers = []
numbers.append(first_card)
numbers.append(second_card)
numbers.append(third_card)

print(numbers)

num_dict = {
    # "A" : 1,
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

total = 0
for card in numbers:
    if card == "A":
        if "A" == 1:
            total += 1
        elif "A" == 11:
            total += 11
    number = num_dict[card]
    total += number
print(total)



if total < 17:
    print("Hit")
elif 17 <= total < 21:
    print("Stay")
elif total == 21:
    print("Blackjack!")
else:
    print("Already Busted")