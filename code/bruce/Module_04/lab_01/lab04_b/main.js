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

let theInputBox = document.createElement('input')
// console.log(theInputBox)


let theDisplayElement = document.createElement('p')
// console.log(theDisplayElement)

let theButtonElement = document.createElement('button')
// console.log(theButtonElement)

document.body.appendChild(theInputBox)

// let theLineBreak1 = document.createElement('br')
// let theLineBreak2 = document.createElement('br')
// document.body.appendChild(theLineBreak1)
// document.body.appendChild(theLineBreak2)

// Add two line breaks.
for (let i=0; i < 2; i++) {
    let aLineBreak = document.createElement('br')
    document.body.appendChild(aLineBreak)
}

document.body.appendChild(theButtonElement)
document.body.appendChild(theDisplayElement)

theInputBox.placeholder = "Input card rank here"

theButtonElement.innerText = "Give me BlackJack Advice"

theButtonElement.addEventListener('click', giveAdvice)


// Listen on 'theInputBox' for 'Enter' key. 'click' the button if 'Enter' is pressed while in 'theInputBox'.
theInputBox.addEventListener("keyup", function(event) {
  if (event.key == 'Enter') {
    // Cancel the default action, if needed
    event.preventDefault()
    theButtonElement.click()
  }
})


theInputBox.focus()

let totalScore = 0

function giveAdvice() {
    console.log("I'm giving advice!!!!")
    cardRank = theInputBox.value.toUpperCase()
    theInputBox.value = ''
    // console.log(cardRank)

    let theCurrentCardValue = getCardValue(cardRank)
    console.log(`Current Card Score: ${theCurrentCardValue}`)

    totalScore += theCurrentCardValue
    console.log(`Total Score: ${totalScore}`)

    theAdvice = advise(totalScore)
    console.log(theAdvice)
    
    if (totalScore == 21) {
        theDisplayElement.style.fontSize = "xx-large"
    }

    theDisplayElement.innerText = `${totalScore} : ${theAdvice}`

    theInputBox.focus()
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


function advise(score) {
    if (score > 21) {
        return "You're Busted! Womp Womp!"
    } else if (score == 21) {
        return "BlackJack! Winner! Winner!"
    } else if (score >= 17) {
        return "Whoah! Stay!"
    } else {
        return "Hit me!"
    }
}
