# *********************** #
#   Copy Pad 2022-01-15   #
#                         #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-15       #
# *********************** #

# Can use a 'global' variable if desired.
do_print_the_logic = True

# Making a print_and_return_value_of_logic() function to be used to pass a variable value through and print the result to console.
# User will need to hard-code the 'description_of_logic' since there is no trivial way to get the 'name' of a variable from a result value.
def print_and_return_value_of_logic(pass_through_variable, description_of_logic = '', print_logic_results = True):
    '''Accepts three arguments. First argument is the variable needing analysis. Second argument is a string description of the  logic being analyzed. Third argument is a print flag.
    Use of function with pass-through:
        Insert 'result, _ = print_and_return_value_of_logic(result, "<description of logic>")', where 'result' is variable under analysis, into code immediately after some logic needing verification.
    Use of function with print only:
        Insert 'print_and_return_value_of_logic(result, "<description of logic>")', where 'result' is variable under analysis, into code immediately after some logic needing verification.
    pass_through_variable is included right now for future expansion. Maybe 'do' something with the actual value other than printing it.'''
    __name__ = print_and_return_value_of_logic
    string_result = f"{print_and_return_value_of_logic.__name__}: {description_of_logic}: {pass_through_variable}"
    if print_logic_results == True:
        print(string_result)
    if description_of_logic == '':
        return pass_through_variable
    return pass_through_variable, string_result

def test_print_and_return_value_of_logic():
    result = 6
    assert print_and_return_value_of_logic(result) == result
    result = str(8)
    assert print_and_return_value_of_logic(result) == result
    result = {'a':1,'b':2}
    assert print_and_return_value_of_logic(result) == result
    assert print_and_return_value_of_logic(2*3) == 6
    assert print_and_return_value_of_logic(2*3, "2*3") == (6,"print_and_return_value_of_logic: 2*3: 6")
    assert print_and_return_value_of_logic(2*9, "2*9") == (18,"print_and_return_value_of_logic: 2*9: 18")
    assert print_and_return_value_of_logic(2*9, "2*9", True) == (18,"print_and_return_value_of_logic: 2*9: 18")
    assert print_and_return_value_of_logic(2*9, "2*9", False) == (18,"print_and_return_value_of_logic: 2*9: 18")

def print_variable_name_and_logic(variable_under_review, description_of_logic = '', print_logic_results = True):
    '''Accepts three arguments: A variable we are examining, a description of the logic of the variable we are examining, and a print flag.'''
    __name__ = print_variable_name_and_logic
    string_result = f"{print_variable_name_and_logic.__name__}: {description_of_logic}: {variable_under_review}"
    print(string_result if print_logic_results else '')

def times_two(num = 0):
    '''Accepts one argument. Returns 2 * num.'''
    print_variable_name_and_logic(num, 'Displaying the value of argument "num"', do_print_the_logic)
    result = 2 * num
    print_variable_name_and_logic(result, "Displaying result after multiplication", do_print_the_logic)
    return result

def test_times_two():
    assert times_two() == 0
    assert times_two('a') == 'aa'
    assert times_two(3) == 6
    assert times_two(9) == 18

def main():
    # number = 3.5
    # output = times_two(number)
    # # print_and_return_value_of_logic(output,"Result of 'ouput'", do_print_the_logic)
    # print_variable_name_and_logic(output,"Result of 'ouput'", do_print_the_logic)
    # # print(f"The result: {output}")

    # print(print_and_return_value_of_logic.__name__)
    # print(print.__name__)
    
    # Experiment with error handling.
    the_integer = 1
    the_list_of_integer = [1]
    the_list_of_string = ['1']
    the_list_of_dictionary = [{'a':1}]

    the_list = [the_integer, the_list_of_integer, the_list_of_string, the_list_of_dictionary]

    for element in the_list:
        result = times_two(element)
        print(result)

main()