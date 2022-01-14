#******************************#
# Project: Pyton Full-Stack 
#  Lab: 01 Unit Converter
#        Version: v01,v02,v03,v04
#    Author: Bruce Stull
#   Date: January 4, 2022
#******************************#

# Assignment:
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/01%20Unit%20Converter.md

# Create a 'conversion' dictionary to hold the units and corresponding value of a specified length in that scale.
# 1 ft == .3048 m == X <other units>
# 39370.08 in == 3280.84 ft == 1093.613 yd == 1000 m == 1 km == .6213712 mi
# {'in': 39370.08, 'ft': 3280.84, 'yd': 1093.613, 'm': 1000, 'km': 1, 'mi': .6213712}
conversion = {
    'in': 39370.08,
    'ft': 3280.84,
    'yd': 1093.613,
    'm' : 1000,
    'km': 1,
    'mi': .6213712
}

# Create length unit dictionary to allow user to input several different forms of each unit and have the converter still work.
# in/inch/"/ft/feet/'/yd/yard/m/meter/km/kilometer/mi/mile
units = {
    'in'    : 'in',
    'inch'  : 'in',
    '"'     : 'in',
    'ft'    : 'ft',
    'feet'  : 'ft',
    "'"     : 'ft',
    'yd'    : 'yd',
    'yard'  : 'yd',
    'm'     : 'm',
    'meter' : 'm',
    'km'    : 'km',
    'kilometer': 'km',
    'mi'    : 'mi',
    'mile'  : 'mi'
}

# Welcome user.
welcome_string = "\nWelcome to convertinator 2022!\n"
print(welcome_string)

# Prompt user to provide input length.
# Keep looping and requesting input as long as provided input is not valid.
while True:
    # Prompt user for input length and save to variable.
    input_length_as_string = input("Please enter an input length: ")
    # If user input is not numeric:
    if not input_length_as_string.replace('.','').isnumeric():
        # Notify user.
        print("Please enter a numeric value.")
        # Go back to beginning and prompt for input.
        continue
    else:
        break

# Print acctepted input units.
print("Accepted input units: in/inch/\"/ft/feet/\'/yd/yard/m/meter/km/kilometer/mi/mile")

# Loop to prompt user to input units. Keep looping as long as input is not valid.
while True:
    # Prompt user for input unit and save to variable.
    input_unit = input("Please enter input length units: ")
    # If user input is not one of the keys in the dictionary:
    if not input_unit in units.keys():
        # Inform user to input one of the choices.
        print("Please enter one of the choices for input length units.")
        # Go back to beginning of loop and prompt for input again.
        continue
    else:
        input_unit = units[input_unit]
        break

# Print accepted output units.
print("Accepted output units: in/inch/\"/ft/feet/\'/yd/yard/m/meter/km/kilometer/mi/mile")

# Loop to prompt user for output units. Keep looping as long as input is not valid.
while True:
    # Prompt user to enter output units.
    output_unit = input("Please enter the output length units: ")
    # If user input is not one of the keys in the dictionary:
    if not output_unit in units.keys():
        # Inform user to input one of the choices.
        print("Please enter one of the choices for output length units.")
        # Go back to beginning of loop and prompt for input again.
        continue
    else:
        output_unit = units[output_unit]
        break

# Convert the string-type input_length_as_string to int-type.
input_length_as_float = float(input_length_as_string)

# Convert the input value to a value in output units.
# X (m) = Y (ft) * (m) / (ft)
output_length = input_length_as_float * conversion[output_unit] / conversion[input_unit]

# Print results.
print(f'''
{input_length_as_float} {input_unit} is {round(output_length, 3)} {output_unit}
''')
