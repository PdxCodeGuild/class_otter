# ********************************************** #
#              Lab 10: Contact List              #
#   Friends, Languages, Drinking, csv, I/O, IO   #
#                  Version: 1.0                  #
#              Author: Bruce Stull               #
#                   2022-01-13                   #
# ********************************************** #

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/labs/10%20Contact%20List.md

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

def main():
    whole_text, lines = open_file_return_contents()
    contacts = create_list_of_friends_info_from_lines(lines)
    
    # Maybe print the contacts list?
    print()
    print(contacts)
    print()
    for dict in contacts:
        print(dict)
    print()

main()