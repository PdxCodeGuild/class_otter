let nlist = []

let lab = true
let total = 0

while (lab) {
    let choice = prompt("Enter a number, or 'done'");
    if (choice == 'done') {
        lab = false;
    } else {
        nlist.push(parseInt(choice));
    }
}

nlist.forEach(function(number) {
    total += number
});

alert(`number list: [${nlist}] \n & the average number: ${total/nlist.length}`)