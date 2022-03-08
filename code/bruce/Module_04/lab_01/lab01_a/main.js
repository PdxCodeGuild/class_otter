const conversion = {
    'in': 39370.08,
    'ft': 3280.84,
    'yd': 1093.613,
    'm' : 1000,
    'km': 1,
    'mi': .6213712
}


const units = {
    'in'    : 'in',
    'inch'  : 'in',
    '"'     : 'in',
    'ft'    : 'ft',
    'feet'  : 'ft',
    "'"     : 'ft',
    'yd'    : 'yd',
    'yard'  : 'yd',
    'm'     : 'm',
    'meter' : 'm',
    'km'    : 'km',
    'kilometer': 'km',
    'mi'    : 'mi',
    'mile'  : 'mi'
}


function consoleLogOrAlert(description, thingToSay) {
    let doAlert = true;

    if (doAlert) {
        window.alert(description + ': ' + thingToSay);
        console.log(description + ': ' + thingToSay);
    } else {
        console.log(description + ': ' + thingToSay);
    }
    return thingToSay;
}


function convertLength() {
    userLength = parseFloat(prompt("Please enter length:"));
    inputUnit = prompt("Input Units - (in/ft/yd/m/km/mi):");
    outputUnit = prompt("Output Units - (in/ft/yd/m/km/mi):");

    consoleLogOrAlert('Input Length', userLength);

    theActualInputUnit = units[inputUnit];
    consoleLogOrAlert('Input Units', theActualInputUnit);

    theActualOutputUnit = units[outputUnit];
    consoleLogOrAlert('Output Units', theActualOutputUnit);

    outputLength = userLength * conversion[theActualOutputUnit] / conversion[theActualInputUnit];

    consoleLogOrAlert('Results', userLength + ' ' + theActualInputUnit + ' is ' + outputLength + ' ' + theActualOutputUnit);
}