metrics ={
    'ft': 0.3048, 'mi': 1609.34, 'm': 1, 'km': 1000
    }

metrics['yd'] = 0.9144 
metrics['in'] = .0254

user_distance = float(input('what is the distance? '))
units = input('what are the units the distance is in? ')

print(f'{metrics[units] * user_distance} m.')
print(metrics)