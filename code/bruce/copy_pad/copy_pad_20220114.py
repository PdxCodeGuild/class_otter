# *********************** #
#   Copy Pad 2022-01-14   #
#                         #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-14       #
# *********************** #

# Make a list of dictionaries. See if we can use index() on it.
# working_string = ('h1,h2,h3\njules,joule,juicy juice\nkarl,kaleidoscope,kiss')
# 'h1,h2,h3\njules,joule,juicy juice\nkarl,kaleidoscope,kiss'

list_of_dictionaries = [{'h1':'jules','h2':'joule','h3':'juicy juice'},{'h1':'karl','h2':'kaleidoscope','h3':'kiss'},{'h1':'lee','h2':'leeds','h3':'leachy'}]

def convert_contacts_to_comma_separated_values(list_of_dictionaries):
    working_string = ''
    for top_row_value in list_of_dictionaries[0].keys():
        working_string += top_row_value + ','
    # Remove the last comma added.
    working_string = working_string[:-1]
    
    for dict in list_of_dictionaries:
        working_string += '\n'
        for i, value in dict.items():
            working_string += value + ','
        # Remove the last comma added.
        working_string = working_string[:-1]
    return working_string

raw_csv = convert_contacts_to_comma_separated_values(list_of_dictionaries)
print(raw_csv)

def write_contents_to_file(file, text, mode = 'w'):
    '''Open 'file' whether it exists or not, overwrite 'text' to 'file', close 'file'.'''
    with open(file, mode) as the_file:
        the_file.write(text)

# file_name_and_path = r".\data\safe_test.csv"
# write_contents_to_file(file_name_and_path, raw_csv, mode = 'w')

