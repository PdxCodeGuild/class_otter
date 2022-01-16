# *********************** #
#   Copy Pad 2022-01-15   #
#                         #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-15       #
# *********************** #

# Can use a 'global' variable if desired.
print_logic = True

# Making a print_and_return_value_of_logic() function to be used to pass a variable value through and print the result to console.
# User will need to hard-code the 'description_of_logic' since there is no trivial way to get the 'name' of a variable from a result value.
def print_and_return_value_of_logic(pass_through_variable, description_of_logic = '', print_logic_results = True):
    '''Accepts three arguments. First argument is the variable needing analysis. Second argument is a string description of the  logic being analyzed. Third argument is a print flag.
    Use of function: Insert 'result, _ = print_and_return_value_of_logic(result, "<description of logic>")', where 'result' is variable under analysis, into code immediately after some logic needing verification.'''
    __name__ = print_and_return_value_of_logic
    # Will remove next line after commit. Keeping line now to remember the history.
    # string_function_name = 'print_and_return_value_of_logic()'
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

def times_two(num = 0):
    '''Accepts one argument. Returns 2 * num.'''
    print_and_return_value_of_logic(num, 'Displaying the value of argument "num"', print_logic)
    result = 2 * num
    result, _ = print_and_return_value_of_logic(result, "Displaying result after multiplication", print_logic)
    return result

def test_times_two():
    assert times_two() == 0
    assert times_two('a') == 'aa'
    assert times_two(3) == 6
    assert times_two(9) == 18

def main():
    number = 3.5
    output = times_two(number)
    # print(f"The result: {output}")

    # print(print_and_return_value_of_logic.__name__)
    # print(print.__name__)

main()