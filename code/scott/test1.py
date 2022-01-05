# input distance to meters distance
def to_meters(distance, units):
    return distance * units_in_meters[units]

# meters to selected units distance
def from_meters(distance, units):
    return distance / units_in_meters[units]

units_in_meters = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'm': 1,
    'yd': 0.9144,
    'in': 0.0254
}