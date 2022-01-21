
# Create a function to multiply two numbers together and return the result for further processing.


# Let's pick some words for some stuff:

# What do we want to name the function: multiply
# What names do we want for the two input parameters: num1, num2
# We want to use some intermediate variable name while working with the numbers. What variable name shall we use: answer

# Type here an equation you would use to show how you multiply two numbers (let's use 3 and 7).
# Include the two numbers you're mulitiplying, an equals sign, and the number we get when we multiply the two numbers together:
# 7 * 3 = 21
# 21 = 7 * 3

def multiply(num1, num2):
    answer = num1 * num2
    return answer

def test_multiply():
    assert multiply(3,7) == 21
    assert multiply(8,3) == 24
    assert multiply(3,3) == 9