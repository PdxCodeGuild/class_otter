with open('test.csv') as file:
    book = file.read().split('\n')
    book[0].split(',')
    catagories = book[0].split(',')
    list_of_contacts = []

    for i in range(1, len(book)):
        data = book[i].split(',')
        catagory = dict(zip(catagories, data))
        list_of_contacts.append(catagory)



# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.


def create_new_contact():
    name, fruit, color = input('enter name, favorite fruit and favorite color for new contact seperated by a space. ').split(' ')
    new_contact = {'name': name ,'favorite fruit': fruit,'favorite color': color}
    list_of_contacts.append(new_contact)
    print(new_contact)




# # Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information

def retrieve_contact():
    retrieve_name = input('enter a name to retrieve contact info. ')
    for i in range(len(list_of_contacts)):
        if retrieve_name in list_of_contacts[i]['name']:
            return print(f'your contact: {list_of_contacts[i]}')
        elif retrieve_name not in list_of_contacts[i]['name']:
            pass
    print('not here')



# # Update a record: ask the user for the contact's name, 
# # then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.



def update_contact():
    name = input('enter the name of the contact you would like to update. ')
    atribute = input('name, favorite fruit, or favorite color? ')
    name_selected = 0
    for i in range(len(list_of_contacts)):
        if name in list_of_contacts[i]['name']:
            name_selected = list_of_contacts[i]
            print(name_selected)
            
    if atribute == 'favorite color':
        print(name_selected['favorite color'])
        color = input('new color? ')
        name_selected['favorite color'] = color
        print(name_selected)
    
    elif atribute == 'name':
        print(name_selected['name'])
        new_name = input('new name? ')
        name_selected['name'] = new_name
        print(name_selected)
    
    elif atribute == 'favorite fruit':
        print(name_selected['favorite fruit'])
        fruit = input('new fruit? ')
        name_selected['favorite fruit'] = fruit
        print(name_selected)



# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


def remove_contact():
    name = input('who would you like to remove from contacts? enter name. ')
    for i in range(len(list_of_contacts)):
        if name in list_of_contacts[i]['name']:
            name_selected = list_of_contacts[i]
    print()
    list_of_contacts.remove(name_selected)
    print(list_of_contacts)
# got this loop from merrit then inputed the functions i made.
while True:
    user_input = input("(c)reate, (r)read, (u)pdate, (d)elete, (q)uit?")
    if user_input == 'q':
        break
    elif user_input == 'c':
        create_new_contact()
    elif user_input == 'r':
        retrieve_contact()
    elif user_input == 'u':
        update_contact()
    elif user_input == 'd':
        remove_contact()

# gotta get the list of dictionaries into a list of lists

dic_to_list_of_list = [[key for key in list_of_contacts[0].keys()], *[list(idx.values()) for idx in list_of_contacts]] 

# then combined the lists of lists into one list.

new_list = [','.join(i) for i in dic_to_list_of_list]

# sepperating the list

new_list = '\n'.join(new_list)

# adding it to the csv file

with open('test.csv', 'w') as file:
    file.write(new_list)

# for some reason i can open it in sheets or excel and see what ive added but when i open the csv in VS code i cant see them.