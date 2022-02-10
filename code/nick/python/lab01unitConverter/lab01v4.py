
# https://github.com/PdxCodeGuild/class_otter/blob/main/1%20Python/labs/01%20Unit%20Converter.md

metrics ={
    'ft': 0.3048, 'in': 1609.34, 'mi': 1609.34, 'm': 1, 'km': 1000
    }
user_distance = float(input('what is the distance? '))
unit = input('what are the units? ')
output = input('what are the output units? ')


conversion = metrics[unit] * user_distance
second_conversion = conversion / metrics[output]

print(f'{user_distance}{unit} is {second_conversion} {output}.')