alert('\nWelcome to the BlackJack Advisor\n')

let card_value = { 'A':1, '1':1, '2':2, '3':3,'4':4, '5':5,
'6':6,'7':7, '8':8, '9':9,'10':10, 'J':10, 'Q':10, "K":10 }

let user_1 = prompt('\nWhat is your first card?\n').toUpperCase()
console.log(user_1)

let user_2 = prompt('\nWhat is your second card?\n').toUpperCase()
console.log(user_2)

let user_3 = prompt('\nWhat is your third card?\n').toUpperCase()
console.log(user_3)

let user_points = card_value[user_1] + card_value[user_2] + card_value[user_3]
console.log(user_points)

if (user_points <= 17) {
    alert(`${user_points}, HIT`)
}

else if (user_points >= 17 && user_points < 21) {
    alert(`${user_points}, STAY`)
}

else if (user_points === 21 ) {
    alert(`${user_points}, BLACKJACK!`)
}

else if (user_points > 21) {
    alert(`${user_points}, ALREADY BUSTED!`)
}