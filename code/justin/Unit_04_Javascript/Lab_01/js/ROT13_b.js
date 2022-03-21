
class ROT13 {
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

    constructor() { }

    run() {
        let textToEncrypt = document.getElementById('textToEncrypt').value;
        let rotation = parseInt(document.getElementById('cypherRotation').value);
        let encryptedText = this.encrypt(textToEncrypt, rotation);
        document.getElementById('encryptedText').innerHTML = encryptedText;
    }

    encrypt(text, rotation=13)
    {
        let result = ''
        text = text.toLowerCase();
        for (let index = 0; index < text.length; index++) {
            if (this.isAlpha(text[index])) {
                let cypherIndex = text.charCodeAt(index) - 97;
                result += this.alphabet[(cypherIndex + rotation) % this.alphabet.length];
            }
            else {
                result += text[index];
            }
        }
        return result;
    }

    isAlpha(character) {
        return this.alphabet.includes(character);
    }
}