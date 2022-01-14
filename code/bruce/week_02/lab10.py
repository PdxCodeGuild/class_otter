# ********************************************** #
#              Lab 10: Contact List              #
#   Friends, Languages, Drinking, csv, I/O, IO   #
#                  Version: 2.0                  #
#              Author: Bruce Stull               #
#                   2022-01-14                   #
# ********************************************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/labs/10%20Contact%20List.md

from os import name


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

def extract_headers_from_lines(lines = []):
    '''Accepts a list of strings. Returns a list of the comma separated values of the first element in the list.'''
    # How to extract the first element of lines list?
    # Can use pop(0)
    if len(lines) != 0:
        the_header_line_string = lines[0]
        headers = the_header_line_string.split(',')
        return headers
    else:
        return []

def test_extract_headers_from_lines():
    assert extract_headers_from_lines() == []
    assert extract_headers_from_lines(['a,b']) == ['a','b']
    assert extract_headers_from_lines(['a,b,c']) == ['a','b','c']
    assert extract_headers_from_lines(['a,b','']) == ['a','b']
    assert extract_headers_from_lines(['a,b,c','']) == ['a','b','c']

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

def create_list_of_friends_info_from_lines(lines = []):
    '''Looks at each line in lines after the header and add it to a list.'''
    friends_list = []
    headers_list = extract_headers_from_lines(lines)
    for i in range(1, len(lines)):
        friend_list = extract_person_info_from_a_line(lines[i])
        friend_dictionary = create_individual_dictionary(headers_list, friend_list)
        friends_list = add_individual_dictionary_to_friends_list(friend_dictionary, friends_list)
    return friends_list

def test_create_list_of_friends_info_from_lines():
    assert create_list_of_friends_info_from_lines() == []
    assert create_list_of_friends_info_from_lines(['h1,h2,h3','p1,l1,d1']) == [{'h1':'p1','h2':'l1','h3':'d1'}]
    assert create_list_of_friends_info_from_lines(['h1,h2,h3','p1,l1,d1','p2,l2,d2']) == [{'h1':'p1','h2':'l1','h3':'d1'},{'h1':'p2','h2':'l2','h3':'d2'}]

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

def create_record(friends_list = [], headers_list = [], name = '', favorite_programming_language = '', favorite_beverage = ''):
    '''Add information (friend,favorite programming language,favorite beverage) to 'friends_list' (a list of dictionaries).'''
    '''Reminder: This function only adds the friend to the contacts (friends_list). It does not write out the list to a file.'''
    friend = create_individual_dictionary(headers_list, [name, favorite_programming_language, favorite_beverage])
    friends_list = add_individual_dictionary_to_friends_list(friend, friends_list)
    print(f"Add:{name}")
    return friends_list

def test_create_record():
    assert create_record() == []
    assert create_record([], ['h1','h2','h3'],'jimboe','jython','jersey juice') == [{'h1':'jimboe','h2':'jython','h3':'jersey juice'}]
    assert create_record([{'h1':'karl','h2':'kornshell','h3':'kemby juice'}], ['h1','h2','h3'],'jimboe','jython','jersey juice') == [{'h1':'karl','h2':'kornshell','h3':'kemby juice'},{'h1':'jimboe','h2':'jython','h3':'jersey juice'}]

# TODO: Add a field for reason for retrieve_record(). Update? Delete? Get the info?
def retrieve_record(friends_list = [{}], friend_name = '', header = 'name'):
    '''Gets the information for a given friend name, if it exists. Returns the index of the record and the record itself (i, dictionary).'''
    # Sometimes 'friends_list' and 'contacts' are used interchangeably. I think I'm using 'friends_list' in funtion definition and 'contacts' in function call (in main()).
    # We want to look at the friends_list and return the specific info for given freind.
    # friends_list is a list of dictionaries. Find the list item where the the value of the first key is 'friend_name'.
    for i, dictionary in enumerate(friends_list):
        print(f"Retrieve: i:{i} Dictionary:{dictionary}")
        if dictionary.get(header) == friend_name:
            print(f"Return: i:{i} Dictionary:{dictionary}")
            return i, dictionary
        # if friend_name == '':
        #     return i, {}
        # if dictionary == {}:
        #     return i, {}
        # else:
        #     return i, {}

# # TODO:  Fix testing. retrieve_record() seems to work functionally, but I'm not able to do effective testing yet.
# def test_retrieve_record():
#     i, friend = retrieve_record([{'n':'george','pl':'g-code','fb':'ginger ale'}],'chad')
#     assert i == 0 and friend == {}
#     assert retrieve_record() == (0,{})
#     assert retrieve_record([{}]) == (0, {})
#     assert retrieve_record([{}],'chad') == (0, {})
#     assert retrieve_record([{'n':'george','pl':'g-code','fb':'ginger ale'}],'chad') == (0, {})
#     assert retrieve_record([{'n':'alphi','pl':'a++','fb':'ale'},{'n':'george','pl':'g-code','fb':'ginger ale'}],'george','n') == (0,{'n':'george','pl':'g-code','fb':'ginger ale'})

def list_of_names(friends_list = [{}]):
    '''Accepts friends_list. Returns the name in each of the deicitonaries.'''
    just_the_names = []
    for dictionary in friends_list:
        just_the_names.append(dictionary.get('name'))
    return just_the_names

def test_list_of_names():
    assert list_of_names([{'name':'sappy'}]) == ['sappy']
    assert list_of_names([{'name':'constance', 'fpl': 'coldfusion'},{'name':'edgerton','fpl':'escher'}]) == ['constance','edgerton']

def update_record_return_friends_list(friends_list = [{}], name = '', new_name = '', new_favorite_programming_language = '', new_favorite_beverage = ''):
    '''Modifies the information in specific dictionary for given name.'''
    # Record should be a dictionary. It may be an empty dictionary, though.
    i, record = retrieve_record(friends_list, name)
    # We now have a record (dictionary), How do we update any of the entries?
    # NOTE: We have access to the headers, since we have the dictionary. The dictionary keys ARE the headers from the CSV.
    headers = record.keys() # dict_keys(['name', 'favorite programming language', 'favorite beverage'])
    # But we don't even need to think about headers. We want to edit an entry (name, language, and/or beverage) of the record.
    if new_name != '':
        print(f"Update Name: {record.get('name')} to {new_name}")
        record.update({'name':new_name})
    if new_favorite_programming_language != '':
        print(f"Update Programming Language: {record.get('favorite programming language')} to {new_favorite_programming_language}")
        record.update({'favorite programming language':new_favorite_programming_language})
    if new_favorite_beverage != '':
        print(f"Update Beverage:  {record.get('favorite beverage')} to {new_favorite_beverage}")
        record.update({'favorite beverage':new_favorite_beverage})
    # Add the changed record back to the friends_list, or replace it,
    # or delete first and replace? REPLACE IT! This is a list so we can replace the element of the list.
    friends_list[i] = record
    return friends_list

def test_update_record_return_friends_list():
    assert True

def delete_record_return_friends_list(friends_list = [{}], name = ''):
    '''Deletes a record. Returns the modified friends_list.'''
    # print(f"Delete: List Length:{len(friends_list)} Name:{name}")
    i, record = retrieve_record(friends_list, name)
    # print(f"Delete: i:{i} Record:{record}")
    if name == '':
        # print(f"Delete: i:{i} Name:{name}")
        return friends_list
    else:
        print(f"Delete: i:{i} Name:{name}")
        # print(f"Length:{len(friends_list)}")
        friends_list.pop(i)
        # print(f"Length:{len(friends_list)}")
        return friends_list


def main():
    whole_text, lines = open_file_return_contents()
    headers = extract_headers_from_lines(lines)
    contacts = create_list_of_friends_info_from_lines(lines)

    print(f"Names: {list_of_names(contacts)}")

    
    # Maybe print the contacts list?
    print()
    for dict in contacts:
        print(dict)
    print()

    # Add friend to list. Create a record.
    # Should we get the headers from 'lines' or from 'contacts'?
    # Or, maybe get the headers from create_list_of_friends_info_from_lines()?
    # Well, actually, we only need to get the headers once, when we start the program.
    # So we can use extract_headers_from_lines(lines) at beginning of main method.
    contacts = create_record(contacts, headers, 'rando', 'racket', 'rum')
    contacts = create_record(contacts, headers, 'tiquediggler', 'tacpol', 'tang')

    print()
    for dict in contacts:
        print(dict)
    print()

    # Update a record in the list.
    update_record_return_friends_list(contacts, 'earl', new_name = 'edgar', new_favorite_programming_language = 'esterel', new_favorite_beverage = 'easy ethanol')

    print()
    for dict in contacts:
        print(dict)
    print()
    # i, record = retrieve_record(contacts, friend_name = 'rando', header = 'name')
    # print(record)
    # print(i)
    contacts = delete_record_return_friends_list(contacts, name = 'falstaff')
    print()
    for dict in contacts:
        print(dict)
    print()

    print(f"Names: {list_of_names(contacts)}")

main()