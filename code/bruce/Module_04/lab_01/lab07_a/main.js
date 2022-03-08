// Assignment:
    // https://github.com/PdxCodeGuild/class_otter/blob/bruce/4%20JavaScript/labs/Lab%2001-03%20Pick%203.md

// Resources:
    // https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/07%20ROT13.md

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


// TODO: defaultSchema assigned here for now. Need to implement functionality where user can choose the schema.
// let defaultSchema = 1;
let defaultSchema = 7;
// let defaultSchema = 12;
// let defaultSchema = 13;
// let defaultSchema = 14;
// let defaultSchema = 25;


function encodeALetter(code, schema=defaultSchema, cipherList=cipherListAlpha) {
    if (code == ' ') {
        return ' ';
    }
    translation = cipherListAlpha.indexOf(code.toLowerCase());
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
    resolution = (translation - schema) % 26
    if (resolution < 0) {
        resolution = resolution + 26
    }
    letter = cipherList[resolution]
    return letter    
}


function letsCipherSomething() {
    messageToEncode = prompt("Please enter message to encode:")
    let encodedMessage = '';
    const letterArray = messageToEncode.split("");
    for (let letter of letterArray) {
        encodedLetter = encodeALetter(letter)
        encodedMessage += encodedLetter;
    }
    consoleLogOrAlert('Encode', messageToEncode + ' -> ' + encodedMessage)
}


function letsUncipherSomething() {
    messageToDecode = prompt("Please enter message to decode:")
    let decodedMessage = '';
    const letterArray = messageToDecode.split("");
    for (let letter of letterArray) {
        decodedLetter = decodeALetter(letter)
        decodedMessage += decodedLetter;
    }
    consoleLogOrAlert('Decode', messageToDecode + ' -> ' + decodedMessage)
}