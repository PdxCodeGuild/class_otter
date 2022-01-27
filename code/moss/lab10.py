
with open ('family_loc_test.csv', 'r') as file :
    lines = file.read().split('\n')
    
list_lines = []

for line in lines:
     list_lines.append(line.split(','))

key_list = list_lines.pop(0)

contact_list = []

for list in list_lines:
    contact_list.append({key_list[0]:list[0], key_list[1]:list[1],key_list[2]:list[2],key_list[3]:list[3]})

print(contact_list)

def creat(contact_list,key_list):
    
    name = input('What')
    city =
    state =
    country =
    contact_create = {key_list[0]:name,...}
    contact_list.append(contact_create)
    return contact_list

def retrieve(contact_list)

    for loop dictionary
    if return

def update(contact_list)
    retrieve()
    return contact

def delete(contact_list)
