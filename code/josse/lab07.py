# english = ["a",	"b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

english = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z",
           "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m"
           }

# rot = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
#        "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]


word = input("please enter your message: ")


for char in word:
    print(english[char])
    # print(char)
