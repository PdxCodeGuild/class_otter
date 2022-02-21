import blog

author = 'GnomeChompsky'

#### List comprehension to get posts by author ####
posts = [post for post in blog.posts if post['author'] == author]
print(posts)
###################################################

# names = ["Tom", "Harry", "Jessica", "Robert", "Kevin"]
# numbers = ["21024", "75978", "92176", "75192", "34323"]
# the_list = list(zip(names, numbers))
# print(the_list)
# # [('Tom', '21024'), ('Harry', '75978'), ('Jessica', '92176'), ('Robert', '75192'), ('Kevin', '34323')]

# names = ["Tom", "Harry", "Jessica", "Robert"]     # Kevin is missing
# numbers = ["21024", "75978", "92176", "75192", "34323"]
# the_list = list(zip(names, numbers, strict=True))
# print(the_list)
# # Traceback (most recent call last):
# #   File "C:\Users\Bruce\Programming\class_otter\code\bruce\Module_02\lab03_Blog\test.py", line 17, in <module>
# #     the_list = list(zip(names, numbers, strict=True))
# # ValueError: zip() argument 2 is longer than argument 1

# a = "abc"
# b = "def"
# c = list(zip(a,b))
# print(c)
# # [('a', 'd'), ('b', 'e'), ('c', 'f')]
