function ticket(a=1, b=99){
    let pick = []

    for (let i=0; i<6; i++){
        pick.push(Math.floor(a + Math.random()*(b)))
    }
    return pick
}


const payouts = {0: 0, 1: 4, 2: 7, 3: 100, 4: 50000, 5: 1000000, 6: 25000000}

const tickets = document.getElementById('tickets')
const results = document.getElementById('results')

tickets.addEventListener('click', function(){
    
    let winTic = ticket()
    let cost = 0
    let payout = 0
    let counter =  0

    while(counter<100000){
        const playTic = ticket()
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
    
    let roi = ((payout - cost) / cost)

    results.innerText = (`
        Payouts: ${payout}
        Costs: ${cost}
        Return on Investment: ${roi}
        Winning Ticket: ${winTic}
    `)
})