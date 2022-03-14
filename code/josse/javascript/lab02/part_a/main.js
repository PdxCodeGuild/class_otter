let english = {
    "a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",
    "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"
}

let word = prompt("please enter a word you would like to encrypt. ")

let characters = []
for (char of word) {
    console.log(english[char].push)


    characters.push(english[char])
}

let new_word = characters.join('')

alert(`This is your new word: ${new_word}`)