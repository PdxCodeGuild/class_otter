let alph = {
    "a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",
    "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"
}

let text = prompt("please enter lowercase text (a-z) you would like to encrypt. ")

let characters = []
for (char of text) {


    characters.push(alph[char])
}

let new_text = characters.join('')

alert(`This is your encrypted/decrypted text: ${new_text}`)