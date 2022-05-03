let input = document.getElementById('input');
let convert = document.getElementById('convert');
let inches = document.getElementById('in');
let feet = document.getElementById('ft');
let miles = document.getElementById('mi');
let yards = document.getElementById('yd');
let meters = document.getElementById('m');
let kilometers = document.getElementById('km');
let cinches = document.getElementById('cin');
let cfeet = document.getElementById('cft');
let cyards = document.getElementById('cyd');
let cmiles = document.getElementById('cmi');
let cmeters = document.getElementById('cm');
let ckilometers = document.getElementById('ckm');


let converted = document.getElementById('converted');
let units = document.getElementById('units');
let nunits = document.getElementById('nunits');


let answer = 0;
let response = 0;

convert.addEventListener('click', function() {
    if (units.value === 'ft') {
        answer += parseFloat(input.value) * .3048
    } else if (units.value === 'yd') {
        answer += parseFloat(input.value) * .9144
    } else if (units.value === 'mi') {
        answer += parseFloat(input.value) * 1609.34
    } else if (units.value === 'in') {
        answer += parseFloat(input.value) * .0254
    } else if (units.value === 'm') {
        answer += parseFloat(input.value)
    } else if (units.value === 'km') {
        answer += parseFloat(input.value) * 1000
    }

    if (nunits.value === 'mi') {
        response += answer / 1609.34
    } else if (nunits.value === 'yd') {
        response += answer / .9144
    } else if (nunits.value === 'ft') {
        response += answer / .3048
    } else if (nunits.value === 'in') {
        response += answer / .0254
    } else if (nunits.value === 'km') {
        response += answer / 1000
    } else if (nunits.value === 'm') {
        response += answer
    }
    converted.innerText = `${input.value}${units.value} is ${response}${nunits.value}`
})