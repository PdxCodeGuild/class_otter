# *********************** #
#   Copy Pad 2022-01-13   #
#                         #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-13       #
# *********************** #


dict_01 = {'a':'1','b':'2'}
dict_02 = {'b':'2','a':'1'}

list_to_save = [dict_01,dict_02]

print(list_to_save)

# Convert list of dictionaries to a comma-separated string, with '\n' between dictionaries.

def dict_to_string(dictionary):
    '''Accepts a dictionary argument. Converts the dictionary to csv string. Returns the string.'''
    return_string = ''
    for key in dictionary.keys():
        print(key)


dict_to_string(dict_01)
