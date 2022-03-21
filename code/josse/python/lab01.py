'''user = float(input("what is distance? "))
units = input("please choose feet,meters, miles,kilometers,yards, inches: ")
feet = 0.3048
miles = 1609.34
kilometers = 1000
yard = 0.9144
inch = 0.0254

if units == "meters":
      print(user)

elif units == "feet":
    output = user * feet
    print(output)

elif units == "miles":
    output = user * miles
    print(output)

elif units == "kilometers": 
    output = user * kilometers
    print(output)
    
elif units == "yards":
    output = user * yard
    print(output)

elif units == "inches":
    output = user * inch
    print(output)

print(output)'''

metrics = {
    
"feet" : 0.3048,
"miles" : 1609.34,
"kilometers" : 1000,
"yard" : 0.9144,
"inch" : 0.0254,
"meter": 1
}

distance = float(input("what is your distance? "))
input_1 = input("pick input unit feet,miles,kilometers,yard or inch? ")
output_1 = input("pick output unit feet,miles,kilometers,yard or inch? ")

user = distance * metrics[input_1]

answer = user / metrics[output_1]

print(f"your conversion is {answer} {output_1}")