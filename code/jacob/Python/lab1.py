"""
Lab 1: Unit Converter
This lab will involve writing a program that allows the user to convert a number between units.

"""

"""

Version 1

"""

print()

# input of distance to be converted
# equation to convert distance given to meters
# output conversion

convert = {1: 0.3048}
distance = int(input("What is the distance in feet?: "))
conversion = distance * convert[1]
print(f'{distance} is {round(conversion, 4)} meters.')

print()


"""

Version 2

"""

print()

# setup the dictionary for conversion table
# converting from different units of measure

new_convert = {'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000}
new_distance = int(input("What is the distance?: "))
units = input("What are the units?: ")
new_conversion = new_distance * new_convert[units]

print(f'{new_distance} {units} is {round(new_conversion, 4)} meters.')
print()

"""

Version 3

"""

# updated the conversion dictionary to incorporate yards and inches

new_measures = {'yd': 0.9144, 'in': 0.0254}
new_convert.update(new_measures)

new_distance = int(input("What is the distance?: "))
units = input("What are the units?: ")
new_conversion = new_distance * new_convert[units]

print(f'{new_distance} {units} is {round(new_conversion, 4)} meters.')
print()


"""

Version 4

"""

print()

# converting from one unit of meaure to another unit of measure

new_convert = {'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000, 'yd': 0.9144, 'in': 0.0254}
new_distance = int(input("What is the distance?: "))
units = input("What are the units?: ")

new_conversion = new_distance * new_convert[units]

meters = {'ft': 3.2808, 'mi': 0.00062137, 'm': 1, 'km': 0.001, 'yd': 1.0936, 'in': 39.37}

newconvert = input("What are the output units?: ")

new_output = new_conversion * meters[newconvert]

print(f'{new_distance} {units} is {round(new_output, 4)} {newconvert}')

print()
                                