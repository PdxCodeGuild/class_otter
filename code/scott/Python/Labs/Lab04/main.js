var cards = {
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

// var face = {
//     'A':1,
//     'J':10,
//     'Q':10,
//     'K':10
// }

let choice = prompt('What is your first card?: ')
let choice2 = prompt('What is your second card?: ')
let choice3 = prompt('What is your third card?: ')

let total = 0 

if (choice in cards){
//     firstCard = face[choice]
// }
// else{
    let firstCard = cards[choice]
}

if(choice2 in cards){
//     secondCard = face[choice2]
// }
// else{
    let secondCard = cards[choice2]
}
if(choice3 in cards){
//     thirdCard = face[choice3]
// }
// else{
    let thirdCard = cards[choice3]
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