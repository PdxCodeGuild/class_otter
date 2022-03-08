

let addCardButton = document.querySelector('#add-card')
let cardInput = document.querySelector('#drop-down')
let adviseButton = document.querySelector('#get-advice')
let advice = document.querySelector('#advice')
let cardList = []
addCardButton.addEventListener('click', function(){
    let choice = cardInput.value
    cardList.push(choice)
    console.log(cardList)

})

adviseButton.addEventListener('click', function(){
    function sum(numbers){
        total_sum = 0
        for (x of numbers){
            total_sum += parseInt(x) /*parseInt required so 0x isn't seen as hexidecimal and throw an error*/
        }
        return total_sum
    }

    let result = sum(cardList)
    console.log(result)


if (result === 21){
    advice.innerText ='Blackjack!'
}
else if (result >= 17 && result < 21){
    advice.innerText = 'Stay'
}
else if (result < 17){
    advice.innerText ='Hit'
}
else if (result >21){
    advice.innerText ='You Have Busted'
}
})