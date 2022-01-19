# Lab 10: Contact List
# 01/14/2022

# Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.

# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n')
#     print(lines)
# Once you've processed the file, your list of contacts will look something like this...

# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# ]
# Note: There is a csv library in Python that will do much of this for you. It is what you would use normally in a project, but for this lab you need to write all the logic yourself.



# Version 1: 

# opens the file without needing to be closed
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

# this splits the dictionary at the first comma to save the key values
dict_keys = lines[0].split(',')
contacts = []

# print(dict_keys)

# for each comma, this splits the list, and then zips it together to form a new dictionary with the dict_keys.  needs the -1 modifier because of how split works
for i in range(1, len(lines) - 1):
    data = lines[i].split(',')
    contact = dict(zip(dict_keys, data))
    contacts.append(contact)

print(contacts)


# Version 2:
# Implement a CRUD REPL
# Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
# Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
# Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


# function to add a new contact to the list of contacts
def create_record(contacts):
    name = input("What is the name? ")
    food = input("What is their favorite food? ")
    color = input("What is their favorite color? ")
    new_contact = {"name": name, "favorite food": food, "favorite color": color}
    contacts.append(new_contact)
    return contacts
# create_record(contacts)
# print(contacts)


# function to retrieve data for a name
def retrieve_record(contacts):
    retrieve = input("What is the contact's name? ")
    for contact in contacts:
        if contact['name'] == retrieve:
            return contact

# print(retrieve_record(contacts))



# function to update a record
## this currently has not functionality to check if the update field is not a correct category.
def update_record(contacts):
    who_to_update = retrieve_record(contacts)
    what_to_update = input("What would you like to update? ")
    new_data = input("What would you like to change it to? ")
    who_to_update[what_to_update] = new_data
    return contacts
# update_record(contacts)
# print(contacts)

# function to delete a record
def delete_record(contacts):
    who_to_delete = input("Who is the contact to delete? ")
    for i in range(len(contacts)):
        if contacts[i]['name'] == who_to_delete:
            del contacts[i]
            return contacts
# delete_records(contacts)
# print(contacts)


# Version 3: When REPL loop finishes, write the updated contact info to the CSV file to be saved. 
# I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.

def update_csv(contacts):
    repl_ask = input("What would you like to do to the csv? (create, retrieve, update, or delete a record? ")
    if repl_ask == 'create':
        create_record(contacts)
        return contacts
    if repl_ask == 'retrieve':
        print(retrieve_record(contacts))
        return contacts
    if repl_ask == 'update':
        update_record(contacts)
        return contacts
    if repl_ask == 'delete':
        delete_record(contacts)
        return contacts
    
update_csv(contacts)

# update the new contacts_test.csv file with the changes
with open('contacts_test.csv', 'w') as update_file:
     update_file.write(str(contacts))