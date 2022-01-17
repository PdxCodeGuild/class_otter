def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
         
# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))

def create_record(headers, contact):
    name = input('Please enter your first name:')
    fruit = input('please enter your favorite fruit:')
    color = input('please enter your favorit color:')
    contact.append({headers[0]: name, headers[1]: fruit, headers[2]: color})
    return contact

def get_record(contacts):
    name = input('Please enter the first name of the person whose record you wish to retrieve:')
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return 'not found'

def update_record(contacts):
    name = input('Please enter the first name of the person whose record you wish to update:')
    for contact in contacts:
        if contact['name'] == name:
        #     return contact
        # print(contact)
    # print('The Name you requested is:' + update_record(contacts))
            key = input("Please enter the attribute; 'name', 'favorite fruit', 'favorite color' you wish to update:")
            value = input("Please enter your 'new value':")
            up_con = (key + ',' + value)
    # for contact in contacts:
            if contact['name'] == key:
                contact.update({up_con})
#                return contact
            elif contact['favorite fruit'] == key:
                contact.update({up_con})
#                return contact
            elif contact['favorite color'] == key:
                contact.update({up_con})
#                return contact
            else:
                return 'Not Found'
    return

with open('f:\class_otter\code\scott\contacts.csv', 'r') as file:
    lines = file.read().split('\n')
#    print(lines)
first_list = []
for line in lines:
    first_list.append(line.split(','))
# print(first_list)

headers = first_list.pop(0) # pop out headers list
contact = []
for item in first_list:
    contact.append({headers[0]: item[0], headers[1]: item[1], headers[2]: item[2]})
# print (contact) 
# print(headers)
contacts = (create_record(headers, contact)) #add new contact to contacts dict
#print(contacts)
#print("The original list is : " + str(contacts))

#print(get_record(contacts))


            
print(update_record(contacts))
            
