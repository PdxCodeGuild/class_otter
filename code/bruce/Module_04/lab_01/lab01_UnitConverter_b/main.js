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

// Create page header:
let thePageHeader = document.createElement('h1')
thePageHeader.innerText = "Length Converter 2019"
document.body.prepend(thePageHeader)


// Create some DOM objects:
let selectorInputUnits = document.getElementById('selector-input-units')
let selectorOutputUnits = document.getElementById('selector-output-units')

let inputLength = document.getElementById('user-length')
let outputDisplay = document.getElementById('output-display')

let calculateButton = document.getElementById('calculate-and-display')


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
    'fathom',
    'chain',
    'nmi',
    'klick',
    'km',
    'kilometer',
    'mi',
    'mile',
]


// Object with unit abbreviations to calculation units:
const calculationUnits = {
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
    'fathom': 'fathom',
    'chain' : 'chain',
    'nmi'   : 'nmi',
    'nautical mile': 'nmi',
    'klick' : 'klick',
    'km'    : 'km',
    'kilometer': 'km',
    'mi'    : 'mi',
    'mile'  : 'mi',
}


// conversionObject of one kilometer length in various unit measurements:
const conversionObject = {
    'in'    : 39370.08,
    'ft'    : 3280.84,
    'yd'    : 1093.613,
    'm'     : 1000,
    'fathom': 546.806,
    'chain' : 49.709,
    'nmi'   : 1.852,
    'klick' : 1,
    'km'    : 1,
    'mi'    : .6213712
}


for (selectorType of [selectorInputUnits, selectorOutputUnits]) {
    for (let i=0; i < userUnits.length; ++i) {
        let option = document.createElement('option')
        option.innerText = userUnits[i]
        option.value = userUnits[i]
        selectorType.appendChild(option)
    }
}


calculateButton.addEventListener('click', calculateAndDisplay)

function calculateAndDisplay(event) {
    console.log("Calculating and Displaying")

    // Get the 'string' value the user typed into the input box:
    theUserInputLengthString = inputLength.value
    // Convert the 'string' to 'float':
    theUserInputLengthFloat = parseFloat(theUserInputLengthString)
    
    // Get the input units:
    inputUnits = selectorInputUnits.value
    
    // Get the output units:
    outputUnits = selectorOutputUnits.value
    
    // Get the 'calculationUnits' for the 'inputUnits' and 'outputUnits':
    theActualInputUnit = calculationUnits[inputUnits]
    theActualOutputUnit = calculationUnits[outputUnits]
    
    // Convert the input length to output length:
    calculatedOutputLength =
        theUserInputLengthFloat *
        conversionObject[theActualOutputUnit] /
        conversionObject[theActualInputUnit]
    
    console.log("User Input Length: " + theUserInputLengthFloat + " " + inputUnits)
    console.log("Output Length: " + calculatedOutputLength + " " + theActualOutputUnit)
    
    // Display the output length and units:
    let outputPrecision = 4
    outputLengthToDisplay = calculatedOutputLength.toPrecision(outputPrecision)
    
    outputLengthString =
        theUserInputLengthFloat + ' ' +
        inputUnits + ' is ' +
        outputLengthToDisplay + ' ' +
        outputUnits

    let outputElement = document.createElement('p')
    outputElement.innerText = outputLengthString
    // outputDisplay.appendChild(outputElement)
    // Use 'prepend' to display most recent calculation at the top.
    outputDisplay.prepend(outputElement)
}
