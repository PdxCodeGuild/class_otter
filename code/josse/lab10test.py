with open('example.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

new_list = []

for row in lines:
    new_list.append(row.split(","))

key_list = new_list.pop(0)

value_list = new_list

dict_key = {}


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
