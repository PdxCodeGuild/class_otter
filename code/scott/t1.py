def updateDict(dictionary):
    choice = int(input("do you want to (1) add/update an item to the dictionary or (2) remove an item: (1 or 2):  "))
    if choice in [1,2]:
        if choice == 1:
            dictionary[input("key: ")] = input("value: ")
        else:
            dictionary.pop(input("key: "))
    else:
        print("invalid choice")
dictionary = [{'name': 'sam', 'favorite_fruit': 'plum', 'favorite_color': 'red'}, {'name': 'sally', 'favorite_fruit': 'grape', 'favorite_color': 'yellow'}]
print(updateDict(dictionary))