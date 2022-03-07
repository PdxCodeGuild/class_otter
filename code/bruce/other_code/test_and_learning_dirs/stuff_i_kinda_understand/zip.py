# zip() can zip two things together.
# Using argument 'strict=True' checks arguments are same lenght.

names = ["Tom", "Harry", "Jessica", "Robert", "Kevin"]
numbers = ["21024", "75978", "92176", "75192", "34323"]
the_list = list(zip(names, numbers))
print(the_list)
# [('Tom', '21024'), ('Harry', '75978'), ('Jessica', '92176'), ('Robert', '75192'), ('Kevin', '34323')]

names = ["Tom", "Harry", "Jessica", "Robert"]     # Kevin is missing
numbers = ["21024", "75978", "92176", "75192", "34323"]
the_list = list(zip(names, numbers))
print(the_list)
# [('Tom', '21024'), ('Harry', '75978'), ('Jessica', '92176'), ('Robert', '75192')]

# names = ["Tom", "Harry", "Jessica", "Robert"]     # Kevin is missing
# numbers = ["21024", "75978", "92176", "75192", "34323"]
# the_list = list(zip(names, numbers, strict=True))
# print(the_list)
# # Traceback (most recent call last):
# #   File "C:\Users\Bruce\Programming\class_otter\code\bruce\other_code\test_and_learning_files\stuff_i_kinda_understand\zip.py", line 18, in <module>
# #     the_list = list(zip(names, numbers, strict=True))
# # ValueError: zip() argument 2 is longer than argument 1

# WOW!!! Strings can be zipped!
a = "abc"
b = "def"
print(list(zip(a,b)))
# [('a', 'd'), ('b', 'e'), ('c', 'f')]