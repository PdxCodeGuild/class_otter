let numberValue = document.getElementById('number-input')
let runBt = document.getElementById('run-bt')
let outputDiv = document.getElementById('output-div')


let nums = []

runBt.addEventListener("click", function () {
    // console.log('you found me')
    let thesum = 0
    // parseInt(thesum)

    let number = numberValue.value
    console.log(number + " this is number from input box")

    nums.push(number)

    console.log(nums + " this is array of all numbers")

    for (let number of nums) {
        thesum += parseInt(number)
        // console.log(thesum)
    }
    let total = nums.length

    let average = thesum / total

    console.log(`this is the average ${average}`)

    outputDiv.innerText = average
})