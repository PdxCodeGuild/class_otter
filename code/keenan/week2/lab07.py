# Lab 7: ROT Cipher
# 01/12/2022

# Write a program that prompts the user for a string, and encodes 
# it with ROT13. For each character, find the corresponding character,
# add it to an output string. Notice that there are 26 letters in 
# the English language, so encryption is the same as decryption.

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
