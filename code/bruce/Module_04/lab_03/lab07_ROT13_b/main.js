// Assignment:
    // https://github.com/PdxCodeGuild/class_otter/blob/bruce/4%20JavaScript/labs/Lab%2001-03%20Pick%203.md

// Resources:
    // https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/07%20ROT13.md

// Create an array of the letters of the alphabet:
const cipherListAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

// Text elements:
let pageHeader = document.createElement('h1')
let inputElement = document.createElement('input')
let outputElement = document.createElement('p')

// Selector for ROT schema:
let rotSchemaSelector = document.createElement('select')

// A 'label' element for 'inputElement':
let inputElementLabel = document.createElement('label')

// Buttons for control:
let encodeButton = document.createElement('button')
let decodeButton = document.createElement('button')
let copyButton = document.createElement('button')

// Containers for stuff:
let inputElementsDiv = document.createElement('div')
let buttonDiv = document.createElement('div')
let outputElementsDiv = document.createElement('div')

// Create mappings for 'header' and 'main' HTMLElements:
let theHeader = document.querySelector('header')
let theMain = document.querySelector('main')

// Put the 'theHeader' in <header>:
theHeader.appendChild(pageHeader)

// Put the containers in 'theMain':
theMain.appendChild(inputElementsDiv)
theMain.appendChild(buttonDiv)
theMain.appendChild(outputElementsDiv)

// Put text in the 'header':
pageHeader.innerText = "ROT Cipher"

// Put text elements, selector, and buttons in their containers:
inputElementsDiv.appendChild(inputElementLabel)
inputElementsDiv.appendChild(document.createElement('br'))
inputElementsDiv.appendChild(inputElement)
inputElementsDiv.appendChild(rotSchemaSelector)
buttonDiv.appendChild(encodeButton)
buttonDiv.appendChild(decodeButton)
outputElementsDiv.appendChild(outputElement)
outputElementsDiv.appendChild(copyButton)

// Set up buttons:
encodeButton.innerText = "Encode your string"
decodeButton.innerText = "Decode your string"
copyButton.innerText = "Copy encoded message text"

// Set up event listeners on buttons:
encodeButton.addEventListener('click', letsEncodeSomething)
decodeButton.addEventListener('click', letsDecodeSomething)

// Event listener on 'copyButton' has anonymous function to copy text of output element.
copyButton.addEventListener('click', function() {
    var copyText = outputElement
    navigator.clipboard.writeText(copyText.innerText);
    alert("Copied the text: " + copyText.innerText);
})

// Set up the input element:
inputElementLabel.htmlFor = "input-element"
inputElementLabel.innerText = "String to encode"
inputElement.type = "text"
inputElement.placeholder = "Enter your un-encoded message here"
inputElement.id = "input-element"

// Populate the 'rotSchemaSelector' schema selector:
for (let i=0; i < 26; ++i) {
    let option = document.createElement('option')
    option.innerText = i
    option.value = i
    rotSchemaSelector.appendChild(option)
}

// TODO: Use two buttons and one function. Inside function, look at which button was pressed. If button was 'encode', then 'schema=userSchema' if button is 'decode', then 'schema=-userSchema'.
function letsEncodeSomething() {
    let userSchema = parseInt(rotSchemaSelector.value)
    messageToEncode = inputElement.value
    let encodedLetter
    let encodedMessage = ''
    const letterArray = messageToEncode.split("")
    for (let letter of letterArray) {
        encodedLetter = encodeALetter(letter, schema=userSchema)
        encodedMessage += encodedLetter
    }
    outputElement.innerText = encodedMessage
}


function letsDecodeSomething() {
    let userSchema = parseInt(rotSchemaSelector.value)
    messageToDecode = inputElement.value
    let decodedLetter
    let decodedMessage = ''
    const letterArray = messageToDecode.split("")
    for (let letter of letterArray) {
        decodedLetter = encodeALetter(letter, schema=-userSchema)
        // decodedLetter = decodeALetter(letter, schema=userSchema)
        decodedMessage += decodedLetter
    }
    outputElement.innerText = decodedMessage
}


function encodeALetter(code, schema=13, cipherList=cipherListAlpha) {
    if (code == ' ') {
        return ' '
    }
    translation = cipherListAlpha.indexOf(code.toLowerCase())
    resolution = (translation + schema) % 26
    if (resolution > 25) {
        resolution = resolution - 26
    } else if (resolution < 0) {
        resolution = resolution + 26
    } 
    letter = cipherList[resolution]
    return letter
}


// function decodeALetter(code, schema=13, cipherList=cipherListAlpha) {
//     if (code == ' ') {
//         return ' ';
//     }
//     translation = cipherListAlpha.indexOf(code.toLowerCase());
//     resolution = (translation - schema) % 26
//     if (resolution < 0) {
//         resolution = resolution + 26
//     }
//     letter = cipherList[resolution]
//     return letter    
// }

