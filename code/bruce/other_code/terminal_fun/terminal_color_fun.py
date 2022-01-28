# ************************************* #
#           Terminal Color Fun          #
#   Uses: colorama, Fore, Back, Style   #
#              Version: 1.0             #
#          Author: Bruce Stull          #
#               2022-01-06              #
# ************************************* #

from colorama import Fore, Back, Style
print(Fore.RED + 'this is red text')
print(Back.BLUE + 'this is red text on a blue background', end='')
print(Style.RESET_ALL)
print('back to normal')