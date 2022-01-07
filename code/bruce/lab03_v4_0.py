# *********************** #
#     Number to Phrase    #
#      Time to Phrase     #
#       Version: 4.0      #
#   Author: Bruce Stull   #
#        2022-01-05       #
# *********************** #

# Convert a time given in hours and minutes to a phrase.

# Resources:
# https://tutors.com/lesson/military-time
# https://military-history.fandom.com/wiki/NATO_phonetic_alphabet

input_time_as_integer = 2130

hours = {
    2400 : 'Twenty Four Hundred Hours',
    2300 : 'Twenty Three Hundred Hours',
    2200 : 'Twenty Two Hundred Hours',
    2100 : 'Twenty One hundred Hours',
    2000 : 'Twenty Hundred Hours',
    1900 : 'Nineteen Hundred Hours',
    1800 : 'Eighteen Hundred Hours',
    1700 : 'Seventeen Hundren Hours',
    1600 : 'Sixteen Hundred Hours',
    1500 : 'Fifteen Hundred Hours',
    1400 : 'Fourteen Hundred Hours',
    1300 : 'Thirteen Hundred Hours',
    1200 : 'Twelve Hundred Hours',
    1100 : 'Eleven Hundred Hours',
    1000 : 'Ten Hundred Hours',
    900  : 'Zero Nine Hundred Hours',
    800  : 'Zero Eight Hundred Hours',
    700  : 'Zero Seven Hundred Hours',
    600  : 'Zero Six Hundred Hours',
    500  : 'Zero Five Hundred Hours',
    400  : 'Zero Four Hundred Hours',
    300  : 'Zero Three Hundred Hours',
    200  : 'Zero Two Hundred Hours',
    100  : 'Zero One Hundred Hours'
}

