# version 1
#feet=float(input('How many feet? '))
#m=feet*0.3048
#print(feet, 'ft is equal to ', m, 'meters')
# version 1
# version 2
#distance=float(input('What is the distance? '))
#unit=input('What is the unit? (ft, m, mi, km) ' )
#d_ft=distance*0.3048
#d_m=distance
#d_mi=distance*1609.34
#d_km=distance*1000
#if unit=='ft':
#    print(distance, 'ft is ',d_ft ,'m')
#if unit=='m':
#    print(distance, 'm is ',distance ,'m')
#if unit=='mi':
#    print(distance, 'mi is ',d_mi ,'m')
#if unit=='km':
#    print(distance, 'km is ',d_km , 'm')
#version 2
#version 3
distance=float(input('What is the distance? '))
unit=input('What is the unit? (ft, m, mi, km, yd, in) ' )
d_ft=distance*0.3048
d_m=distance
d_mi=distance*1609.34
d_km=distance*1000
d_yd=distance*0.9144
d_in=distance*0.0254
if unit=='ft':
    print(distance, 'ft is ',d_ft ,'m')
if unit=='m':
    print(distance, 'm is ',distance ,'m')
if unit=='mi':
    print(distance, 'mi is ',d_mi ,'m')
if unit=='km':
    print(distance, 'km is ',d_km ,'m')
if unit=='yd':
    print(distance, 'yd is ',d_yd ,'m')
if unit=='in':
    print(distance, 'in is ',d_in , 'm')
#version 3