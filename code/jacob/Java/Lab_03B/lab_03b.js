const points = {a: 1, A: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
     9: 9, 10: 10, j: 10, J: 10, q: 10, Q: 10, k: 10, K: 10, none: 0}

let checker = document.getElementById('checker')
let cardAdvice = document.getElementById('advice')
let cards = document.getElementById('cards')

checker.addEventListener('click', function(){
     let card1 = document.getElementById('card1').value
     let card2 = document.getElementById('card1').value
     let card3 = document.getElementById('card1').value

     
     function score(a, b){
     let x = points[a] + points[b]
     return x
     }

     let advice = score(card1, card2) + points[card3]

     if ((points[card1] === 10 && card2 === 'A') || (card1 === 'A' && points[card2] === 10)){
          advice = 21
          cardAdvice.innerText = "Blackjack"
     }

     else if ((points[card1] === 10 && card2 === 'a') || (card1 === 'a' && points[card2] === 10)){
          advice = 21
          cardAdvice.innerText = "Blackjack"
     }
     
     
     else if (advice < 17){
          cardAdvice.innerText ="Hit"
     }
     else if (advice >= 17 && advice < 21){
          cardAdvice.innerText ="Stay"
          
     }
     else if (advice > 21){
          cardAdvice.innerText ="Busted"
     }
     

     
})