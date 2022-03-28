"""
Allow the user to also enter the units. 
Then depending on the units, convert the distance into meters.
The units we'll allow are feet, miles, meters, and kilometers.
"""

metrics ={
    'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000
    }

user_distance = float(input('what is the distance?'))
units = input('what are the units the distance is in? ')

print(f'{metrics[units] * user_distance} m.')
