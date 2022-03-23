from tarfile import RECORDSIZE


with open('example.csv', 'r') as file:
    lines = file.read().split('\n')


def extract_string(input_lines):
    list = []
    for row in input_lines:
        list.append(row.split(","))
    return list


new_list = extract_string(lines)
key_list = new_list.pop(0)


def main_dict(header, values):
    list_of_dicts = []
    for value in values:
        list_of_dicts.append(
            {header[0]: value[0], header[1]: value[1], header[2]: value[2]})
    return list_of_dicts


contacts = main_dict(key_list, new_list)

# print(contacts)


# create a record
def create_friend_dictionary(name, fruit, color):
    '''create friend dictionary from input'''
    friend_dict = {
        "name": name,
        "favorite fruit": fruit,
        "favorite color": color
    }
    return friend_dict


def add_friend_dict_to_list(dict, list):
    '''Combine dictionary of friend to contacts'''
    list.append(dict)
    return list


new_friend = create_friend_dictionary("Bruce", "Mango", "purple")
# print(new_friend)

new_contacts = add_friend_dict_to_list(new_friend, contacts)
# print(new_contacts)


def user_input_dict(contacts_list):
    '''prompt user for name, favorite fruit, favorite color and append to contacts list'''
    name = input("please enter a name: ")
    fruit = input("please enter your favorite fruit: ")
    color = input("please enter your favorite color: ")
    dictionary = create_friend_dictionary(name, fruit, color)
    new_contacts = add_friend_dict_to_list(dictionary, contacts_list)
    return new_contacts


# print(contacts)
# new_contacts = user_input_dict(contacts)
# # print(new_contacts)

# print(contacts[0]['name'])
# print(contacts[0]['favorite fruit'])
# print(contacts[0]['favorite color'])


# print(contacts[1]['name'])
# print(contacts[1]['favorite fruit'])
# print(contacts[1]['favorite color'])

# print(contacts[1]['name'])
# print(contacts[1]['favorite fruit'])
# print(contacts[1]['favorite color'])

# print(contacts[1]['name'])


# retrieve a record

def find_record(list_of_dictionary):
    '''takes user input of name and finds input inside dictionary and returns a dictionary'''
    name = input("please enter a name: ").lower()
    for i in range(len(list_of_dictionary)):
        # print(list_of_dictionary[name]['name'])
        if list_of_dictionary[i]['name'].lower() == name:

            return list_of_dictionary[i]


specific_contact = find_record(new_contacts)
print(specific_contact)


def print_contact_information(dictionary):
   return dictionary.keys()


show_keys = print_contact_information(specific_contact)

print(show_keys)


while True:
    input(f"Would you like to create , read, update, delete? ")
'''Display dictionary information'''
# Get keys for the dictionary
# print out the value for keys
# use f string !!!!!!!!!!!!!!!!
# Create a cred repl using a while loop.
# inside while loop
# create print statement inside cred to show what input was selected. for each selection

# def create():

# ----------------------------------------------------------------------------------------------------

########################################################################################################


# ------------------------------------------------------------------------------------------------------


# name = input("enter your name: ")
# fav_color = input("enter your favorite color: ")
# fav_fruit = input("enter your favorite fruit: ")

# name_outputs = name, fav_fruit, fav_color

# lists_test = []


# def create(answer):
#     added_list = []
#     for user in answer:
#         added_list.append({
#             name_outputs})
#     return added_list


# newer_list = create(contacts)

# newest_list = contacts.append(newer_list)

# print(create(newest_list))

# --------------------------------------------------------------------------
# def create(answer):
#     added_list = []
#     for user in answer:
#         added_list.append(
#             {answer: name[0], answer: fav_color[1], answer: fav_fruit[2]})
#     return added_list


# new_dict = {}
# for i in range(len(header)):
#     new_dict[header[i]]


# def convert(conversion):
#     dict_header = []
#     for string in conversion:
#         dict_header.join(string)
#     return dict_header

# def convert(list_converter):
#      dict_header = {}
#     for dictionary in list_converter:
#         dict_header.append(dictionary.split(" , "))
#     return dict_header


# new_list = []
# for row in lines:
#     new_list.append(row.split(","))

# value_list = new_list

# def convert_to_dict(a):
#     dict_key = {}
#     for keys in dict(key_list):
#         dict_key[key_list]
#         return dict_key


# if "'name,favorite fruit,favorite color'" in lines:
#     print(True)
# elif "'name,favorite fruit,favorite color'" != lines:
#     print(False)

# def convert():

# f = open('example.csv')
# contents = f.read()
# # print(contents)
