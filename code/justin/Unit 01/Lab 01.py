# Full Stack Bootcamp - Unit 01 Lab 01
# Justin Hammond, 01/03/2022

# Unit Converter
# This program will convert a number between different units of measure

conversion_factor_map = {
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34,
        "m": 1.0,
        "km": 1000
    }

def get_conversion_factor(units):
    return conversion_factor_map.get(units)

def convert_between_units(distance, origin_unit, converted_unit):
    conversion_factor = get_conversion_factor(origin_unit) / get_conversion_factor(converted_unit)
    return round(distance * conversion_factor, 4)

def main():
    distance = float(input("Enter a distance: "))
    origin_unit = input("Enter the origin unit of measure ([in], [ft], [yd], [mi], [m], [km]): ").lower()
    converted_unit = input("Enter the unit to convert to ([in], [ft], [yd], [mi], [m], [km]): ").lower()
    
    # Convert a distance from a selected unit of measure into another
    converted_distance = convert_between_units(distance, origin_unit, converted_unit)

    print(f"{distance}{origin_unit} is {converted_distance}{converted_unit}\n")

    pass


main()
