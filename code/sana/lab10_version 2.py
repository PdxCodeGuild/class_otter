istart = 'y'
contacts = [{'name': 'Jim', 'favorite fruit': 'apples', 'favorite color': 'blue'}, {'name': 'Bob', 'favorite fruit': 'oranges', 'favorite color': 'red'}, {'name': 'John', 'favorite fruit': 'pears', 'favorite color': 'black'}, {'name': 'Bill', 'favorite fruit': 'grapes', 'favorite color': 'white'}, {'name': 'Will', 'favorite fruit': 'berries', 'favorite color': 'green'}, {'name': 'Joe', 'favorite fruit': 'banana', 'favorite color': 'purple'}, {'name': 'Louis', 'favorite fruit': 'grapefruit', 'favorite color': 'pink'}]
testcontacts = []
print(contacts)
while istart == 'y':
    istart = input('open CRUD REPL: press y to continue: ')
    if istart == 'y':
        start = ''
        newdata = []
        addlist = []
        start = input('press c to create a new record\npress r to retrieve a record\npress u to update a record\npress d to delete a record\nPress key to implement action: ')
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
            # if contacts.get(f"{retname}") == None:
            #     print("name not found")
            #     continue
            rindex = contacts.index(f"{retname}")
            print()
            print(f"favorite fruit: {contacts[rindex]['favorite fruit']}")
            print(f"favorite color: {contacts[rindex]['favorite color']}")
            print()
        elif start == 'u':
            upname = input('enter name: ')
            # if contacts.get(f"{upname}") == None:
            #     print("name not found")
            #     continue
            uindex = contacts.index(f"{upname}")
            upfruit = input('update fav fruit: ')
            upcolor = input('update fav color: ')
            print(contacts[uindex])
            print(contacts[uindex]['favorite fruit'])
            print(contacts[uindex]['favorite color'])
            contacts[uindex]['favorite fruit'] = f"{upfruit}"
            contacts[uindex]['favorite color'] = f"{upcolor}"
            print(contacts[uindex]['favorite fruit'])
            print(contacts[uindex]['favorite color'])
            print(contacts[uindex])
            print()
            print(contacts)
            print()
        elif start == 'd':
            dname = input('enter name to delete: ')
            # if contacts.get(f"{dname}") == None:
            #     print("name not found")
            #     continue
            dindex = contacts.index(f"{dname}")
            del contacts[dindex]
            print('Deleted Contact')
            print(contacts)
        else:
            continue