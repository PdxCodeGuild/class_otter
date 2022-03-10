let distance = document.getElementById('number')
let input_unit = document.getElementById('input_unit')
let output_unit = document.getElementById('output_unit')
let getNums = document.getElementById("get_nums")
let result = document.getElementById("result")
let modalBtn = document.getElementById("modalBtn")


function conversion(input_unit, output_unit, distance) {
    let convert_to_meter

    if (input_unit === "ft"){
        convert_to_meter = distance * 0.3048;
    }
    else if (input_unit === "mi"){
        convert_to_meter = distance  * 1609.34;
    }
    else if (input_unit === "m"){
        convert_to_meter = distance  * 1;
    }
    else if (input_unit === "km"){
        convert_to_meter = distance  * 1000;
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


modalBtn.addEventListener('click', function(){
    if (distance.value === "") {
        modalBtn.innerText = "Put something!"
        setTimeout(function(){
            location.reload(1);
        }, 1000)
    }
    else {
        let answer = conversion(input_unit.value, output_unit.value, parseInt(distance.value))
        modalBtn.innerText = `${distance.value} ${input_unit.value} = ${answer} ${output_unit.value}`
        setTimeout(function(){
            location.reload(1);
        }, 10000)
    }
})

