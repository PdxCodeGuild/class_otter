
# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/10%20Functions.md

# Function named add_numbers.
# Accepts arguments of num_01 and num_02
# Returns the the result of adding num_01 to num_02

# Function named print_the_result.
# Accepts argument of any type, name of argument should be input_argument.
# Prints the value of the argument to console.

def add_number(num_01, num_02):
    answer = num_01 + num_02
    print_the_result(f"result of addition: {answer}") # <<== Don't really need to make our own function since python alreacy includes print().
    return answer

def print_the_result(input_argument):
    print(input_argument)

number = add_number(3, 6)