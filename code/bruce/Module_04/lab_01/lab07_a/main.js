
// Create an array of the letters of the alphabet:
const cipherListAlpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



function consoleLogOrAlert(description, thingToSay) {
    let doAlert = true;

    if (doAlert) {
        window.alert(description + ': ' + thingToSay);
        console.log(description + ': ' + thingToSay);
    } else {
        console.log(description + ': ' + thingToSay);
    }
    return thingToSay;
}


let defaultSchema = 11;


function encodeALetter(code, schema=defaultSchema, cipherList=cipherListAlpha) {
    if (code == ' ') {
        return ' ';
    }
    translation = cipherListAlpha.indexOf(code.toLowerCase());
    // resolution = (translation + schema) % 26

    resolution = (translation + schema) % 26
    if (resolution > 25) {
        resolution = resolution - 26
    }

    letter = cipherList[resolution]
    return letter
}


function decodeALetter(code, schema=defaultSchema, cipherList=cipherListAlpha) {
    if (code == ' ') {
        return ' ';
    }
    translation = cipherListAlpha.indexOf(code.toLowerCase());
    // resolution = (translation - schema) % 26
    resolution = (translation - schema) % 26
    if (resolution < 0) {
        resolution = resolution + 26
    }
    letter = cipherList[resolution]
    return letter    
}


function letsCipherSomething() {
    messageToEncode = prompt("Please enter message to encode:")
    // userSchema = prompt("Please enter cipher rotation:")
    let encodedMessage = '';

    const letterArray = messageToEncode.split("");

    // for (let index in letterArray) {
    //     // consoleLogOrAlert('A letter', letterArray[index])
    //     encodedLetter = encodeALetter(letterArray[index])
    //     // consoleLogOrAlert('Encode', letterArray[index] + ' -> ' + encodedLetter);
    //     encodedMessage += encodedLetter;
    // }
    
    for (let letter of letterArray) {
        // consoleLogOrAlert('A letter', letterArray[index])
        encodedLetter = encodeALetter(letter)
        // consoleLogOrAlert('Encode', letterArray[index] + ' -> ' + encodedLetter);
        encodedMessage += encodedLetter;
    }
    consoleLogOrAlert('Encode', messageToEncode + ' -> ' + encodedMessage)
}

function letsUncipherSomething() {
    messageToDecode = prompt("Please enter message to decode:")
    // userSchema = prompt("Please enter cipher rotation:")
    
    let decodedMessage = '';

    const letterArray = messageToDecode.split("");

    // for (let index in letterArray) {
    //     // consoleLogOrAlert('A letter', letterArray[index])
    //     decodedLetter = decodeALetter(letterArray[index])
    //     // consoleLogOrAlert('Decode', letterArray[index] + ' -> ' + decodedLetter);
    //     decodedMessage += decodedLetter;
    // }
    
    for (let letter of letterArray) {
        // consoleLogOrAlert('A letter', letterArray[index])
        decodedLetter = decodeALetter(letter)
        // consoleLogOrAlert('Decode', letterArray[index] + ' -> ' + decodedLetter);
        decodedMessage += decodedLetter;
    }
    consoleLogOrAlert('Decode', messageToDecode + ' -> ' + decodedMessage)
}