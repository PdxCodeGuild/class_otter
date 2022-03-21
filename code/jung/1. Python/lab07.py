ask = input("tell me a word: ")
ask2 = input("encryption or decryption?: ")
ask3 = int(input("amount of rotation used in the encryption/decryption: "))
ask_list = [i for i in ask]
# print(ask_list)


#make a list of index contains 0 - 25
index = []
for num in range(0,26):
    index.append(num)
# print(index)

#make a list of english contains a - z
english = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# print(english)

#iterate through the index list and 
rot = []

for letter in ask_list:
    letter_num = english.index(letter)
    if ask2 == "encryption":
        letter_num += ask3
        rot.append(english[letter_num])
    elif ask2 == "decryption":
        letter_num -= ask3
        rot.append(english[letter_num])
print(rot)
    

            