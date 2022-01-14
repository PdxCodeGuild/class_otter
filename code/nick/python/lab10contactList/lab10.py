from os import name
from turtle import onclick


with open('test.csv') as file:
    lines = file.read().split('\n')
    row1 =lines[0].split(',')
    row2 = lines[1].split(',')
    row3 = lines[2].split(',')
    row4 = lines[3].split(',')
    row5 = lines[4].split(',')
    names = [row1[0], row2[0], row3[0], row4[0], row5[0]]
    favorite_fruit = [row1[1], row2[1], row3[1], row4[1], row5[1]]
    favorite_color = [row1[2], row2[2], row3[2], row4[2], row5[2]]
    contacts = [
        {row1[0] :row2[0], row1[1]:row2[1], row1[2]:row2[2]},
        {row1[0] :row3[0], row1[1]:row3[1], row1[2]:row3[2]},
        {row1[0] :row4[0], row1[1]:row4[1], row1[2]:row4[2]},
        {row1[0] :row5[0], row1[1]:row5[1], row1[2]:row5[2]} 
    ]

name, fruit, color = input('enter name, favorite fruit and favorite color for new contact seperated by a comma. ').split(',')


def create(name, fruit, color):
    new_contact = {'name': name ,'favorite fruit': fruit,'favorite color': color}
    contacts.append(new_contact)
    print(new_contact)

create(name,fruit,color)

# Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information

