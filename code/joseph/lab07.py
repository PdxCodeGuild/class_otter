# Lab 7 ROT Cipher Version 1
input_user = input("Please enter a string to be encoded: ")
cipher_rot = {
    "a" : "n",
    "b" : "o",
    "c" : "p",
    "d" : "q",
    "e" : "r",
    "f" : "s",
    "g" : "t",
    "h" : "u",
    "i" : "v",
    "j" : "w",
    "k" : "x",
    "l" : "y",
    "m" : "z",
    "n" : "a",
    "o" : "b",
    "p" : "c",
    "q" : "d",
    "r" : "e",
    "s" : "f",
    "t" : "g",
    "u" : "h",
    "v" : "i",
    "w" : "j",
    "x" : "k",
    "y" : "l",
    "z" : "m"
}
list_user = list(input_user)
elist = []
for x in range(len(list_user)):
    ciph = cipher_rot[list_user[x]]
    elist.append(ciph)
enc_cipher = "".join(elist)
print(enc_cipher)