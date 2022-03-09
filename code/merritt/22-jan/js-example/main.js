let button = document.getElementById('btn')
let buttons = document.getElementsByTagName('button')
let hello = document.getElementById('hello')
let dontPress = document.getElementById('btn2')

let num1 = document.getElementById('num1')
let num2 = document.getElementById('num2')
let nums = document.getElementsByClassName('num')
let getNums = document.getElementById("get-nums")
let results = document.getElementById("results")

console.log(button)
console.log(buttons)

console.log(num1)
console.log(num2)
console.log(nums)
console.log(getNums)
console.log(results)

// button.addEventListener('click', function(e) {
//     alert('Hello World!')
//     console.log(e.x, e.y)
// })

// function superCoolCallback(e) {
//     alert("Hello World (but cool this time)!")
//     console.log(e.x, e.y)
// }

// button.addEventListener('click', superCoolCallback)

button.addEventListener('click', function(e) {
    hello.innerText = "Hello World"
    console.log(e)
})

// getNums.addEventListener('click', function() {
//     let number1 = parseFloat(num1.value)
//     let number2 = parseFloat(num2.value)
//     let numResult = number1 + number2
//     results.innerText = numResult
// })

getNums.addEventListener('click', function() {
    numResult = 0
    for (let i = 0; i < nums.length; i++) {
        numResult += parseFloat(nums[i].value)
    }
    results.innerText += numResult
})

for (let i = 0; i < nums.length; i++) {
    nums[i].addEventListener('input', function() {
        console.log(nums[i].value)
    })
}

dontPress.addEventListener('click', function() {
    let myButton = document.createElement('button')
    myButton.innerText = "I said don't click!"
    myButton.addEventListener('click', function() {
        alert("I told you not to click me.")
    })
    
    document.body.appendChild(myButton)
    dontPress.remove()
})