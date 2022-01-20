# Lab09.py Compute Automated Readability Index - 22-01-12
#import re
#with open(fname , 'r', encoding='utf-8') as f:
# with open(fname , 'r') as f:
#     # fname = "gettysburg.txt"

    # print(num_lines)
    # print(num_words)
    # print(num_chars)
    
#    contents = f.read()
#    number_of_characters = len(contents)
#    number_of_words = contents.split()
# #  numbers_of_sentences = re.split('[.!?]', contents)
# #    number_of_sentences = len(contents.split('[\n]'))
# #    number_of_sentences = re.findall(r' . ', f.read())
#     sentence_split = re.split('[.?!]', contents)
#     print(sentence_split)
#     number_of_sentences = sentence_split.count('.')

# (re.split('[.?!]', contents)) 
    # number_of_lines = contents.readnumber_of_lines()
#   print('\nNumber of words in text file :', len(number_of_words))
    # print('Number of number_of_sentences in tex file:', numb_lines)       
    # contents = f.read()
    # number_of_lines = 0
    # for line in contents:
    #     if line = "\n":
    #         number_of_lines += 1


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