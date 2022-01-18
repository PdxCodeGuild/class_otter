import os

# with open('test.csv') as file:
#     book = file.read().split('\n')
#     book[0].split(',')
#     catagories = book[0].split(',')
#     list_of_contacts = []

#     for i in range(1, len(book)):
#         data = book[i].split(',')
#         catagory = dict(zip(catagories, data))
#         list_of_contacts.append(catagory)



# # Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
# while True:
#     name, fruit, color = input('Create a new contact. enter name, favorite fruit and favorite color for new contact seperated by a space. ').split(' ')

#     def create_new_contact(name, fruit, color):
#         new_contact = {'name': name ,'favorite fruit': fruit,'favorite color': color}
#         list_of_contacts.append(new_contact)
#         print(new_contact)
#     create_new_contact(name,fruit,color)


#     retrieve_name = input('enter a name to retrieve contact info. ')

# # # Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information

#     def retrieve_contact(key):
#         for i in range(len(list_of_contacts)):
#             if key in list_of_contacts[i]['name']:
#                 return print(f'your contact: {list_of_contacts[i]}')
#             elif key not in list_of_contacts[i]['name']:
#                 pass
#         print('not here')

#     retrieve_contact(retrieve_name)

# # # Update a record: ask the user for the contact's name, 
# # # then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.

#     user_choice = input('enter the name of the contact you would like to update. ')
#     atribute_to_change = input('name, favorite fruit, or favorite color? ')


#     def update_contact(name,atribute):
#         name_selected = 0
#         for i in range(len(list_of_contacts)):
#             if name in list_of_contacts[i]['name']:
#                 name_selected = list_of_contacts[i]
#                 print(name_selected)
            
#         if atribute == 'favorite color':
#             print(name_selected['favorite color'])
#             color = input('new color? ')
#             name_selected['favorite color'] = color
#             print(name_selected)
    
#         elif atribute == 'name':
#             print(name_selected['name'])
#             new_name = input('new name? ')
#             name_selected['name'] = new_name
#             print(name_selected)
    
#         elif atribute == 'favorite fruit':
#             print(name_selected['favorite fruit'])
#             fruit = input('new fruit? ')
#             name_selected['favorite fruit'] = fruit
#             print(name_selected)

#     update_contact(user_choice,atribute_to_change)

# # Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

#     delete_name = input('who would you like to remove from contacts? enter name. ')

#     def remove_contact(name):
#         for i in range(len(list_of_contacts)):
#             if name in list_of_contacts[i]['name']:
#                 name_selected = list_of_contacts[i]
#         print()
#         list_of_contacts.remove(name_selected)
#         print(list_of_contacts)

#     remove_contact(delete_name)

    # with open('test.csv', 'r') as file:
folder_path = 'C:\Users\nickc\class_otter\code\nick\python\lab10contactList\test.csv'
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        file_path = os.path.join(folder_path, file)
    with open(file_path, 'r') as f:
            print(f.read())