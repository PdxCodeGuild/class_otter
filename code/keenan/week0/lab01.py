# Lab 01 Unit Converter
# 01/04/2022

# get user input for distance 
dist = int(input('What is the distance? '))

# get user input for input unit
unit_in = input('Please provide the input unit in its abbreviated form. What is the input unit? ')

if unit_in == 'ft':
    meters = dist * 0.3048
elif unit_in == 'mi':
    meters = dist * 1609.34
elif unit_in == 'm':
    meters = dist * 1
elif unit_in == 'km':
    meters = dist * 1000
elif unit_in == 'yd':
    meters = dist * 0.9144
elif unit_in == 'in':
    meters = dist * 0.0254
else:
    print("Incorrect unit provided. Check abbreviation.")

print(meters)

unit_out = input('What is the output unit? ')

if unit_out == 'm':
    final = round(meters, 4) 
elif unit_out == 'ft':
    final = meters / 0.3048
elif unit_out == 'mi':
    final = meters / 1609.34
elif unit_out == 'km':
    final = meters / 1000
elif unit_out == 'yd':
    final = meters / 0.9144
elif unit_out == 'in':
    final = meters / 0.0254

final = round(final, 4) 
print(f"{dist} {unit_in} is {final} {unit_out}.")