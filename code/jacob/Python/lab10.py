"""
Lab 10: Contact List
Versions 1, 2 and 3
"""
with open('contacts.csv', 'r') as file:
    contents = file.read().split('\n')


keys = contents[0].split(',')
contacts = []

for i in range(1, len(contents)):
    info = contents[i].split(',')
    contact = dict(zip(keys, info))
    contacts.append(contact)
    

def create_record(contacts, keys, new):

    for i in range(len(new)):
        info = new[i].split(',')
        contact = dict(zip(keys, info))
        contacts.append(contact)
    return contacts

def retrieve_record(contacts, name):

    for i in contacts:
        if i['name'] == name:
            print(f"Their favorite fruit is: {i['favorite fruit']} and color is: {i['favorite color']}")

def update_record(contacts, name, info, new):

    for i in contacts:
        if i['name'] == name:
            i[info] = new
            #contacts.append(i[2])
    return contacts

def delete_record(contacts, name):

    for i in contacts:
        if i['name'] == name:
            contacts.remove(i)
    return contacts

def save_record(contacts, keys):

    line = [','.join(keys)]
    
    for contact in contacts:
        info = ','.join(contact.values())
        line.append(info)
    
    new_contacts = '\n'.join(line)
    
    with open('contacts.csv', 'w') as file:
        file.write(new_contacts)

check = ''

while check != 'Done':
    print()
    print(f'What would you like to do? ')
    check = input('Please choose from: Create, Retrieve, Update, Delete or Done to end. ')
    
    if check == 'Create':
        new = []
        new.append(str(input("What is the new contact information with syntax 'name,favorite fruit,favorite color': ")))
        create_record(contacts, keys, new)

    elif check == 'Retrieve':
        name = input('What is the contact\'s name: ')
        retrieve_record(contacts, name)

    elif check == 'Update':
        name = input('What is the contact\'s name: ')
        info_to_change = input('What info needs to change? Choices are "favorite fruit" or "favorite color" ')
        new_info = input(f'New info for {name}: ')
        update_record(contacts, name, info_to_change, new_info)

    elif check == 'Delete':
        name = input('What contact needs to be deleted? Enter the contact name: ')
        delete_record(contacts, name)

    print()
    
save_record(contacts, keys)