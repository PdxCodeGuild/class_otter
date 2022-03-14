# ****************************** #
#          REGEX FUN!!!          #
#   How much fun can be had???   #
#          Version: 0.0          #
#      Author: Bruce Stull       #
#           2022-01-12           #
# ****************************** #

import re

# Resources:
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/0%20Intro/05%20Regular%20Expressions.md
# https://github.com/PdxCodeGuild/class_otter/blob/bruce/1%20Python/docs/12%20Regular%20Expressions%20in%20Python.md
# https://docs.python.org/3/howto/regex.html
# https://regexr.com/



# s1 = 'we can\'t write \\ as easily, but escapes \' work'
# s2 = r'we can write \ more easily, but escapes \" dont work'
# print(s1) # we can't write \ as easily, but escapes ' work
# print(s2) # we can write \ more easily but escapes \" dont work

fox_dog_string = "The quick brown fox jumps over the lazy dog."

other_string = r'''RegExr was created by gskinner.com, and is proudly hosted by Media Temple.
Edit the Expression & Text to see matches. Roll over matches or the expression for details. PCRE & JavaScript flavors of RegEx are supported. Validate your expression with Tests mode.
The side bar includes a Cheatsheet, full Reference, and Help. You can also Save & Share with the Community, and view patterns you create or favorite in My Patterns.
Explore results with the Tools below. Replace & List output custom results. Details lists capture groups. Explain describes your expression in plain English.'''

# pattern = r"(\w+) (\w+) (\w+) (\w+) (\w+)"
# result = re.search(pattern, other_string)
# print(result.group())
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))

# pattern = r"(\w+)"
# result = re.findall(pattern, other_string)
# print(result)



some_sort_of_string = "Isaac Newton, physicist"
pattern = r"(\w+) (\w+)"
result = re.match(pattern, some_sort_of_string)
print(result)
print(result.group())      # The entire match 'Isaac Newton'
print(result.group(1))     # The first parenthesized subgroup 'Isaac'
print(result.group(2))     # The second parenthesized subgroup 'Newton'
print(result.group(1, 2))  # Multiple arguments give us a tuple ('Isaac', 'Newton')

# Isaac Newton
# Isaac
# Newton
# ('Isaac', 'Newton')

# still_yet_another_string = "June 14"
# pattern = r"([a-zA-Z]+) (\d+)"
# result = re.match(pattern, still_yet_another_string)
# print(result.start()) # the beginning of the match, 0
# print(result.end()) # the end of the match, 7
# print(result.group()) # same as result.group(0), 'June 14'
# print(result.group(1)) # 'June'
# print(result.group(2)) # '24'

# 0
# 7
# June 14
# June
# 14