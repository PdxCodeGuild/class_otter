
with open ('family_loc_test.csv', 'r') as file :
    lines = file.read().split('\n')
    
list_lines = []

for line in lines:
     list_lines.append(line.split(','))

key_list = list_lines.pop(0)

contact_list = []

for listing in list_lines:
    contact_list.append({key_list[0]:listing[0], key_list[1]:listing[1],key_list[2]:listing[2],key_list[3]:listing[3]})

# print(lines)
# print(key_list)
# print(list_lines)
# print(contact_list)

def create(contact_list,key_list):

    add_contact = {}
    
    for i, key in enumerate(key_list):
        add_contact[key] = input(f"What is your contact's {key_list[i]}? ")
    contact_list.append(add_contact)
    return add_contact

# print(create(contact_list,key_list))

def read(contact_list,key_list):

    key_string = '\n' + '\n'.join(key_list) + '\n'
    key_input = input(f"\nWhat would like to search by? Choose from: {key_string} ")
    contact_input = input("\nWhat is your search term? ")
    
    for contact in contact_list:
        if contact[key_input] == contact_input:
            return contact
            
# print(read(contact_list,key_list))

def update(contact_list,key_list):
    
    contact_output = read(contact_list,key_list)
    key_string = '\n' + '\n'.join(key_list) + '\n'
    update_key = input(f"\nWhat category would you like to update? {key_string} ")
    update_value = input(f"\nWhat do you want to change {update_key} to? ")
    
    contact_output[update_key] = update_value
    return contact_output

# print(update(contact_list,key_list))

def delete(contact_list,key_list):

    contact_delete = read(contact_list,key_list)
    delete_yxn = input(f"\nDo you want to delete this contact, (y) or (n)?")
    if delete_yxn == 'y':
        contact_list.remove(contact_delete)
        return contact_list
    else:
        print('\nNo deletions were made')

#print(delete(contact_list,key_list)

while True:
    usr_input = input('\nWelcome, accessing family location list. Type "c" to create, "r" to read, "u" to update, "d" to delete or "q" to exit: ')

    if usr_input == 'q':
        print('Goodbye')
        break 
    elif usr_input == 'c':
        print(create(contact_list,key_list))
    elif usr_input == 'r':
        print(read(contact_list,key_list))
    elif usr_input == 'u':
        print(update(contact_list,key_list))
    elif usr_input == 'd':
        print(delete(contact_list,key_list))

csv_output = []
csv_output.append(key_list)

for contact in contact_list:
    csv_output.append(list(contact.values()))

csv_output = [",".join(line) for line in csv_output]
csv_output = "\n".join(csv_output)

with open('family_loc_test.csv', 'w') as file:
    file.write(csv_output)
