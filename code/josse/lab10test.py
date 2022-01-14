with open('example.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

new_list = []

for row in lines:
    new_list.append(row.split(","))

key_list = new_list.pop(0)

value_list = new_list


def convert_to_dict(a):
    dict_key = {}
    for keys in dict(key_list):
        dict_key[key_list]
        return dict_key


print(convert_to_dict(key_list))
# name = input("enter your name: ")
# fav_color = input("enter your favorite color: ")
# fav_fruit = input("enter your favorite fruit: ")

# if "'name,favorite fruit,favorite color'" in lines:
#     print(True)
# elif "'name,favorite fruit,favorite color'" != lines:
#     print(False)


# def convert():

# f = open('example.csv')
# contents = f.read()
# # print(contents)
