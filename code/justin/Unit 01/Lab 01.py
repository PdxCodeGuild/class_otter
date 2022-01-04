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

def convert_to_meters(distance, origin_unit):
    return round(distance * get_conversion_factor(origin_unit), 4)

def main():
    distance = float(input("Enter a distance: "))
    origin_unit = input("Enter a unit of measure ([in], [ft], [yd], [mi], [m], [km]): ").lower()
    
    # Convert a distance from a selected unit of measure into meters
    distance_in_meters = convert_to_meters(distance, origin_unit)

    print(f"{distance}{origin_unit} is {distance_in_meters}m\n")

    pass


main()
