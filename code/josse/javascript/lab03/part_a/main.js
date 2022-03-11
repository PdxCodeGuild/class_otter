let metrics = {

    "feet": 0.3048,
    "miles": 1609.34,
    "kilometers": 1000,
    "yard": 0.9144,
    "inch": 0.0254,
    "meter": 1
}

let distance = parseFloat(prompt("what is your distance? "))

let input_1 = prompt("pick input unit feet,miles,kilometers,yard or inch? ")

let output_1 = prompt("pick output unit feet,miles,kilometers,yard or inch? ")

let user = Number(distance) * metrics[input_1]

let answer = user / metrics[output_1]

alert(`here is your coversion: ${answer} ${output_1}`)