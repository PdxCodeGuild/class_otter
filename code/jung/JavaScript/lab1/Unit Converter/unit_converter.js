

function conversion(input_unit, output_unit, distance) {
    if (input_unit === "ft"){
        let convert_to_meter = distance  * 0.3048;
        return convert_to_meter
    }
    else if (input_unit === "mi"){
        let convert_to_meter = distance  * 1609.34;
        return convert_to_meter
    }
    else if (input_unit === "m"){
        let convert_to_meter = distance  * 1;
        return convert_to_meter
    }
    else if (input_unit === "km"){
        let convert_to_meter = distance  * 1000;
        return convert_to_meter
    }
    
    if (output_unit === "ft") {
        let result = convert_to_meter / 0.3048;
        return result
    }
    else if (output_unit === "mi"){
        let result = convert_to_meter / 1609.34;
        return result
    }
    else if (output_unit === "m"){
        let result = convert_to_meter / 1;
        return result
    }
    else if (output_unit === "km"){
        let result = convert_to_meter / 1000;
        return result
    }
}

let distance = prompt("What is the distance? ");
let input_unit = prompt("What are the input units? ");
let output_unit = prompt("What are the output units? ");
let result = conversion(input_unit, output_unit, distance);
alert(distance + " " + input_unit + "= " + result + " " + output_unit)