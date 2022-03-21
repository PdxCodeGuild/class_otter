let cards = { 'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }

let firstCard = 'What is your first card?'
let secondCard = 'What is your second card?'
let thirdCard = 'What is your third card?'

let firstInput = prompt(firstCard)

let secondInput = prompt(secondCard)

let thirdInput = prompt(thirdCard)

function blackJack(a, b, c) {
    let total = a + b + c
    if (total === 21) {
        alert('Black Jack!')
    }
    else if (total >= 17) {
        alert('Stay and hold')
    }
    else if (total < 17) {
        alert('Hit')
    }
    else if (total > 21) {
        alert('Busted')
    }
}
blackJack(cards[firstInput], cards[secondInput], cards[thirdInput])