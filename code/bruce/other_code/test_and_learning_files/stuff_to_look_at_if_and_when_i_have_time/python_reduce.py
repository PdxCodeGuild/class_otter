# *********************** #
#     Python reduce()     #
#     functools lambda    #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-18       #
# *********************** #

# print([(int * 2 if list[i] % 2 == 0 else list[i]) for i, int in enumerate(list)])
# [0, 1, 4, 3, 8, 5, 12]
# print([(list[i] * 2 if list[i] % 2 == 0 else list[i]) for i, int in enumerate(list)])
# [0, 1, 4, 3, 8, 5, 12]
# print([(int * 2 if int % 2 == 0 else int) for i, int in enumerate(list)])
# [0, 1, 4, 3, 8, 5, 12]
# print([(int * 2 if int % 2 == 0 else int) for int in enumerate(list)])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# TypeError: unsupported operand type(s) for %: 'tuple' and 'int'
# print([(int * 2 if int % 2 == 0 else int) for i, int in enumerate(list)])
# [0, 1, 4, 3, 8, 5, 12]

# python code to demonstrate working of reduce()

# importing functools for reduce()
import functools

# initializing list
numbers = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, numbers))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, numbers))
