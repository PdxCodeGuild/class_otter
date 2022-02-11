#******************************#
# Project: Programming101_Unit04_Lab_3_Extra
#
#        Version: 1.0
#    Author: Bruce Stull
#   Date: December 8, 2021
#******************************#

# Now we'll ask the user for the distance, the starting units, and the units to convert to.

# Create dictionary of equal-length items. Used https://duckduckgo.com/?q=how+many+feet+in+km&ia=answer for conversion factors.
conversion = {
    'in': 39370.08,
    'ft': 3280.84,
    'yd': 1093.613,
    'm': 1000,
    'fathom': 546.806649169,
    'km': 1,
    'mi': .6213712,
}

# ##############################################################################
# # Prompt user to enter distance they want converted from.
# response_as_string = input("\nPlease enter the distance you want to convert: ")

# # Convert response string to integer type.
# response_as_integer = int(response_as_string)

# # Prompt user to choose input units.
# input_units = input("Please enter the units for input distance (ft/m/km/mi/yd/in): ")   # TODO: Use dictionary to populate the unit options: ft/m/km/mi/yd/in.

# # Prompt user to chose output units.
# output_units = input("Please enter the units for output distance (ft/m/km/mi/yd/in): ")   # TODO: Use dictionary to populate the unit options: ft/m/km/mi/yd/in.

# # General conversion equation example.
# # X m = Y ft * ( A m / B ft)

# # Calculate the output length for input length and units.
# output_distance = response_as_integer * conversion[output_units] / conversion[input_units]

# # Display results
# print(f"\n> {response_as_integer} {input_units} is {round(output_distance, 3)} {output_units}\n")
# ##############################################################################


# Make the function to convert:
def length_converter(input_length, input_units, output_units, conversion_dict):
    '''Accepts input length, input units, output units, and conversion dictionary. Returns length in output_units.'''
    return input_length * conversion_dict[output_units] / conversion_dict[input_units]


