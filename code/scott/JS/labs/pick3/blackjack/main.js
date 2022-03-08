var cards = {
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
}

var face = {
    'A':1,
    'J':10,
    'Q':10,
    'K':10
}

let choice = prompt('What is your first card?: ')
let choice2 = prompt('What is your second card?: ')
let choice3 = prompt('What is your third card?: ')

let total = 0 

if (choice in face){
    firstCard = face[choice]
}
else{
    firstCard = cards[choice]
}

if(choice2 in face){
    secondCard = face[choice2]
}
else{
    secondCard = cards[choice2]
}
if(choice3 in face){
    thirdCard = face[choice3]
}
else{
    thirdCard = cards[choice3]
}

result = (firstCard + secondCard + thirdCard)

if (result < 17){
    alert('Take a Hit')
}
else if (result >= 17 < 21){
    alert('Stay')
}
else if (result == 21){
    alert('You have a Blackjack!')
}
else{
    alert('You Have Busted!')
}

// Original Python Was 
// card_values = {
//     'A': 1, 
//     '2': 2, 
//     '3': 3, 
//     '4': 4, 
//     '5': 5, 
//     '6': 6, 
//     '7': 7,
//     '8': 8, 
//     '9': 9, 
//     '10': 10, 
//     'J': 10, 
//     'Q': 10,  
//     'K': 10
// }

// print("\n*** Card selection should be: 2 through 10, A, J, Q, K ***\n")

// first_card = input('What is your first card?')
// second_card = input('what is your second card?')
// third_card = input('what is your third card?')

// first_card_value = card_values.get(first_card)
// second_card_value = card_values.get(second_card)
// third_card_value = card_values.get(third_card)

// total = first_card_value + second_card_value + third_card_value

// print('Your Hand total is:', total)

// if total < 17:
//     print('Take a Hit')
// elif total >= 17 and total < 21:
//     print('Stay')
// elif total == 21:
//     print('You have a Blackjack!')
// else:
//     print('You Busted!')