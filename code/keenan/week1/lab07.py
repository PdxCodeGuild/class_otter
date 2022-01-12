# Lab 7: ROT Cipher
# Write a program that prompts the user for a string, and encodes 
# it with ROT13. For each character, find the corresponding character,
# add it to an output string. Notice that there are 26 letters in 
# the English language, so encryption is the same as decryption.

# should this dict have been reversed?  This is way harder with a dictionary.  Should have just used a list......
# alphabet = {
#     'a': 0,
#     'b': 1,
#     'c': 2,
#     'd': 3,
#     'e': 4,
#     'f': 5,
#     'g': 6,
#     'h': 7,
#     'i': 8,
#     'j': 9,
#     'k': 10,
#     'l': 11,
#     'm': 12,
#     'n': 13,
#     'o': 14,
#     'p': 15,
#     'q': 16,
#     'r': 17,
#     's': 18,
#     't': 19,
#     'u': 20,
#     'v': 21,
#     'w': 22,
#     'x': 23,
#     'y': 24,
#     'z': 25
#     }

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g ', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encryption_input = input('What text would you like to encrypt? ')
encryption_shift = input('How much would you like to shift the text? ')
encryption_shift = int(encryption_shift)


# we can use enumerate to help us find the index?

# need to add last functionality to loop through the beginning of the list with if index greater than 25, reset to beginning (modulo 25)
# shoudl this be 
list_input = list(encryption_input)

def rot_cipher(list_input):
    encrypted_text = ""
    for i in range(len(list_input)):
        if list_input[i] in alphabet:
            encrypted_place = alphabet.index(list_input[i]) + encryption_shift
            if encrypted_place > 25:
                encrypted_place = encrypted_place % 25 - 1
            encrypted_text += alphabet[encrypted_place]
            i += 1
    print(encrypted_text)   

rot_cipher(list_input)

         

# can use ASCII code like i did in cs50?
