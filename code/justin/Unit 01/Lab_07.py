# Full Stack Bootcamp - Unit 01 Lab 07
# Justin Hammond, 01/06/2022


'''
Write a program that prompts the user for a string, and encodes it with ROT13. For each character,
find the corresponding character, add it to an output string. Notice that there are 26 letters in
the English language, so encryption is the same as decryption.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_ROT13(text):
    result = ''
    for character in text.lower():
        if character.isalpha():
            index = ord(character) - 97
            result += alphabet[(index + 13) % 26]
        else:
            result += character
    return result

def test_encrypt_ROT13():
    assert encrypt_ROT13("HelloWorld") == 'uryybjbeyq'


def main():
    text_to_encrypt = input("Enter text to be encrypted: ")
    encrypted_text = encrypt_ROT13(text_to_encrypt)

    print(f"{text_to_encrypt}: {encrypted_text}")


main()
