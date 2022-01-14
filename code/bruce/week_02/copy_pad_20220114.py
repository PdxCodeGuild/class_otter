# *********************** #
#   Copy Pad 2022-01-14   #
#                         #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-14       #
# *********************** #

# Make a list of dictionaries. See if we can use index() on it.
list_of_dictionaries = [{'a':'1','b':'2'},{'a':'3','b':'4'},{'a':'5','b':'6'}]

where_is_a3_b4 = list_of_dictionaries.index({'a':'3','b':'4'})
print(where_is_a3_b4)

where_is_a3_b4 = list_of_dictionaries.index({'b':'2','a':'1'})
print(where_is_a3_b4)

# It seems we can compare dictionaries.
print(list_of_dictionaries[0] == {'a':'1','b':'2'})
