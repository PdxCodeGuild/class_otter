// Resources:
    // DOM Manipulation:
        // https://github.com/PdxCodeGuild/class_otter/blob/bruce/4%20JavaScript/docs/11%20-%20DOM%20Manipulation.md
    // Events:
        // https://github.com/PdxCodeGuild/class_otter/blob/bruce/4%20JavaScript/docs/12%20-%20Events.md

// Types of events:
// load	        an element is loaded
// focus	    an element gains focus
// blur	        element loses focus
// input	    the user inputs a value
// change	    an input's value is changed
// keydown	    any key is pressed
// keyup	    any key is released
// keypress	    any button except Shift, Fn, CapsLock is pressed (fires continuously)
// click	    the mouse has been pressed and released
// mousedown    the mouse has been pressed
// mouseup	    the mouse has been released
// mouseenter   the mouse has entered the element
// mouseleave   the mouse has exited the element
// mousemove    the mouse has moved on the element

// '#select-units' selects 'id' of 'select-units'.
// let selectUnits = document.querySelector('#select-units')

// Run server:
// python -m http.server


console.log("Starting main.js")

let selectorInputUnits = document.getElementById('selector-input-units')
let selectorOutputUnits = document.getElementById('selector-output-units')
console.log(selectorInputUnits)
console.log(selectorOutputUnits)

let selectors = document.getElementsByTagName('select')
// console.log(selectors)

let inputLength = document.getElementById('user-length')
let outputLength = document.getElementById('output-length')
console.log(inputLength)
console.log(outputLength)

let inputBoxes = document.getElementsByTagName('input')
// console.log(inputBoxes)

let calculateButton = document.getElementById('calculate-and-display')
console.log(calculateButton)

// Array of units displayed for user:
let userUnits = [
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


// Object with unit abbreviations to calculation units:
const calcluationUnits = {
    'in'    : 'in',
    'inch'  : 'in',
    '"'     : 'in',
    'ft'    : 'ft',
    'feet'  : 'ft',
    "'"     : 'ft',
    'yd'    : 'yd',
    'yard'  : 'yd',
    'm'     : 'm',
    'meter' : 'm',
    'km'    : 'km',
    'kilometer': 'km',
    'mi'    : 'mi',
    'mile'  : 'mi'
}


// Table of one kilometer length in various unit measurements:
const conversionTable = {
    'in': 39370.08,
    'ft': 3280.84,
    'yd': 1093.613,
    'm' : 1000,
    'km': 1,
    'mi': .6213712
}


for (selectorType of [selectorInputUnits, selectorOutputUnits]) {
    for (let i=0; i < userUnits.length; ++i) {
        let option = document.createElement('option')
        option.innerText = userUnits[i]
        option.value = userUnits[i]
        selectorType.appendChild(option)
    }
}


selectorInputUnits.addEventListener('input', inputUnitsActivity)

function inputUnitsActivity() {
    console.log("User has selected Input Units:", selectorInputUnits.value)
}

calculateButton.addEventListener('click', calculateAndDisplay)

function calculateAndDisplay(event) {
    console.log("Calculating and Displaying")
    // console.log(event)
    // console.log(event.x, event.y)
    // alert(event.x + ' : ' + event.y)

    // Get the value the user typed into the input box:
    theUserInputLengthString = inputLength.value
    // console.log(typeof theUserInputLengthString)
    theUserInputLengthFloat = parseFloat(theUserInputLengthString)
    // console.log(typeof theUserInputLengthFloat)

    console.log(theUserInputLengthFloat)
    
}





userLength = parseFloat(prompt("Please enter length:"));

theActualInputUnit = calcluationUnits[inputUnit];

theActualOutputUnit = calcluationUnits[outputUnit];

outputLength = userLength * conversionTable[theActualOutputUnit] / conversionTable[theActualInputUnit];