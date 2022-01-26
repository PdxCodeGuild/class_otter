'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*         Lab 10 - Contact List             *
*            13/January/2022                *
*                                           *
*********************************************
'''


def create_record(headers, contacts):
    name = input('Please enter your first name:')
    fruit = input('please enter your favorite_fruit:')
    color = input('please enter your favorit_color:')
    contacts.append({headers[0]: name, headers[1]: fruit, headers[2]: color})
    return contacts

def get_record(contacts):
    name = input('Please enter the first name of the person whose record you wish to retrieve:')
    for contact in contacts:
        if contact['name'] == name:
            print(contact['name'])
            return contact
   
def updateDict(contacts):
    name = input('Please enter the first name of the person whose record you wish to update:')
    for index, contact in enumerate(contacts):
        if contact['name'] == name:
            key = input("\nenter the key to change: 'name', 'favorite_fruit', 'favorite_color':") 
            value = input("\nPlease enter new  - value:")
            if key == ('name'):
                contacts[index]['name'] = value
                return contacts
            elif key == ('favorite_fruit'):
                contacts[index]['favorite_fruit'] = value
                return contacts
            elif key == ('favorite_color'):
                contacts[index]['favorite_color'] = value
                return contacts
            else:
                print('incorrect key')
                return None
        else:
           continue

def del_record(contacts):
    name = input('Please enter the first name of the person whose record you wish to delete:')
    for index, contact in enumerate(contacts):
        if contact['name'] == name:
            contacts.pop(index)
        else:
            continue
    return contacts

def run():
    with open('contacts.csv', 'r') as file:
        #contacts.csv = file.read()
        lines = file.read().split('\n')
    first_list = []
    for line in lines:
        first_list.append(line.split(','))
    headers = first_list.pop(0) # pop out headers list
    # print('headers = ' + str(headers))
    contacts = []
    for item in first_list:
        contacts.append({headers[0]: item[0], headers[1]: item[1], headers[2]: item[2]})

        
    new_record = create_record(headers, contacts) #add new contact to contacts dict
    print('contacts =' + str(new_record))
    
    retrieved_record = get_record(contacts)
    print('contacts = ' + str(retrieved_record))

    updated_record = updateDict(contacts)
    print('updated contacts = '+ str(updated_record))
    
    delete_record = del_record(contacts)
    print('remaining_contacts ='+ str(delete_record))

    contacts_output = []
    contacts_output.append(headers)
    for contact in contacts:
        contacts_output.append(list(contact.values()))
    print(contacts_output)

    contacts_output = [",".join(line) for line in contacts_output]
    contacts_output = "\n".join(contacts_output)

    with open('contacts.csv', 'w') as f:
        f.write(contacts_output)
        

if __name__ == '__main__':
    run()



    



    
    
