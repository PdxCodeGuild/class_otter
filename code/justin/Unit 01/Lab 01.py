# Full Stack Bootcamp - Unit 01 Lab 01
# Justin Hammond, 01/03/2022

# Unit Converter
# This program will convert a number between different units of measure

foot_factor = 0.3048

def convert_to_meters(distance_in_feet):
    return round(distance_in_feet * foot_factor, 4)

def main():
    distance_in_feet = float(input("Enter a distance in feet: "))
    
    # Convert a distance measured in feet to one in meters
    distance_in_meters = convert_to_meters(distance_in_feet)

    print(f"{distance_in_feet}ft is {distance_in_meters}m\n")

    pass


main()
