# *********************** #
#   Copy Pad 2022-01-16   #
#                         #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-16       #
# *********************** #

do_print_the_logic = False

def print_variable_and_description(variable_under_review, description_of_logic = '', print_logic_results = True):
    '''Accepts three arguments: A variable we are examining, a description of the logic we are examining, and a print flag.'''
    __name__ = print_variable_and_description
    string_result = f"{print_variable_and_description.__name__}: {description_of_logic}: {variable_under_review}"
    if print_logic_results:
        print(string_result)

# Resources:
# https://runestone.academy/ns/books/published//fopp/Sequences/IndexOperatorWorkingwiththeCharactersofaString.html

def dollars_to_thousands(number):
    '''Accepts an integer value. Returns an numeric string value with the ',' separating thousands.'''
    input_as_string = str(number)
    print_variable_and_description(input_as_string, "input_as_string", do_print_the_logic)
    reversed_input_as_string = input_as_string[::-1]
    print_variable_and_description(reversed_input_as_string,"Reversed input_as_string", do_print_the_logic)

    print_variable_and_description(len(reversed_input_as_string),"Length of string", do_print_the_logic)

    working_string = ''
    number_commas = 0   # 0
    print_variable_and_description(working_string,"working_string", do_print_the_logic)
    print_variable_and_description(number_commas,"number_commas", do_print_the_logic)
    index = 0
    while index < len(reversed_input_as_string):
        working_string += reversed_input_as_string[index]
        print_variable_and_description(index,"index", do_print_the_logic)
        print_variable_and_description(working_string,"working_string", do_print_the_logic)
        index += 1
        if index % 3 == 0:
            working_string += ','
            number_commas += 1
    
    working_string = working_string.rstrip(',')
    print_variable_and_description(working_string,"Reversed", do_print_the_logic)
    working_string = working_string[::-1]
    print_variable_and_description(working_string,"Forward", do_print_the_logic)
    return working_string

def main():
    the_input = 'abcdefghijk'
    # the_input = 1000000
    print(the_input)
    print(dollars_to_thousands(the_input))

    # num = 10000000
    # print_variable_and_description(f"{num:,}","Number in thousands")
    # print(f"{num:,}")



    


main()