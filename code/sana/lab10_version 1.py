with open('pcontacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)
# print(len(lines))
# print(lines[0])
tcount = int(len(lines))
# print(tcount)
tcount = tcount - 1
contacts = []
for line in range(0, tcount):
    data = lines[line].split(',')
    newdic = {'name': '', 'favorite fruit' : '', 'favorite color' : ''}
    newdic['name'] = data[0]
    newdic['favorite fruit'] = data[1]
    newdic['favorite color'] = data[2]
    contacts.append(newdic)
    # print(newdic)
    # newdic = {'name': '', 'favorite fruit' : '', 'favorite color' : ''}
    # print(lines[line])
    # print(data)
print(contacts)
