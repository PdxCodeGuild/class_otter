# BlackJack Advice lab04 - Scott Madden
card_values = {
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

print("\n*** Card selection should be: 2 through 10, A, J, Q, K ***\n")

first_card = input('What is your first card?')
second_card = input('what is your second card?')
third_card = input('what is your third card?')

first_card_value = card_values.get(first_card)
second_card_value = card_values.get(second_card)
third_card_value = card_values.get(third_card)

total = first_card_value + second_card_value + third_card_value

print('Your Hand total is:', total)

if total < 17:
    print('Take a Hit')
elif total >= 17 and total < 21:
    print('Stay')
elif total == 21:
    print('You have a Blackjack!')
else:
    print('You Busted!')