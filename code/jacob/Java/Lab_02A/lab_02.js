function ticket(a=1, b=99){
    let pick = []

    for (let i=0; i<6; i++){
        pick.push(Math.floor(a + Math.random()*(b)))
    }
    return pick
}

var winTic = ticket()
var payouts = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}

var cost = 0
var payout = 0
var counter =  0
var payout = 0

while(counter<100000){
    let playTic = ticket()
    let score = 0
    counter += 1
    cost += 2

    for (let i=0; i<6; i++){
        if ( playTic[i] === winTic[i]){
            score += 1
        }
    }

    payout += payouts[score]
}

var roi = ((payout - cost) / cost)

alert(`
        Payouts: ${payout} 
        Costs: ${cost} 
        Return on Investment: ${roi}
        Winning Ticket: ${winTic}
`)
