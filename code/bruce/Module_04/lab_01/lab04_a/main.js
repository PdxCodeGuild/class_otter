// Assignment:
    // https://github.com/PdxCodeGuild/class_otter/blob/bruce/4%20JavaScript/labs/Lab%2001-03%20Pick%203.md

// Resources:
    // BlackJack advice:
    // https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/labs/04%20Blackjack%20Advice.md

    
const faceCards = {
    A: 1,
    J: 10,
    Q: 10,
    K: 10,
}


function getFaceCardValue(card) {
    return faceCards[card]
}


function getCardValue(card) {
    if ( isNaN(card) ) {
        return getFaceCardValue(card)
    } else {
        return Number(card)
    }
}


function promptUserAddScore(score) {
    userInput = prompt("Please enter a card:");
    userInputUpper = userInput.toUpperCase();
    console.log('Card value: ' + getCardValue(userInputUpper))
    score += getCardValue(userInputUpper)
    return score
}


function advise(score) {
    if (score > 21) {
        return "Already Busted! Womp Womp!"
    } else if (score == 21) {
        return "BlackJack! Winner! Winner!"
    } else if (score >= 17) {
        return "Whoah! Stay!"
    } else {
        return "Hit me!"
    }
}


function consoleLogOrAlert(alertString, score) {
    let doAlert = true
    currentAdvise = advise(score)
    if (doAlert) {
        window.alert(alertString + score + ' - ' + currentAdvise)
        console.log(alertString + score + ' - ' + currentAdvise)
    } else {
        console.log(alertString + score + ' - ' + currentAdvise)
    }
    return currentAdvise
}


function getBlackJackAdvice() {
    let score = 0;
    let alertString = 'Score: ';
    score = promptUserAddScore(score)
    alertString = 'Cumulative score: ';
    while (true) {
        let advice = consoleLogOrAlert(alertString, score)
        if (advice.includes("Busted")) {
            break
        } else if (advice.includes("Stay")) {
            break
        } else if (advice.includes("BlackJack")) {
            break
        }
        score = promptUserAddScore(score)
    }
}
