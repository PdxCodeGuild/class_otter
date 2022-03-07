# ***************************** #
#   Function Returns Function   #
#                               #
#          Version: 0.0         #
#      Author: Bruce Stull      #
#           2022-01-13          #
# ***************************** #

# Resource:
# https://towardsdatascience.com/python-for-beginners-functions-2e4534f0ae9d

def functionTwo():
    print(input("Gimme a string: "))

def functionOne():
    return functionTwo()

functionOne()