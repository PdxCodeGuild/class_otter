with open('ncontacts.csv', 'r') as file:
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
# print(contacts)
istart = 'y'
while istart == 'y':
    istart = input('open CRUD REPL: press y to continue: ')
    if istart == 'y':
        start = ''
        newdata = []
        addlist = []
        start = input('press c to create a new record\npress r to retrieve a record\npress u to update a record\npress d to delete a record\npress s to save to csv\nPress key to implement action: ')
        if start == 'c':
            newname = input('enter name: ')
            newfruit = input('enter fav fruit: ')
            newcolor = input('enter fav color: ')
            newdata.append(newname)
            newdata.append(newfruit)
            newdata.append(newcolor)
            newdic = {'name': '', 'favorite fruit' : '', 'favorite color' : ''}
            newdic['name'] = newdata[0]
            newdic['favorite fruit'] = newdata[1]
            newdic['favorite color'] = newdata[2]
            addlist.append(newdic)
            contacts.extend(addlist)
            print(contacts)
        elif start == 'r':
            retname = input('enter name: ')
            for x in range(0, len(contacts)):
                if contacts[x]['name'] == retname:
                    rindex = x
                    print(f"favorite fruit: {contacts[rindex]['favorite fruit']}")
                    print(f"favorite color: {contacts[rindex]['favorite color']}")
                    continue
        elif start == 'u':
            upname = input('enter name: ')
            for x in range(0, len(contacts)):
                if contacts[x]['name'] == upname:
                    uindex = x
                    upfruit = input('update fav fruit: ')
                    upcolor = input('update fav color: ')
                    # print(contacts[uindex])
                    # print(contacts[uindex]['favorite fruit'])
                    # print(contacts[uindex]['favorite color'])
                    contacts[uindex]['favorite fruit'] = f"{upfruit}"
                    contacts[uindex]['favorite color'] = f"{upcolor}"
                    # print(contacts[uindex]['favorite fruit'])
                    # print(contacts[uindex]['favorite color'])
                    # print(contacts[uindex])
                    # print()
                    print(contacts)
                    # print()
                    continue
        elif start == 'd':
            dname = input('enter name to delete: ')
            for x in range(0, len(contacts)):
                if contacts[x]['name'] == dname:
                    dindex = x
                    del contacts[dindex]
                    print('Deleted Contact')
                    print(contacts)
        elif start == 's':
            saved = ''
            for x in range(0, len(contacts)):
                saved = saved + f"{contacts[x]['name']}"
                saved = saved + ',\n'
                saved = saved + f"{contacts[x]['favorite fruit']}"
                saved = saved + ',\n'
                saved = saved + f"{contacts[x]['favorite color']}"
                saved = saved + '\n'
            with open('ncontacts.csv', 'a') as file:
                file.write(','.join(saved))
        else:
            break
