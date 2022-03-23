let wordInput = document.getElementById('word-input');
let runBt = document.getElementById('run-bt');
let outputDiv = document.getElementById('output-div');

let english = {
    "a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",
    "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"
}


// console.log(wordInput)
// console.log(outputDiv)
// console.log(runBt)

runBt.addEventListener("click", function () {
    let characters = []
    let textValue = wordInput.value
    console.log(textValue)
    // for loop grabs each character of text value
    for (char of textValue)
        // characters.push adds to empty list/parameter compares to dictionary
        characters.push(english[char])


    outputDiv.innerText = characters.join('')

})