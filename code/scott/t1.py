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

# def Convert(a):
#     it = iter(a)
#     res_dct = dict(zip(it, it))
#     return res_dct
         
# # Driver code
# lst = ['a', 1, 'b', 2, 'c', 3]
# print(Convert(lst))

import csv       
    csv_columns = ['name','favorite_fruit','favorite_color']
    # csv_file = "contacts.csv"
    try:
        with open('contacts.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            writer.writerow(contacts)
    except IOError:
        print("I/O error")
        
    write_records = write_csv()
    print(write_records)