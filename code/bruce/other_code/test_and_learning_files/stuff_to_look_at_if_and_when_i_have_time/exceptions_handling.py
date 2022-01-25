

# Resources:
# https://github.com/brucestull/PDX_Full_Stack/blob/bruce/1%20Python/docs/02%20Exceptions%20%26%20Testing.md
# https://www.tutorialsteacher.com/python/error-types-in-python

# ####################### ValueError #######################
# def crash(i):
#     if i < 0:
#         raise ValueError('i needs to be 0 or greater.')
#     print("Error not encountered here.")


# print("before crash")

# try:
#     crash(1)
# except ValueError:
#     print("Error occured but continuing nonetheless.")

# print("after crash")

# ##########################################################


# ########################## TypeError ##########################
# # It seems that once the error is encountered, the operation jumps to the except block, skipping in-between code.
# try:
#     this_wont_work = 1 + 'hello'
#     print("This won't print.")
#     print("Niether will this.")
# except TypeError:
#     print('That didn\'t work!')
# ###############################################################
# # It seems that once the error is encountered, the operation jumps to the except block, skipping in-between code.
# # And since the exception is caught, the program can continue.
# try:
#     this_wont_work = 1 + 'hello'
# except TypeError:
#     print('That didn\'t work!')
# print("This will print since the exception is caught immediately after it raised.")
# ###############################################################


# ######################## KeyError ########################
# my_dict = {'a':1}
# try:
#     my_value = my_dict['b'] # The stuff/logic/etc which we are wrapping with try/except.
# except KeyError:            # When type KeyError is encountered in 'try' block, we execute the except's code block. We can choose how we want to handle the situation for business needs.
#     my_value = my_dict['a']
#     print('Defaulting to dictionary \'a\' value.')
# ##########################################################


# ######################## ValueError ########################
# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Please enter integer numeric value.")

# print(x)
# ############################################################


# ###### Catching multiple exceptions ######
# import random

# # using a tuple
# print("Catch using tuple.")
# try:
#     if random.randint(0, 1) == 0:
#         raise KeyError('key error')
#     else:
#         raise IndexError('index error')
# except (KeyError, IndexError) as e:
#     print(e)
#     print(f"KeyError: {type(e) == KeyError}")
#     print(f"IndexError: {type(e) == IndexError}")

# # using multiple except blocks
# print("Catch using multiple except blocks.")
# try:
#     if random.randint(0, 1) == 0:
#         raise IndexError('index error')
#     else:
#         raise KeyError('key error')
# except KeyError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# ##########################################


# ############ else and finally ############
# try:
#     f = open('file.txt')
#     contents = f.read()
#     print(contents)
# except (IOError, OSError) as e:
#     print(e)
# except NameError:
#     print("NameError encountered.")
# else:
#     print('no exception occurred')
# finally:
#     f.close()
# ##########################################