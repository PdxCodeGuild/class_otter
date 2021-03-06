# *********************** #
#       Style Guide       #
#       python PEP-8      #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-23       #
# *********************** #

# Resources:
# https://www.python.org/dev/peps/pep-0008/

from typing import AnyStr


def my_func(input: AnyStr = "No string provided"):
    '''my_func'''
    print(input)
    pass

my_func()   # No string provided
my_func('word') # word

# typing
# https://docs.python.org/3/library/typing.html

def greeting(name: str) -> str:
    return 'Hello, ' + name

print(greeting('Bunbun'))   # Hello, Bunbun

# Wrap single-element tuple with parentheses to clarify that it's a tuple.
name_tuple_without_parens = 'Karl',
name_tuple_with_parens = ('Cassidy',)

print(name_tuple_without_parens)
print(name_tuple_with_parens)


def print_a_list(list_=[]):
    print(list_)

print_a_list()  # []
print_a_list([1, 2, 3])  # [1, 2, 3]


# isinstance
the_thing = ''
if isinstance(the_thing, int):
    print(the_thing)
else:
    print("not an int")
# not an int

the_thing = 143
if isinstance(the_thing, int):
    print(f"An int: {the_thing}")
else:
    print("not an int")
# 143

the_thing = {}
if isinstance(the_thing, dict):
    print(f"A dict: {the_thing}")
else:
    print("not an int")


# Empty sequences return False.
sequence_ = ('a', 'b', 'c')

if not sequence_:
    print("Empty sequence.")
if sequence_:
    print("Non-empty sequence.")
# Non-empty sequence.

sequence_ = ()

if not sequence_:
    print("Empty sequence.")
if sequence_:
    print("Non-empty sequence.")
# Empty sequence.

# Python program to demonstrate
# name mangling
class Student:
    def __init__(self, name):
        self.__name = name
  
s1 = Student("Santhosh")
print(dir(s1))
# NOTE: '__name' ==> '_Student__name'
# ['_Student__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

# Python program to demonstrate
# name mangling
class Student:
    def __init__(self, name):
        self.__name = name
  
s1 = Student("Santhosh")
print(s1._Student__name)
# Santhosh