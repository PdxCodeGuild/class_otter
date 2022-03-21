
# Create a function to multiply two numbers together and return the result for further processing.


# Let's pick some words for some stuff:

# What do we want to name the function:
    # multiply
# What names do we want for the two input parameters:
    # num1, num2
# We want to use some intermediate variable name while working with the numbers. What variable name shall we use:
    # answer

# Type here an equation you would use to show how you multiply two numbers (let's use 3 and 7).
# Include the two numbers you're mulitiplying, an equals sign, and the number we get when we multiply the two numbers together:
# 7 * 3 = 21

# We changed the order of the above equation to remember that in Python
# we do the operations/calculations to the right of the '=' and 
# then assign that resulting value to the variable to the left of the '='.
#   21   =   7  *   3
# answer = num1 * num2

def multiply(num1, num2):
    answer = num1 * num2
    return answer

# Remember that pytest needs to be installed to run the tests. If pytest is not installed, the function can be tested using print statements.
    # https://docs.pytest.org/en/6.2.x/getting-started.html
        # TLDR:
        # Command to install pytest, this command is run in the terminal (like powershell or windows cmd) (not inside a python session):
            # pip install -U pytest

def test_multiply():
    assert multiply(3,7) == 21
    assert multiply(8,3) == 24
    assert multiply(3,3) == 9