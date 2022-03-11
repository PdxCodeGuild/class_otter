# *********************** #
#     String Functions    #
#     f-string format     #
#       Version: 0.0      #
#   Author: Bruce Stull   #
#        2022-01-18       #
# *********************** #

# 
alpha_string = 'abcdefghij'
num_string = 123456789

eff_string = f"{alpha_string}:{num_string}"
print(eff_string)
# abcdefghij:123456789

the_number = 'the number'
print('the number: {}'.format(num_string))
print('{}: {}'.format(the_number, num_string))
print(f"the number: {num_string}")
# the number: 123456789
# the number: 123456789
# the number: 123456789