# ******************************** #
#   Super Basic Function Example   #
#                                  #
#           Version: 1.0           #
#       Author: Bruce Stull        #
#            2022-01-13            #
# ******************************** #

# Create two variables to hold values we will use later.
rectangle_width = 10
rectangle_length = 5

# Define function to calculate area of a rectangle.
def area_of_rectangle(length, width):
    '''Accepts arguments of 'length' and 'width'. RETURNs the area of a rectangle which has "length" and "width".'''
    # On this line: We do two things:
        # 1. Calculate the area of the rectangle by executing "length * width".
        # 2. Assign the result of "length * width" to "rectangle_area".
        # By placing "rectangle_area = " in front of "length * width",
            # we tell python to execute "length * width" and assign the value of that execution to "rectangle_area".
        # NOTE: An execution of "length * width" is occuring followed by 
            # assignment of that value to "rectangle_area". The order matters.
        # NOTE: We assign the value of "length * width" to a variable so we can use it later.
            # We don't HAVE to use this intermediate step in this simple function,
            # but realizing what we are doing can help.
        # NOTE: TODO: Your task is to figure out how to put a print() statement in this
            # function to 'see' what's going on, but also make sure the function is 'return'-ing the area to function caller.
    rectangle_area = length * width
    # We have the function return a value here so that the information can be processed further in other functions or logic.
    return rectangle_area

# We now 'call' the function and insert the desired parameters in the () of the function.
area_of_rectangle(rectangle_width, rectangle_length)

# But... even though the call is valid and won't result in error, we want to do two things:
# 1. Call the function and provide parameters.
# 2. Assigne the result of calling the function to some new variable so we can use it later.
    # Like in further logic or print statements or whatever.
area_of_specific_rectangle = area_of_rectangle(rectangle_width, rectangle_length)

# Now, we can do further processing or logic on 'area_of_specific_rectangle'.
# We will print out the result here, but we are only printing out the result 
    # to see that the function is working.
print(area_of_specific_rectangle)
# See me if you want to write a test function for this example.
    # Test functions let us test a function without using print statements.
    # Print statements are okay for troubleshooting, but we need to use other methods
    # to further process the logic. So maybe a good solution is to print something to
    # see what's going on, BUT still return the value to function caller.