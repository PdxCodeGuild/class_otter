# names = ['David', 'Helen', 'Anne']
# lower_names = [name.lower() for name in names]
# lower_names  #> ['david', 'helen', 'anne']

# names = ['David', 'Helen', 'Anne']
# lower_names = []
# for name in names:
#     lower_names.append(name.lower())
# print(names)
# print(lower_names)

# def say_hello(name):
#     return f"Hello, {name}!"

# names = ['David', 'Helen', 'Anne']
# lower_names = [say_hello("name") for _ in names]


#Filtering Elements
# one instance you can chamge the number of items is use an "if"
#people = ['Bob J.', 'Joe S.', 'Jane K.', 'Bob F']
#bobs_only = [person for person in people if person.startswith('Bob')]

#print(people)
#print(bobs_only)
# ['Bob J.', 'Joe S.', 'Jane K.', 'Bob F']
# ['Bob J.', 'Bob F']

# people = ['Bob J.', 'Joe S.', 'Jane K.', 'Bob F']
# bobs_only = [f"Hello {person}!" for person in people if person.startswith('Bob')]

nums = range(0, 20)

doubled_evens = [num * 2 if num % 2 == 0 else num for num in nums]

print(doubled_evens)
