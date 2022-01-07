# Full Stack Bootcamp - Unit 01 Lab 10
# Justin Hammond, 01/07/2022

import os

'''
Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together,
and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV,
convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header
represents the keys, the text in the other lines represent the values.

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
Once you've processed the file, your list of contacts will look something like this...

contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]
Note: There is a csv library in Python that will do much of this for you. It is what you would use normally in a
project, but for this lab you need to write all the logic yourself.


Version 2
Implement a CRUD REPL

Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that
the user entered.

Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their
information

Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and
the value of the attribute they'd like to set.
Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.


Version 3
When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a
backup contacts.csv because you likely won't write it correctly the first time.
'''

def load_lines_from_file(file_name):
    base_path = os.path.dirname(__file__)
    lines = []
    try:
        with open(f'{base_path}\\{file_name}', 'r') as file:
            lines = file.read().split('\n')
    except FileNotFoundError as exception:
        print(f'{exception.strerror}: {exception.filename}')
        lines = None
    finally:
        return lines

def test_load_lines_from_file():
    assert load_lines_from_file('') == None
    assert load_lines_from_file('not_a_file.txt') == None
    assert load_lines_from_file('a_real_file.txt') == ['This is a test file']
    assert load_lines_from_file('multi_line_file.txt') == ['This is a test file', 'Testing for multiple lines of text;', 'in a single file']
    assert load_lines_from_file('empty_file.txt') == ['']

def get_row_cells(csv_line):
    cells = csv_line.split(',')
    for column_index in range(len(cells)):
        cells[column_index] = cells[column_index].strip()

    return cells

def test_get_row_cells():
    sample_lines = load_lines_from_file('sample.csv')

    assert get_row_cells(sample_lines[0]) == ['header a', 'header b', 'header c', 'header d']
    assert get_row_cells(sample_lines[1]) == ['1', '5', '3', '9']
    assert get_row_cells(sample_lines[2]) == ['1', '4', '5', '6']
    assert get_row_cells(sample_lines[3]) == ['4', '5', '2', '0']
    assert get_row_cells(sample_lines[4]) == ['1', '4', '2', '6']
    assert get_row_cells(sample_lines[5]) == ['9', '2', '5', '2']
    assert get_row_cells(sample_lines[6]) == ['2', '7', '4', '9']

def create_entry(headers, row):
    entry = {}
    for index in range(len(headers)):
        entry[headers[index]] = row[index]
    return entry

def test_create_entry():
    sample_lines = load_lines_from_file('sample.csv')
    headers = get_row_cells(sample_lines[0])
    row = get_row_cells(sample_lines[1])
    
    assert create_entry(headers, row) == {f'{headers[0]}': f'{row[0]}', f'{headers[1]}': f'{row[1]}', f'{headers[2]}': f'{row[2]}', f'{headers[3]}': f'{row[3]}'}

    row = get_row_cells(sample_lines[3])
    assert create_entry(headers, row) == {f'{headers[0]}': f'{row[0]}', f'{headers[1]}': f'{row[1]}', f'{headers[2]}': f'{row[2]}', f'{headers[3]}': f'{row[3]}'}

    row = get_row_cells(sample_lines[6])
    assert create_entry(headers, row) == {f'{headers[0]}': f'{row[0]}', f'{headers[1]}': f'{row[1]}', f'{headers[2]}': f'{row[2]}', f'{headers[3]}': f'{row[3]}'}

def process_csv(csv_lines):
    headers = get_row_cells(csv_lines[0])

    entries = []
    for index in range(len(csv_lines)):
        if index == 0:
            continue

        row = get_row_cells(csv_lines[index])
        entries.append(create_entry(headers, row))
    return entries

def test_process_csv():
    sample_lines = load_lines_from_file('sample.csv')
    headers = get_row_cells(sample_lines[0])

    rows = [get_row_cells(sample_lines[1]), get_row_cells(sample_lines[2]), get_row_cells(sample_lines[3]), get_row_cells(sample_lines[4]), get_row_cells(sample_lines[5]), get_row_cells(sample_lines[6])]
    
    assert process_csv(sample_lines) == [
        {f'{headers[0]}': f'{rows[0][0]}', f'{headers[1]}': f'{rows[0][1]}', f'{headers[2]}': f'{rows[0][2]}', f'{headers[3]}': f'{rows[0][3]}'},
        {f'{headers[0]}': f'{rows[1][0]}', f'{headers[1]}': f'{rows[1][1]}', f'{headers[2]}': f'{rows[1][2]}', f'{headers[3]}': f'{rows[1][3]}'},
        {f'{headers[0]}': f'{rows[2][0]}', f'{headers[1]}': f'{rows[2][1]}', f'{headers[2]}': f'{rows[2][2]}', f'{headers[3]}': f'{rows[2][3]}'},
        {f'{headers[0]}': f'{rows[3][0]}', f'{headers[1]}': f'{rows[3][1]}', f'{headers[2]}': f'{rows[3][2]}', f'{headers[3]}': f'{rows[3][3]}'},
        {f'{headers[0]}': f'{rows[4][0]}', f'{headers[1]}': f'{rows[4][1]}', f'{headers[2]}': f'{rows[4][2]}', f'{headers[3]}': f'{rows[4][3]}'},
        {f'{headers[0]}': f'{rows[5][0]}', f'{headers[1]}': f'{rows[5][1]}', f'{headers[2]}': f'{rows[5][2]}', f'{headers[3]}': f'{rows[5][3]}'}
        ]


def main():
    lines = load_lines_from_file('sample_contacts.csv')
    contacts_list = process_csv(lines)

    print(contacts_list)

main()