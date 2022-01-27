# TO BE CONTINUED

print ('\nVersion 1, 2, 3, & 4\n')

print ('\nWelcome to the Unit Converter!\n')

user_dist = input('\nWhat is the distance?\n')

user_unit = input('\nWhat are the units?\n')

user_out_unit = input('\nWhat are the output units?\n')

user_dist = int(user_dist)

convr_unit_m = {

    'in': .0254,
    'ft': .3048, 
    'yrd': .9144,
    'mi': 1609.34,
    'm':  1,
    'km': 1000
}

unit_scale = convr_unit_m[user_unit]


unit_convr = user_dist * unit_scale

unit_scale_out = convr_unit_m[user_out_unit]

m_convr_out = unit_convr / unit_scale_out

print (f'\n {user_dist} {user_unit} is {round(m_convr_out,2)} {user_out_unit} \n')

# TO BE CONTINUED.... 