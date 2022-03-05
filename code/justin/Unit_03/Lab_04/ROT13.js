
class ROT13 {
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

    constructor() { }

    run() {
        let textToEncrypt = prompt("Enter text to be encrypted: ");
        let rotation = parseInt(prompt("Enter cypher rotation: "));

        let encryptedText = this.encrypt(textToEncrypt, rotation);

        console.log(`${textToEncrypt}: ${encryptedText}`);
        alert(`You entered:\t${textToEncrypt}\nEncrypted:\t${encryptedText}`);
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
                result += text[i];
            }
        }
        return result;
    }

    isAlpha(character) {
        return this.alphabet.includes(character);
    }
}