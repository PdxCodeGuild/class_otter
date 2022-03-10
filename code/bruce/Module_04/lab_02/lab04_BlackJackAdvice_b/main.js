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

let thePageHeading = document.createElement('h1')
thePageHeading.innerText = "Bunbun's BlackJack Advise"
document.body.appendChild(thePageHeading)

let theInputAmalgamation = document.createElement('div')
theInputAmalgamation.className = 'input-div'

let theInputBox = document.createElement('input')
let theDisplayElement = document.createElement('p')
let theButtonElement = document.createElement('button')

document.body.appendChild(theInputAmalgamation)
theInputAmalgamation.appendChild(theInputBox)
theInputAmalgamation.appendChild(document.createElement('br'))
theInputAmalgamation.appendChild(theButtonElement)

document.body.appendChild(theDisplayElement)

theInputBox.placeholder = "Input card rank here"
theButtonElement.innerText = "Give me BlackJack Advice"

theButtonElement.addEventListener('click', giveAdvice)


// Listen on 'theInputBox' for 'Enter' key. 'click' the button if 'Enter' is pressed while in 'theInputBox'.
theInputBox.addEventListener("keydown", function(event) {
  if (event.key == 'Enter') {
    // Cancel the default action, if needed
    event.preventDefault()
    // console.log(event)
    theButtonElement.click()
  }
})


theInputBox.focus()

let totalScore = 0

function giveAdvice() {
    console.log("I'm giving advice!!!!")
    cardRank = theInputBox.value.toUpperCase()
    theInputBox.value = null

    let theCurrentCardValue = getCardValue(cardRank)
    console.log(`Current Card Score: ${theCurrentCardValue}`)

    totalScore += theCurrentCardValue
    console.log(`Total Score: ${totalScore}`)

    theAdvice = advise(totalScore)
    console.log(theAdvice)
    
    if (totalScore >= 21) {
        theDisplayElement.style.fontSize = "xx-large"
        theInputAmalgamation.remove()
        let doPlayAgain = document.createElement('button')
        doPlayAgain.innerText = "Please advise me on another game of BlackJack"
        document.body.appendChild(doPlayAgain)
        doPlayAgain.focus()
        doPlayAgain.addEventListener('click', function (event) {
            location.reload()
        })
    }

    theDisplayElement.innerText = `${totalScore} Points : ${theAdvice}`

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
