# ********************************************** #
#              Lab 10: Contact List              #
#   Friends, Languages, Drinking, csv, I/O, IO   #
#                  Version: 1.0                  #
#              Author: Bruce Stull               #
#                   2022-01-13                   #
# ********************************************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/labs/10%20Contact%20List.md

###########################################################
# STEP 01
###########################################################
# Use 'with open...' to see what kind of data we are receiving from the file.
def open_file_return_contents(file = r'.\data\friends.csv', mode = 'r'):
    '''Accepts arguments of filename of csv file and file opening mode. Returns whole_text and lines (list).'''
    '''We don't necessarily need the whole text in one file, but I'm returning it in case it's needed.'''
    with open(file, mode) as file:
        whole_text_of_file = file.read()
        list_of_lines = whole_text_of_file.split('\n')
    return whole_text_of_file, list_of_lines

def test_open_file_return_contents():
    text, lines = open_file_return_contents(r'.\data\empty_file.txt')
    assert text == ''
    assert lines == ['']

    text, lines = open_file_return_contents(r'.\data\headers_only.csv')
    assert text == 'header_1,header_2,header_3'
    assert lines == ['header_1,header_2,header_3']

    text, lines = open_file_return_contents(r'.\data\headers_and_one_line.csv')
    assert text == 'header_a,header_b,header_c\nvalue_a,value_b,value_c'
    assert lines == ['header_a,header_b,header_c','value_a,value_b,value_c']
###########################################################


# ###########################################################
# whole_text, lines = open_file_return_contents()

# print(f'''whole_text:\nType: {type(whole_text)}\nContents:\n{whole_text}''')
# # whole_text:
# # Type: <class 'str'>
# # Contents:
# # friend,favorite programming language,favorite beverage
# # earl,perl,monster
# # broseph,risk,juicy juice
# # cornelius,ruby,mineral water
# # sonny,regex,power ade

# print(f'''lines:\nType: {type(lines)}\nContents:\n{lines}''')
# # It seems we are getting a list of strings.
# # Each string element has three comma-separated values in it.
# # The first string element is the headers.
# # The following strings, after the first, are the entries for each line (friend).
# # lines:
# # Type: <class 'list'>
# # Contents:
# # ['friend,favorite programming language,favorite beverage', 'earl,perl,monster', 'broseph,risk,juicy juice', 'cornelius,ruby,mineral water', 'sonny,regex,power ade']
# ###########################################################


###########################################################
# STEP 02
###########################################################
# Decide how we are going to split up the returned list into the required dictionaries.
# NOTE! Let's make a function to read the file and return the lines before continuing:
    # DONE: Go back up to STEP 01 and create function there: open_file_return_contents()

# We have a list of strings.
# The first string is the headers.
# Following strings are lines.
# Make a function to extract the first element of the list, these will become 'keys' for the dictionaries.
def extract_headers_from_lines(lines = []):
    '''Accepts a list of strings. Returns a list of the comma separated values of the first element in the list.'''
    # How to extract the first element of lines list?
    if len(lines) != 0:
        the_header_line_string = lines[0]
        headers = the_header_line_string.split(',')
        return headers
    else:
        return []

def test_extract_headers_from_lines():
    assert extract_headers_from_lines() == []
    # DONE: lines = ['a,b'] --- Why is lines[0] == 'a'? <<<=== That used to happen, I swear!!! It works now!! Why??? What happened?
    assert extract_headers_from_lines(['a,b']) == ['a','b']
    assert extract_headers_from_lines(['a,b,c']) == ['a','b','c']
    assert extract_headers_from_lines(['a,b','']) == ['a','b']
    assert extract_headers_from_lines(['a,b,c','']) == ['a','b','c']
###########################################################


###########################################################
# STEP 03
###########################################################
# We now have the headers. It's a list of strings.
# Create a function to accept a list of strings. This function will assign these list items as keys of the dictionary.
# Do we even need to do this? We have the list of headers. We can use this list in a function to extract the data line values to the keys.
# Create a function which accepts the list of headers and a list of the rest of the data from the file. So we should create a function which...

# 1. Take header list and use as keys. SO, header list will be one function argument.
# 2. Take a record element of the list and assign it's values to an individual record using these keys.
# 3. We will be appending each individual record (dictionary) to a list.
    # So, maybe we need the function to accept a list (header list) and another list (the line list).
def create_individual_dictionary(headers_list = [], friend_list = []):
    '''Accepts header list and a friend_list. Returns a dictionary item. Empty arguments return empty dictionary.'''
    '''The returned dictionary will be added to a list of contacts.'''
    individual_dictionary = {}
    if len(headers_list) == 0 or len(friend_list) == 0:
        individual_dictionary = {}
    else:
        for i in range(len(headers_list)):
            individual_dictionary[headers_list[i]] = friend_list[i]
    return individual_dictionary

def test_create_individual_dictionary():
    assert create_individual_dictionary() == {}
    assert create_individual_dictionary(['a','b','c'],['1','2','3']) == {'a':'1','b':'2','c':'3'}
    assert create_individual_dictionary(['r','b'],['c','r']) == {'r':'c','b':'r'}
###########################################################


###########################################################
# STEP 06
###########################################################
# Need a function to look at an element of 'lines' and extract the person list from that string.
# NOTE: TODO: This is, sorta(?), duplicating the function of extract_headers_from_lines(), so I need to refactor sometime. Well, maybe not.
def extract_person_info_from_a_line(line_string = ''):
    '''Extracts a person info list from one from a single line of lines. Empty argument returns empty list.'''
    if len(line_string) != 0:
        friend_list = line_string.split(',')
        return friend_list
    else:
        return []

def test_extract_person_info_from_a_line():
    assert extract_person_info_from_a_line() == []
    assert extract_person_info_from_a_line('a,b,c') == ['a','b','c']
    assert extract_person_info_from_a_line('r,g,b,y') == ['r','g','b','y']
    assert extract_person_info_from_a_line('1,2') == ['1','2']
###########################################################


###########################################################
# STEP 07
###########################################################
# Do we need a separate function to loop through the elements of lines?
# Well... Let's try it out.
# Write a function to loop through the 1 - len() elements of the lines list and "do something" with that element.
def create_list_of_friends_info_from_lines(lines = []):
    '''Looks at each line in lines after the header and add it to a list.'''
    friends_list = []
    headers_list = extract_headers_from_lines(lines)
    for i in range(1, len(lines)):
        # What are we doing to each line?
        friend_list = extract_person_info_from_a_line(lines[i])
        # We have a person list now. What now?
        # Create the dictionary for that person?
        # Need headers_list.
        friend_dictionary = create_individual_dictionary(headers_list, friend_list)
        # Add the friend_dictionary to the persons_list?
        friends_list = add_individual_dictionary_to_friends_list(friend_dictionary, friends_list)
    return friends_list

def test_create_list_of_friends_info_from_lines():
    assert create_list_of_friends_info_from_lines() == []
    assert create_list_of_friends_info_from_lines(['h1,h2,h3','p1,l1,d1']) == [{'h1':'p1','h2':'l1','h3':'d1'}]
    assert create_list_of_friends_info_from_lines(['h1,h2,h3','p1,l1,d1','p2,l2,d2']) == [{'h1':'p1','h2':'l1','h3':'d1'},{'h1':'p2','h2':'l2','h3':'d2'}]

###########################################################


###########################################################
# STEP 04
###########################################################
# Create function to add individual dictionary to friends list
def add_individual_dictionary_to_friends_list(friend_dictionary = {}, friends_list = []):
    '''Accept a friend dictionary and a friends list, adds the friend dictionary to the friends list.
    Returns the friends list. Empty friend_dictionary returns existing friends_list.'''
    if len(friend_dictionary) == 0:
        return friends_list
    else:
        friends_list.append(friend_dictionary)
        return friends_list

def test_add_individual_dictionary_to_friends_list():
    assert add_individual_dictionary_to_friends_list() == []
    assert add_individual_dictionary_to_friends_list({},[]) == []
    assert add_individual_dictionary_to_friends_list({},[{}]) == [{}]
    assert add_individual_dictionary_to_friends_list({},[{'v':'j'}]) == [{'v':'j'}]
    assert add_individual_dictionary_to_friends_list({'c':'d'},[{'a':'b'}]) == [{'a':'b'},{'c':'d'}]
    assert add_individual_dictionary_to_friends_list({'c':'d','r':'j'},[{'a':'b','1':'2'}]) == [{'a':'b','1':'2'},{'c':'d','r':'j'}]
###########################################################


def main():
    ###########################################################
    # STEP 05
    ###########################################################
    # I think all we need to do now, for first verion, is to run the functions to create the friends list.
    # It seems our goal is to return the final friends list.
    
    # Retrieve the info from the csv file. We are getting the full text, even though we aren't processing it. That's okay. We may need that info in some future expansion.
    whole_text, lines = open_file_return_contents()

    ### TEST ###
    # lines = ['friend,favorite programming language,favorite beverage', 'earl,perl,monster', 'broseph,risk,juicy juice', 'cornelius,ruby,mineral water', 'sonny,regex,power ade']
    ############

    # Get the headers.
    headers = extract_headers_from_lines(lines)

    # OOPS! We still need to get the person strings from the contents list and extract the person list.
    # See STEP 06
    ###########################################################


    ###########################################################
    # STEP 08
    ###########################################################
    # Continue doing all the things.
    contacts = create_list_of_friends_info_from_lines(lines)
    
    # Maybe print the contacts list?
    print()
    print(contacts)
    print()
    for dict in contacts:
        print(dict)
    print()
    ###########################################################

main()