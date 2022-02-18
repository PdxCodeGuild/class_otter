#unit coverter dictionary
converter = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
    }
#function to run the conversion
def unit_converter(meters, unit):
    converted = meters * unit
    return converted
while True:
    distance = input("what is the distance in meters?: ")
    #got the distance from user
    if distance == 'done':
        break
    distance = int(distance)
    #ensured compatability with integers as int
    units = input("In what units should the distance be converted to? \n'ft' for feet \n'mi' for feet \n'm' for meters \n'km' for kilometer \n'yard' for yards \n'inch' for inches \nEnter the units: ")
    #get the requested units from user
    result = unit_converter(distance, converter[units])
    print(result)