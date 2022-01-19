converter = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'inch': 0.0254
    }
#dictionary for meter
meter_convert = {
    'ft': float(1 / 0.3048),
    'mi': float(1 / 1609.34),
    'm': 1,
    'km': float(.001),
    'yard': float(1 / 0.9144),
    'inch': float(1/ 0.0254)
    }
#dictionary for meters
#function to run the conversion to meters
def meter_converter(input_units, distance):
    meter_converted = input_units * distance
    return meter_converted
#function to run conversion from meters
def unit_converter(output_units, distance):
    converted = distance * output_units
    return converted
while True:
    distance = input("What is the distance? or 'done' to quit: ")
    if distance == 'done':
        break
    input_units = input("What are the input units? \n'ft' for feet \n'mi' for feet \n'm' for meters \n'km' for kilometer \n'yard' for yards \n'inch' for inches \nEnter the units: ")
    #got the distance from user
    #got the input units
    #run function to convert into meters
    distance = float(distance)
    meter_result = meter_converter(distance, converter[input_units])
    #ensured compatability with integers as int
    output_units = input("What are the output units? \n'ft' for feet \n'mi' for feet \n'm' for meters \n'km' for kilometer \n'yard' for yards \n'inch' for inches \nEnter the units: ")
    #get the requested units from user to convert from meters
    result = unit_converter(meter_result, meter_convert[output_units])
    # print(meter_result)
    print(result)