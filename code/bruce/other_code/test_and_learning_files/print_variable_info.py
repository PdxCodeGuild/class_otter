# *********************** #
#   print_variable_info   #
#                         #
#       Version: 1.0      #
#   Author: Bruce Stull   #
#        2022-01-17       #
# *********************** #

def print_variable_and_description(variable_under_review, description_of_logic = '', print_logic_results = True):
    '''Accepts three arguments: A variable we are examining, a description of the logic we are examining, and a print flag.'''
    __name__ = print_variable_and_description
    string_result = f"{print_variable_and_description.__name__}: {description_of_logic}: {variable_under_review}"
    if print_logic_results:
        print(string_result)