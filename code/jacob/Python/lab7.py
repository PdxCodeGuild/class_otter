"""
Lab 7: ROT Cipher
Version 1 and 2
"""
print()
letters = ''
for i in range(97, 123):
    letters += (chr(i))

rotation = int(input('Enter the amount of rotation?: '))

rot_letters = letters[rotation:] + letters[:rotation]

word = input('Enter a word: ')
new_word = ''

def encrypt(a):
    new_word = ''
    for n in a:
        position = letters.find(n)
        new_word += rot_letters[position]
    
    return new_word

print(letters)
print(rot_letters)

print(encrypt(word))
print()