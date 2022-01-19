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

###################### Example use ######################
the_string = ''
for i in range(4):
    print_variable_and_description(i,"The value of index 'i'",True)
    the_string += str(i)
    print_variable_and_description(the_string,"The value of the_string")
    print_variable_and_description(str(i),"The value of str(i)")
    print_variable_and_description(type(str(i)),"The value of type(str(i))")

print(the_string)
#########################################################