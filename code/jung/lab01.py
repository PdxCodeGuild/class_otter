#Version 1

# distance = int(input("What is the distance in feet? "))
# converter = distance * 0.3048
# converter = round(converter, 4)
# answer = f"{distance} ft is {converter} m"
# print(answer)


#Version 2

# distance = int(input("What is the distance? "))
# unit = input("What are the units? ")

# if unit == "ft":
#     answer = distance * 0.3048
# elif unit == "mi":
#     answer = distance * 1609.34
# elif unit == "m":
#     answer = distance * 1
# elif unit == "km":
#     answer = distance * 100

# answer = round(answer)

# result = f"{distance} {unit} is {answer} m"

# print(result)



#Version 3

# distance = int(input("What is the distance? "))
# unit = input("What are the units? ")

# if unit == "ft":
#     answer = distance * 0.3048
# elif unit == "mi":
#     answer = distance * 1609.34
# elif unit == "m":
#     answer = distance * 1
# elif unit == "km":
#     answer = distance * 100
# elif unit == "yd":
#     answer = distance * 0.9144
# elif unit == "in":
#     answer = distance * 0.0254

# answer = round(answer)

# result = f"{distance} {unit} is {answer} m"

# print(result)


#Version 4

distance = int(input("What is the distance? "))
input_unit = input("What are the input units? ")
output_unit = input("What are the output units? ")

if input_unit == "ft":
    convert_to_meter = distance * 0.3048
elif input_unit == "mi":
    convert_to_meter = distance * 1609.34
elif input_unit == "m":
    convert_to_meter = distance * 1
elif input_unit == "km":
    convert_to_meter = distance * 1000

if output_unit == "ft":
    answer = convert_to_meter / 0.3048
elif output_unit == "mi":
    answer = convert_to_meter / 1609.34
elif output_unit == "m":
    answer = convert_to_meter / 1
elif output_unit == "km":
    answer = convert_to_meter / 1000

result = f"{distance} {input_unit} is {answer:.7} {output_unit}"

print(result)