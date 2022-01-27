import random

num_cards = [2,3,4,5,6,7,8,9,10,"A","J","Q","K"]

face_cards = {"A" : 1, "J" : 10, "Q": 10, "K" : 10}
cards =[]

first = random.choice(num_cards)
print(f"here is your first card: {first}")

second = random.choice(num_cards)
print(f"here is your second card: {second}")

third = random.choice(num_cards)
print(f"here is your third card: {third}")

cards.append(first)
cards.append(second)
cards.append(third)

for i in range(len(cards)):
    if cards[i] in face_cards:
        print(cards[i],i)   
        cards[i] = face_cards[cards[i]]
        
#print(cards)

total_card = 0

for card in cards:
    total_card += card

#print(total_card)



#total = first + second + third

if total_card <= 17:
    print("try again")
elif total_card <= 20:
    print("almost try again")
elif total_card == 21:
    print("you win!")
elif total_card > 21:
    print("bust!")


print(total_card)













'''import random

first = random.randint(1,10)
print(f"here is your first card: {first}")

second = random.randint(1,10)
print(f"here is your second card: {second}")

third = random.randint(1,10)
print(f"here is your third card: {third}")

#print(f"{first} + {second} + {third}" )

total = first + second + third

if total <= 17:
    print("try again")
elif total <= 20:
    print("almost try again")
elif total == 21:
    print("you win!")
elif total > 21:
    print("bust!")


''''''first = int(input("what is your first hand? "))
second = int(input("what is your second hand? "))
third = int(input("what is your third hand? "))'''

'''if  first <= 17:
    print("Hit!")
elif second <= 21 :
    print("stay")
elif third == 21:
    print("blackjack!")
elif third > 21:
    print("youlose!")


print(total)'''