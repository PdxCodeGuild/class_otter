# Print out each of the following. How does the code change?

# X
# X X
# X X X
# X X X X

#       X
#     X X
#   X X X
# X X X X


# X X X X
# X X X
# X X 
# X


# ####################################
# # Thinking process:
# ####################################
# # Go ahead and create the actual expressions for each part.
# print('X')
# print('XX')
# print('XXX')
# print('XXXX')

# # There are ways we can automate that process.
# # But, first, let's use strings to create the objects we insert into the print().
# line_1 = 'X'
# line_2 = 'XX'
# line_3 = 'XXX'
# line_4 = 'XXXX'

# print(line_1)
# print(line_2)
# print(line_3)
# print(line_4)

# Specify number of rows.
number_of_rows = 5

def print_lower_left_n(number_of_rows = 0):
    '''Accepts an integer parameter. Prints out diagonaly filled rows to console, returns list of the strings printed on each row.'''
    result_string = ""
    result_list = []
    for i in range(number_of_rows):
        result_string += "X" + '  '
        result_list.append(result_string)
        # There exists an extra ' ' at end of string. How to remove?
        # Use slice?
        # print(f"'{result_string[:-2]}'")
        print(f"'{result_string[:-2]}'")  # [:-2] cuts off the last character since [-1] is the last character.
    # result_list = [result_list[i][:-2] for i in range(len(result_list))]
    # Remove the last two ' ' from each element so result string has no hidden space characters.
    result_list = [element[:-2] for element in result_list]
    return result_list

def test_print_lower_left_n():
    assert print_lower_left_n(1) == ['X']
    assert print_lower_left_n(3) == ['X', 'X  X', 'X  X  X']
    assert print_lower_left_n(6) == ['X', 'X  X', 'X  X  X', 'X  X  X  X', 'X  X  X  X  X', 'X  X  X  X  X  X']

def print_lower_right_n(number_of_rows = 1):
    # For each row n: print N - n ' ', then print n 'X'.
    result_string = ""
    result_list = []
    for n in range(number_of_rows):
        result_string = (number_of_rows - n + 1) * '   ' + (n + 1) * '  X'
        # TODO: Figure out why we need this magic number of '8' to print as desired.
        result_list.append(result_string[8:])
        # print((number_of_rows - n) * '  ' + n * ' X')
        # TODO: Figure out why we need this magic number of '8' to print as desired.
        print(f"'{result_string[8:]}'")
    return result_list

def test_print_lower_right_n():
    assert print_lower_right_n(1) == ['X']
    assert print_lower_right_n(2) == ['   X', 'X  X']
    assert print_lower_right_n(3) == ['      X', '   X  X', 'X  X  X']
    assert print_lower_right_n(4) == ['         X', '      X  X', '   X  X  X', 'X  X  X  X']
    assert print_lower_right_n(5) == ['            X', '         X  X', '      X  X  X', '   X  X  X  X', 'X  X  X  X  X']
    assert print_lower_right_n(6) == ['               X', '            X  X', '         X  X  X', '      X  X  X  X', '   X  X  X  X  X', 'X  X  X  X  X  X']


# TODO: Add print_upper_right().
def main():
    # print_lower_left_n(4)
    # # Included '' to show that the final string no longer has the extra '  ' at the end of each element.
    # # 'X'
    # # 'X  X'
    # # 'X  X  X'
    # # 'X  X  X  X'

    lower_right_n = print_lower_right_n(4)
    # print(lower_right_n)
    # '         X'
    # '      X  X'
    # '   X  X  X'
    # 'X  X  X  X'

    # for element in lower_right_n:
    #     print(element)
    # #          X
    # #       X  X
    # #    X  X  X
    # # X  X  X  X
    pass



main()