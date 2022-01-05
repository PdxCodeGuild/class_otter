#Ask the user for the distance in feet then convert to meters
units_in_meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'm': 1,
    'yd': 0.9144,
    'in': 0.0254
}
print("""please enter units of measurement as indicated below - \n
ft (feet)
mi (mile) 
km (kilometer)
m (meter)
yd (yard))
in (inch)""")
d = float(input("\nenter the 'distance':"))
u = input("\nEnter the input unit of distance: ")
o = input("\Enter the output unit of distance:")
total_distance = d * units_in_meters[u] / units_in_meters[o]
print(total_distance, o)

#U = input("\nEnter the unit of distance")