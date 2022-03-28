var points = {a: 1, A: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
     9: 9, 10: 10, j: 10, J: 10, q: 10, Q: 10, k: 10, K: 10, none: 0}

var card1 = prompt("What is your first card? ")
var card2 = prompt("What is your second card? ")
var card3 = prompt("What is your third card? ")

function score(a, b){
    let x = points[a] + points[b]
    return x
}

var advice = score(card1, card2) + points[card3]

if ((points[card1] === 10 && card2 === 'A') || (card1 === 'A' && points[card2] === 10)){
    advice = 21
    alert("Blackjack")
}

else if ((points[card1] === 10 && card2 === 'a') || (card1 === 'a' && points[card2] === 10)){
    advice = 21
    alert("Blackjack")
}

else if (advice > 21){
    alert("Busted")
}

else if (advice === 21){
    alert("Blackjack")
}

while (advice < 21){
    if (advice < 17){
        alert("Hit")
    }
    else if (advice >= 17 && advice < 21){
        alert("Stay")
        break
    }
    else if (advice > 21){
        alert("Busted")
    }
    var nextCard = prompt("What is your next card? ")

    if ((advice === 10 && nextCard === 'A') || (advice === 10 && nextCard === 'a')){
        alert("Blackjack")
        break
    }
    else if ((advice + points[nextCard]) > 21){
        alert("Busted")
    }
    else if ((advice + points[nextCard]) === 21){
        alert("Blackjack")
    }

    advice += points[nextCard]
}