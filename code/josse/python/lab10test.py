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

print(contacts)

#Create a cred repl using a while loop.
#inside while loop 
#create print statement inside cred to show what input was selected. for each selection

def create():

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
