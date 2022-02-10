'''
*********************************************
*              PDXCode Guild                *
*  Full-Stack Python/JavaScript Day Class   *
*               Class_Otter                 *
*              Scott Madden                 *
*          Lab 01 - Unit Converter          *
*              04/month/2022                *
*                                           *
*********************************************
'''

#Ask the user for the distance in feet then convert to meters
units_in_meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'm': 1,
    'yd': 0.9144,
    'in': 0.0254
}
print("""please use the two letter abbreviation for the 
      units of measurement, as indicated below - \n
ft (feet)  
mi (mile) 
km (kilometer)
m (meter)
yd (yard))
in (inch)""")
# can lay out as selectable inputs, select your unkt of measurement, 
# the number of units to convert, the unit of measurement, 
# hit enter to return to a Gui display. Add a clear function, 
# and if possible, a query if they want to convert the 
# returned distance (Unit Of Meas and Num of Units) and logic 
# to handle converting the returned value to the new unit of measurement (LOOP)
# possibly modify some of the calculator structure to build a 
# convert-a-lator or incorporate the function into the original


# Need to build an 'if' statement with error handling 
# around the inputs
d = float(input("\nenter the 'distance':"))
u = input("\nEnter the input unit of distance: ")
o = input("\nEnter the output unit of distance:")
total_distance = d * units_in_meters[u] / units_in_meters[o]
print(total_distance, o)
