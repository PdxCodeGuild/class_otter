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
    alert(firstCard)
}
else{
    firstCard = cards[choice]
    alert(firstCard)
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

let result = (firstCard + secondCard + thirdCard)
alert(result)
if (result == 21){
    alert('You Have Blackjack!')
}
else if (result < 17){
    alert('Hit')
}
else if (result >= 17 < 21){
    alert('Stay')
}
else if (result > 21){
    alert('You Have Busted!')
}