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
    base_path = os.path.dirname(os.path.abspath(__file__))
    lines = None
    try:
        with open(f'{os.path.join(base_path, file_name)}', 'r') as file:
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
    assert get_row_cells(sample_lines[2]) == ['2', '4', '5', '6']
    assert get_row_cells(sample_lines[3]) == ['3', '5', '2', '0']
    assert get_row_cells(sample_lines[4]) == ['4', '4', '2', '6']
    assert get_row_cells(sample_lines[5]) == ['5', '2', '5', '2']
    assert get_row_cells(sample_lines[6]) == ['6', '7', '4', '9']

def create_entry(headers, row):
    entry = {}
    for index in range(len(headers)):
        entry[headers[index]] = row[index]
    return entry

def test_create_entry():
    sample_lines = load_lines_from_file('sample.csv')
    sample_headers = get_row_cells(sample_lines[0])

    row = get_row_cells(sample_lines[1])
    assert create_entry(sample_headers, row) == {f'{sample_headers[0]}': f'{row[0]}', f'{sample_headers[1]}': f'{row[1]}', f'{sample_headers[2]}': f'{row[2]}', f'{sample_headers[3]}': f'{row[3]}'}

    row = get_row_cells(sample_lines[3])
    assert create_entry(sample_headers, row) == {f'{sample_headers[0]}': f'{row[0]}', f'{sample_headers[1]}': f'{row[1]}', f'{sample_headers[2]}': f'{row[2]}', f'{sample_headers[3]}': f'{row[3]}'}

    row = get_row_cells(sample_lines[6])
    assert create_entry(sample_headers, row) == {f'{sample_headers[0]}': f'{row[0]}', f'{sample_headers[1]}': f'{row[1]}', f'{sample_headers[2]}': f'{row[2]}', f'{sample_headers[3]}': f'{row[3]}'}

def process_csv(csv_lines):
    headers = get_row_cells(csv_lines[0])
    table_id_header = headers[0]

    entries = []
    for index in range(len(csv_lines)):
        if index == 0:
            continue

        row = get_row_cells(csv_lines[index])
        entries.append(create_entry(headers, row))
    return entries, table_id_header

def test_process_csv():
    sample_lines = load_lines_from_file('sample.csv')
    sample_headers = get_row_cells(sample_lines[0])
    rows = [get_row_cells(sample_lines[1]), get_row_cells(sample_lines[2]), get_row_cells(sample_lines[3]), get_row_cells(sample_lines[4]), get_row_cells(sample_lines[5]), get_row_cells(sample_lines[6])]
    
    sample_table, table_id_header = process_csv(sample_lines)
    assert sample_table == [
        {f'{sample_headers[0]}': f'{rows[0][0]}', f'{sample_headers[1]}': f'{rows[0][1]}', f'{sample_headers[2]}': f'{rows[0][2]}', f'{sample_headers[3]}': f'{rows[0][3]}'},
        {f'{sample_headers[0]}': f'{rows[1][0]}', f'{sample_headers[1]}': f'{rows[1][1]}', f'{sample_headers[2]}': f'{rows[1][2]}', f'{sample_headers[3]}': f'{rows[1][3]}'},
        {f'{sample_headers[0]}': f'{rows[2][0]}', f'{sample_headers[1]}': f'{rows[2][1]}', f'{sample_headers[2]}': f'{rows[2][2]}', f'{sample_headers[3]}': f'{rows[2][3]}'},
        {f'{sample_headers[0]}': f'{rows[3][0]}', f'{sample_headers[1]}': f'{rows[3][1]}', f'{sample_headers[2]}': f'{rows[3][2]}', f'{sample_headers[3]}': f'{rows[3][3]}'},
        {f'{sample_headers[0]}': f'{rows[4][0]}', f'{sample_headers[1]}': f'{rows[4][1]}', f'{sample_headers[2]}': f'{rows[4][2]}', f'{sample_headers[3]}': f'{rows[4][3]}'},
        {f'{sample_headers[0]}': f'{rows[5][0]}', f'{sample_headers[1]}': f'{rows[5][1]}', f'{sample_headers[2]}': f'{rows[5][2]}', f'{sample_headers[3]}': f'{rows[5][3]}'}
    ]
    assert table_id_header == 'header a'


def create_record(table, table_id_header, name, favorite_fruit, favorite_color):
    for entry in table:
        if entry[table_id_header] == name:
            return table

    entry = {'name': name, 'favorite fruit': favorite_fruit, 'favorite color': favorite_color}
    table.append(entry)
    return table

def test_create_record():
    sample_contacts, table_id_header = process_csv(load_lines_from_file('sample_contacts.csv'))
    create_record(sample_contacts, table_id_header, 'Kelly', 'Banana', 'Green')

    record_found = False
    for contact in sample_contacts:
        if contact[table_id_header] == 'Kelly':
            record_found = True
    assert record_found

def retrieve_record(table, table_id_header, name):
    for entry in table:
        if entry[table_id_header] == name:
            return entry
    return None

def test_retrieve_record():
    sample_contacts, table_id_header = process_csv(load_lines_from_file('sample_contacts.csv'))
    assert retrieve_record(sample_contacts, table_id_header, 'sam') == {'name': 'sam', 'favorite fruit': 'pineapple', 'favorite color': 'blue'}
    assert retrieve_record(sample_contacts, table_id_header, 'bacon') == None

def update_record(table, table_id_header, name, updates):
    for entry in table:
        if entry[table_id_header] == name:
            for update in updates.items():
                entry[update[0]] = update[1]
            return entry
    return None

def test_update_record():
    sample_contacts, table_id_header = process_csv(load_lines_from_file('sample_contacts.csv'))
    assert update_record(sample_contacts, table_id_header, 'sam', {'favorite color': 'yellow'}) == {'name': 'sam', 'favorite fruit': 'pineapple', 'favorite color': 'yellow'}

def delete_record(table, table_id_header, name):
    record_found = False
    record_to_delete = None
    for entry in table:
        if entry[table_id_header] == name:
            record_found = True
            record_to_delete = entry

    if record_found:
        table.remove(record_to_delete)

    return table

def test_delete_record():
    sample_contacts, table_id_header = process_csv(load_lines_from_file('sample_contacts.csv'))
    delete_record(sample_contacts, table_id_header, 'sam')

    record_found = False
    for contact in sample_contacts:
        if contact[table_id_header] == 'sam':
            record_found = True
    assert not record_found


def clean_command_input(command_string):
    command_string = str(command_string)[0:1].upper()

    if command_string == 'C' or command_string == 'R' or command_string == 'U' or command_string == 'D' or command_string == 'Q' or command_string == 'Y' or command_string == 'N':
        return command_string
    
    return ''

def test_clean_command_input():
    assert clean_command_input('Create') == 'C'
    assert clean_command_input('Retrieve') == 'R'
    assert clean_command_input('N') == 'N'
    assert clean_command_input('c') == 'C'
    assert clean_command_input('y') == 'Y'

    assert clean_command_input('a') == ''
    assert clean_command_input('T') == ''
    assert clean_command_input('5') == ''
    assert clean_command_input(1337) == ''
    assert clean_command_input('$%^&*') == ''

def table_to_csv_string(table):
    csv_string = ''

    for header in table[0].keys():
        csv_string += header + ','
    csv_string = csv_string[:-1]
    
    for row in table:
        csv_string += '\n'
        for _, value in row.items():
            csv_string += value + ','
        csv_string = csv_string[:-1]

    return csv_string

def test_table_to_csv_string():
    sample_lines = load_lines_from_file('sample.csv')
    sample_table, _ = process_csv(sample_lines)

    assert table_to_csv_string(sample_table) == 'header a,header b,header c,header d\n1,5,3,9\n2,4,5,6\n3,5,2,0\n4,4,2,6\n5,2,5,2\n6,7,4,9'

def write_to_db(table, file_name):
    base_path = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(f'{os.path.join(base_path, file_name)}', 'w') as file:
            file.write(table_to_csv_string(table))
    except FileNotFoundError as exception:
        print(f'{exception.strerror}: {exception.filename}')

def test_write_to_db():
    file_name = 'sample.csv'
    sample_table, table_id_header = process_csv(load_lines_from_file(file_name))

    update_record(sample_table, table_id_header, '1', {'header b': '9'})
    write_to_db(sample_table, file_name)
    sample_table, table_id_header = process_csv(load_lines_from_file(file_name))
    record = retrieve_record(sample_table, table_id_header, '1')
    assert record['header b'] == '9'

    update_record(sample_table, table_id_header, '1', {'header b': '5'})
    write_to_db(sample_table, file_name)
    sample_table, table_id_header = process_csv(load_lines_from_file(file_name))
    record = retrieve_record(sample_table, table_id_header, '1')
    assert record['header b'] == '5'


def main():
    file_name = 'sample_contacts.csv'
    lines = load_lines_from_file(file_name)
    contacts_list, table_id_header = process_csv(lines)

    while True:
        command = input("Enter a command ([C]reate, [R]etrieve, [U]pdate, [D]elete, or [Q]uit): ")
        command = clean_command_input(command)

        if command == 'C':
            name = input("\tEnter name: ")
            favorite_fruit = input("\tEnter favorite fruit: ")
            favorite_color = input("\tEnter favorite color: ")
            create_record(contacts_list, table_id_header, name, favorite_fruit, favorite_color)
            continue
        elif command == 'R':
            name = input("\tEnter name: ")
            record = retrieve_record(contacts_list, table_id_header, name)
            if record == None:
                print(f"No contact information for {name}")
            else:
                print(f"\n{record['name']}\t{record['favorite fruit']}\t{record['favorite color']}")
            continue
        elif command == 'U':
            updates = {}
            name = input("\tEnter name: ")
            while True:
                contact_attribute = input("\tEnter attribute: ")
                attribute_value = input("\tEnter value: ")
                updates[contact_attribute] = attribute_value
                keep_updating = clean_command_input(input("\nUpdate another attribute? ([Y]es or [N]o)"))
                if keep_updating == 'Y':
                    continue
                else:
                    break
            update_record(contacts_list, table_id_header, name, updates)
            continue
        elif command == 'D':
            name = input("\tEnter name: ")
            delete_record(contacts_list, table_id_header, name)
            continue
        elif command == 'Q':
            break
    
    write_to_db(contacts_list, file_name)


if __name__ == '__main__':
    main()

'''sample_contacts.csv
name, favorite fruit, favorite color
matthew, blackberries, orange
sam, pineapple, blue
bob, cherry, blue
alice, blueberry, red
jenny, strawberry, pink
frank, apple, red
jason, cherry, red
mike, pear, purple
amber, cherry, pink
jordan, kiwi, green
stephanie, apple, pink
'''