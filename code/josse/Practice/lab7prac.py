alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


word = input("enter your word: ")
number = int(input("rot_amount: "))
temp_string = ""

for char in word:
    index = alphabet.index(char)
    tran_char = alphabet[index + number]
    temp_string += tran_char

print(temp_string)
