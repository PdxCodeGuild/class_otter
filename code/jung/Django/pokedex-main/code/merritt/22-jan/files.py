with open('test.txt', 'r') as f:
    contents = f.read()
contents = contents[::2]
contents += "\nMerritt opened this file!"
with open('test.txt', 'w') as f:
    f.write(contents)