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
#distance=float(input('What is the distance? '))
#unit=input('What is the unit? (ft, m, mi, km, yd, in) ' )
#d_ft=distance*0.3048
#d_m=distance
#d_mi=distance*1609.34
#d_km=distance*1000
#d_yd=distance*0.9144
#d_in=distance*0.0254
#if unit=='ft':
#    print(distance, 'ft is ',d_ft ,'m')
#if unit=='m':
#    print(distance, 'm is ',distance ,'m')
#if unit=='mi':
#    print(distance, 'mi is ',d_mi ,'m')
#if unit=='km':
#    print(distance, 'km is ',d_km ,'m')
#if unit=='yd':
#    print(distance, 'yd is ',d_yd ,'m')
#if unit=='in':
#    print(distance, 'in is ',d_in , 'm')
#version 3
#version 4
distance=float(input('What is the distance? '))
unit=input('What is the input unit? (ft, m, mi, km, yd, in) ' )
o_unit=input('What is the output unit? (ft, m, mi, km, yd, in) ' )
d_ft=distance*0.3048
d_m=distance
d_mi=distance*1609.34
d_km=distance*1000
d_yd=distance*0.9144
d_in=distance*0.0254
o_dft=d_ft/0.3048
o_dm=d_m
o_dmi=d_mi/1609.34
o_dkm=d_km/1000
o_dyd=d_yd/0.9144
o_din=d_in/0.0254
if o_unit=='ft':
    print(distance, unit, 'is ',o_dft ,'ft')
if o_unit=='m':
    print(distance, unit, 'is ',o_dm ,'m')
if o_unit=='mi':
    print(distance, unit, 'is ',o_dmi ,'mi')
if o_unit=='km':
    print(distance, unit, 'is ',o_dkm ,'km')
if o_unit=='yd':
    print(distance, unit, 'is ',o_dyd ,'yd')
if o_unit=='in':
    print(distance, unit, 'is ',o_din , 'in')
