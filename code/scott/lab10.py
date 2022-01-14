

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
first_list = []
for line in lines:
    first_list.append(line.split(','))

headers = first_list.pop(0)
# contact = []
# for item in first_list:
#     contact.append({headers[0]: item[0], headers[1]: item[1], headers[2]: item[2]})
# print (contact) 
print(headers)

# def create_record():

name = input('Please enter your first name:')
fruit = input('please enter your favorite fruit:')
color = input('please enter your favorit color:')
new_contact = ''.join(name + ',' + fruit + ',' + color)

print(new_contact)    

# new_contact = []
# contact_name = []
# for item in contact_name:
#     contact_name.append({headers[0]: item[0], headers[1]: item[1], headers[2]: item[2]})
#print(first_list)
#print({headers[0]: first_list[0][0]})