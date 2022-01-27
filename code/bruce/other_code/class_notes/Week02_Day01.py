# ************************ #
#   Week 01 - Lecture 01   #
#      Lists and Such      #
#       Version: 1.0       #
#   Author: Bruce Stull    #
#        2022-01-10        #
# ************************ #

# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/docs/09%20Lists%20%26%20Tuples.md

import random

nums = [x**2 for x in range(10)]
print(nums)

nums = [x**2 for x in [0,1,2]]
print(nums)

nums = [x**2 for x in range(10) if x != 4]
print(nums)

names = ['David', 'Helen', 'Anne']
lower_names = [name.lower() for name in names]
print(lower_names)  #> ['david', 'helen', 'anne']
greeting_strings = [f"Hello, {name}!" for name in names]
print(greeting_strings)

ticket = [random.randint(1,99) for _ in names]
print(ticket)

people = ['Bob J.', 'Joe S.', 'Jane K.', 'Bob F']
bobs_only = [person for person in people if person.startswith('Bob')]
print(people)
print(bobs_only)

nums = range(0,20)
print(nums)

# Disposes odd nums
doubles = [ num * 2 for num in nums if num % 2 == 0]
print(doubles)
# Only modify the ones which match num % 2 == 0
double_evens = [(num * 2 if num % 2 == 0 else num) for num in nums]
print(double_evens)

the_dict = {
    'A': 1,
    'B': 2
}

print(the_dict.get('A'))
