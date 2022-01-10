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

for i in index:
    i += 13
    rot.append(english[i])
print(rot)