// '#select-fruits' selects the 'id' of 'select-fruits'.
// let selectFruits = document.querySelector('#select-fruits')

let selectFruits = document.getElementById('select-fruits')
let selectUnits = document.getElementById('select-units')

let fruits = ['apples', 'bananas', 'pears']

let userInputUnits = [
    'in',
    'inch',
    '"',
    'ft',
    'feet',
    "'",
    'yd',
    'yard',
    'm',
    'meter',
    'km',
    'kilometer',
    'mi',
    'mile',
]


for (let i=0; i < fruits.length; ++i) {
    let option = document.createElement('option')
    option.innerText = fruits[i]
    option.value = fruits[i]
    selectFruits.appendChild(option)
}

for (let i=0; i < userInputUnits.length; ++i) {
    let option = document.createElement('option')
    option.innerText = userInputUnits[i]
    option.value = userInputUnits[i]
    selectUnits.appendChild(option)
}
