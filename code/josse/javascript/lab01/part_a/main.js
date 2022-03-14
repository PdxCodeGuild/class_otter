let nums = []


for (let i = 0; i < 6; i++) {
    // console.log(i)

    let number = prompt("please enter a number or done: ")
    if (number === "done") {
        console.log("done")
        break
    }

    nums.push(number)
}



let thesum = 0
parseInt(thesum)
for (let number of nums) {
    thesum += parseInt(number)
    console.log(thesum)
}

let total = nums.length

let average = thesum / total

console.log(average)

alert(`The average of your number is ${average}`)