import string, random

# one_twenty_seven_string = (
#     ''.join([random.choice(string.ascii_letters + string.digits + ' ') for _ in range(127)])
# )

# print(one_twenty_seven_string)
# print(len(one_twenty_seven_string))


# # Function to cut a large text string into pieces 126 character long.

# def cut_127(input_string):
#     string_list = []
#     string_element = ''
#     # Add the first 127 characters, as a string, to the list.
#     # Add the second 127 characters, as a string, to the list.
#     for c in input_string:
#         if len(string_element) < 127:
#             string_element += c
#         string_list.append(string_element)
#     return string_list

# print(cut_127(one_twenty_seven_string))

source_string = """
Buckeye Ipsum Woody Archie Griffin WOSU Oval Mirror Lake Horseshoe Moritz Scarlet Gray Brutus Buckeye Leaf Ohio State The Union Tbdbitl OH-IO Script Ohio Carmen Ohio Hagerty Hall Fisher John Glenn Buckeyes Lee Horvath Michael Redd The Lantern Morrill Hayes St. John's Excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy River Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus Woody Archie Griffin WOSU Oval Mirror Lake Horseshoe Moritz Scarlet Gray Brutus Buckeye Leaf Ohio State The Union Tbdbitl OH-IO Script Ohio Carmen Ohio Hagerty Hall Fisher John Glenn Buckeyes Lee Horvath Michael Redd The Lantern Morrill Hayes St. John's Excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus Orlando Pace 14-0 Olentangy River Les Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus Woody Archie Griffin WOSU Oval Mirror Lake Horseshoe Moritz Scarlet Gray Brutus Buckeye Leaf Ohio State The Union Tbdbitl OH-IO Script Ohio Carmen Ohio Hagerty Hall Fisher John Glenn Buckeyes Lee Horvath Michael Redd The Lantern Morrill Hayes St. John's Excellence Urban Meyer Hoppalong Cassidy Woody Hayes Columbus
"""

print(f"len(source_string): {len(source_string)}")

# def add_character_to_string(the_string, the_character):
#     return the_string + the_character

# def test_add_character_to_string():
#     assert add_character_to_string('a', 'a') == 'aa'
#     assert add_character_to_string('abc', 'f') == 'abcf'

# small_string = 'abcdefghij'

# working_string = ''
# for single_character in small_string:
#     while len(working_string) < 4:
#         print(single_character)
#         working_string += single_character

# print(working_string)

print(len("Wexner Mike Conley Ryan Shazier Eddie George Dr. Michael Drake RPAC Skull Session 1870 Jack Nicklaus Woody Archie Griffin WOSU"))