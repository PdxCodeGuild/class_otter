let inputText = document.getElementById('user_input')
let button = document.getElementById('button')
let outputDiv = document.getElementById('output-div');
let startUnits = document.getElementById('start_metric')
let endUnits = document.getElementById('end_metric')
let metrics = {

    "feet": 0.3048,
    "miles": 1609.34,
    "kilometers": 1000,
    "yard": 0.9144,
    "inch": 0.0254,
    "meter": 1
}
button.addEventListener("click", function () {
    console.log('hello world')
    let distance = inputText.value
    console.log(distance)
    let toMeters = distance * metrics[startUnits.value]
    console.log(`from units - ${startUnits.value}`)
    // console.log(textValue)

    let final = toMeters / metrics[endUnits.value]

    outputDiv.innerText = (`here is your converted number ${final} ${endUnits.value}`)
})


