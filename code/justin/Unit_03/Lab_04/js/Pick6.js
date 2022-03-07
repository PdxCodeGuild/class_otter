
class Pick6 {
    prize_tiers = [4, 7, 100, 50000, 1000000, 25000000];

    constructor() { }

    run() {
        let winning_numbers = this.select_numbers();
        console.log(winning_numbers);
        let expenses = 0;
        let earnings = 0;

        for (let i = 0; i < 100000; i++) {
            let ticket = this.select_numbers();
            expenses += 2;
            let match_count = this.get_number_of_matches(ticket, winning_numbers);
            earnings += this.get_prize(match_count);
        }

        alert(`Winnings: ${earnings - expenses}\nROI: ${(earnings - expenses) / expenses}`)
    }

    select_numbers() {
        let result = [];

        for (let index = 0; index < 6; index++) {
            result.push(Math.floor(Math.random() * 100));
        }

        return result;
    }

    get_number_of_matches(ticket, winning_numbers) {
        let match_count = 0;
        for (let index = 0; index < ticket.length; index++) {
            if (ticket[index] == winning_numbers[index]) {
                match_count += 1;
            }
        }
        return match_count;
    }

    get_prize(match_count) {
        if (match_count > 0 && match_count < 7) {
            return this.prize_tiers[match_count + 1];
        }
        else {
            return 0;
        }
    }
}