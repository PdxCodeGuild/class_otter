user = float(input("what is distance? "))
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

print(output)




