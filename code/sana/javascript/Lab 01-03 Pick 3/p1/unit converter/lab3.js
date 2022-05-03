let distance = prompt('distance?')
let input = prompt('input units? (in, ft, , yd, mi, m, km)')
let output = prompt('output units? (in, ft, , yd, mi, m, km)')
let response = 0
let final = 0



if (input == 'in') {
    response += distance * .0254
}  else if (input == 'ft') {
    response += distance * .3048
} else if (input == 'yd') {
    response += distance * .9144
} else if (input == 'mi') {
    response += distance * 1609.34
} else if (input == 'm') {
    response += distance * 1
} else if (input == 'km') {
    response += distance * 1000
}
if (output == 'm') {
    final += response 
} else if (output == 'km') {
    final += response / 1000
} else if (output == 'mi') {
    final += response / 1609.34
} else if (output == 'yd') {
    final += response / .9144
} else if (output == 'ft') {
    final += response / .3048
} else if (output == 'in') {
    final += response / .0254
}
alert(distance + input + ' is ' + final + output)