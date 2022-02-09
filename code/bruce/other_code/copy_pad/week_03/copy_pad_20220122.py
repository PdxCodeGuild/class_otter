
# Resources:
# https://towardsdatascience.com/10-examples-to-master-args-and-kwargs-in-python-6f1e8cc30749

# Understanding *args.

# def addition(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
# print(addition(1,2,3))
# print(addition(1,2,3,4,5))
# print(addition(1,2,3,4,5,6,7))
# # 6
# # 15
# # 28

# def arg_printer(a, b, *args):
#     print(f'a: {a}')
#     print(f'b: {b}')
#     print(f'args: {args}')
# arg_printer(3, 4, 5, 8, 3, 7)
# # a: 3
# # b: 4
# # args: (5, 8, 3, 7)

# def addition(a, b, *args, option=True):
#     result = 0
#     if option:
#         for i in args:
#             result += i
#         return a + b + result
#     else:
#         return result
# print(addition(1,2,3,4,5))
# print(addition(1,2,3,4,5,6))
# print(addition(1,2,3,4,5,6,7,option=False))
# # 15
# # 21
# # 0

# def arg_printer(a, b, option=True, **kwargs):
#     print(a, b)
#     print(option)
#     print(kwargs)
# arg_printer(3, 4, param1=5, param2=6)
# # 3 4
# # True
# # {'param1': 5, 'param2': 6}

# def arg_printer(a, b, *args, option=True, **kwargs):
#     print(a, b)
#     print(args)
#     print(option)
#     print(kwargs)
# arg_printer(1, 4, 6, 5, param1=5, param2=6)
# # 1 4
# # (6, 5)
# # True
# # {'param1': 5, 'param2': 6}

# def arg_printer(*args):
#     print(args)
# the_list = [1,4,5]
# arg_printer(the_list) # Returns a one-element tuple. That one element is a list.
# # ([1, 4, 5],)

# def arg_printer(*args):
#     print(args)
# the_list = [1,4,5]
# # Use '*' in front of variable '*the_list' to unpack the contents of the_list 
# # into a tuple containing three elements. Each element is an element provided from the_list.
# arg_printer(*the_list)
# # (1, 4, 5)

# def arg_printer(*args):
#     print(args)
# the_tuple = (1, 2, 3)
# the_list = [1,4,5]
# arg_printer(the_tuple)
# arg_printer(the_list)
# # ((1, 2, 3),)
# # ([1, 4, 5],)

# def arg_printer(*args):
#     print(args)
# the_tuple = (1, 2, 3)
# the_list = [1, 4, 5]
# arg_printer(*the_tuple)
# arg_printer(*the_list)
# # (1, 2, 3)
# # (1, 4, 5)

# def arg_printer(*args):
#     print(args)
# the_list = [1, 4, 5]
# the_tuple = ('a', 'b', 4)
# arg_printer(*the_list, *the_tuple, 5, 6)
# # (1, 4, 5, 'a', 'b', 4, 5, 6)

# ######### BIG IDEA #########
# # NOTE: We can use a dictionary (or some other iterable mapping thingy) to pass **kwargs into a function.
# def arg_printer(**kwargs):
#     print(kwargs)
# the_dictionary = {'param1':5, 'param2':8}
# arg_printer(**the_dictionary)
# # {'param1': 5, 'param2': 8}

# def arg_printer(**kwargs):
#     print(kwargs)
# the_dictionary = {'param1':5, 'param2':8}
# arg_printer(param3=9, **the_dictionary)
# # {'param3': 9, 'param1': 5, 'param2': 8}

# NOTE: Each kwarg can be passed separately. In this example we have one single-entry dictionary, and one two-entry dictionary.
def arg_printer(**kwargs):
    print(kwargs)
the_dictionary = {'param1':5, 'param2':8}
first_dictionary = {'param3':9}
# NOTE: We type in the variable which is the kwarg, and add two asterisks in front of the variable name.
# The variable 'the_dictionary' can be passed as kwarg by '**the_dictionary'.
arg_printer(**first_dictionary, **the_dictionary)
# {'param3': 9, 'param1': 5, 'param2': 8}
