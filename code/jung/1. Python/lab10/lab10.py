# version1

with open('lab10.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)
    

def empty_li(csv):
    empty_list = []
    for line in csv:
        empty_list.append(line.split(","))
    return empty_list



li = empty_li(lines)

# assign 'keys' list
keys = li.pop(0)


# delete the 'keys' list (values)




# dictionary = {keys: values}
def dict(li, keys):
    contacts = []
    for group in li: #[['jung', 'watermelon', 'white'], ['tim', 'peach', 'pink'], ['jane', 'blackberries', 'orange'], ['mia', 'orange', 'black']]
        dictionary = {}
        for i in range(len(keys)):
            dictionary[keys[i]] = group[i]
        contacts.append(dictionary)
    return contacts
    # print(f"contacts = {contacts}")

contacts = dict(li, keys)
# print(f"contacts = {contacts}")


######################################################################################################################################################


# version2

def create_a_record(contacts):
    name = input("Tell me your name: ")
    fruit = input("What's your favorite fruit?: ")
    color = input("What's your favorite color?: ")

    new_contacts = {"name": name, "favorite fruit": fruit, "favorite color": color}
    # new_contacts.extend((name,fruit,color))
    # li.append(new_contacts)
    contacts.append(new_contacts)
    return contacts

# print(create_a_record(contacts))



def retrieve_a_record(contacts):
    ask = input("what is the contact's name?: ")
    # print(contacts)

    for contact in contacts:
        if contact["name"] == ask:
            return contact
    return "There's nothing there"

# print(retrieve_a_record(contacts))



def update_a_record(contacts): 
    retrieved_contact = retrieve_a_record(contacts) # {'name': 'jung', 'favorite fruit': 'watermelon', 'favorite color': 'white'}
    ask2 = input("What do you want to update?: ")
    ask3 = input(f"Update {ask2}: ")
    retrieved_contact[ask2] = ask3
    return contacts



# print(update_a_record(contacts))


def delete_a_record(contacts):
    ask = input("what is the contact's name?: ")
    # print(len(contacts))
    for i in range(len(contacts)):
        if contacts[i]["name"] == ask:
            del contacts[i]
            return contacts
    

# print(delete_a_record(contacts))



# Create, retrieve, update, and delete (ask the user) using While true:
# for contact in contacts:
#     for key in contact:
#         # print(contact[key])
#         new_list.append(key)
#         new_list.append(contact[key])
# print(new_list)

# new_list = new_list.join(li[0])
# print(li)
new_list = []




def joined_li(list):
    empty_list = []
    for line in list:
        empty_list.append(",".join(line))
    return empty_list


# print(joined_list)

def final(joined_list):
    csv = ""
    count = 0
    for items in joined_list:
        count += 1
        # print(count)
        if len(joined_list) == count:
            csv += items
        else:
        # "\n".join(items)
        # print(items)
            csv += items + "\n"
    return csv

# print(final(joined_list))


# for item in li:
#     # print(item)
#     ",".join(item)

# print(li)

# list dics to list of list
# list of list to csv
# join convert

def result(contacts):
    li = []
    for item in contacts:
        val = item.values()
        li.append(val)

    li.insert(0, keys)
    joined_list = joined_li(li)
    return final(joined_list)

# f.re

while True:
    # input (what do you want to do? c,r,u,d,or done)
    ask = input("What do you want to do? create, retrieve, update, delete, or done: ")
    
    # depends on user's preference, create a function
    if ask == "create":
        create_a_record(contacts)
        print(result(contacts))
    elif ask == "retrieve":
        print(retrieve_a_record(contacts))
    elif ask == "update":
        update_a_record(contacts)
        print(result(contacts))
    elif ask == "delete":
        delete_a_record(contacts)
        print(result(contacts))
    elif ask == "done":
        break
    else:
        print("It's not a valid command")
        continue


with open("lab10.csv", "w") as f:
    f.write(result(contacts))