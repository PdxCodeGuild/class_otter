# Full Stack Bootcamp - Unit 01 Lab 07
# Justin Hammond, 01/06/2022


'''
Write a program that prompts the user for a string, and encodes it with ROT13. For each character,
find the corresponding character, add it to an output string. Notice that there are 26 letters in
the English language, so encryption is the same as decryption.

Version 2
Allow the user to input the amount of rotation used in the encryption / decryption.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_ROT(text, rotation=13):
    result = ''
    for character in text.lower():
        if character.isalpha():
            index = ord(character) - 97
            result += alphabet[(index + rotation) % 26]
        else:
            result += character
    return result

def test_encrypt_ROT13():
    assert encrypt_ROT("HelloWorld") == 'uryybjbeyq'
    assert encrypt_ROT("HelloWorld", 7) == 'olssvdvysk'
    assert encrypt_ROT("HelloWorld", 20) == 'byffiqilfx'


def main():
    text_to_encrypt = input("Enter text to be encrypted: ")
    rotation = int(input("Enter cypher rotation: "))

    encrypted_text = encrypt_ROT(text_to_encrypt, rotation)

    print(f"{text_to_encrypt}: {encrypted_text}")


main()
