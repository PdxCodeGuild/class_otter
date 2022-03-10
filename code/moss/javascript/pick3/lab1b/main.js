
alert('\nWelcome to the Unit Converter!\n')

// let user_dist = prompt('\nWhat is the distance?\n')
let distance = document.getElementById('user_dist')

// let user_unit = prompt('\nWhat are the units?\n')
let from_unit = document.getElementById('user_unit')

// let user_out_unit = prompt('\nWhat are the output units?\n')
let to_unit = document.getElementById('user_out_unit')

let button = document.getElementById('btn')

let convr_unit_m = {

    'in': .0254,
    'ft': .3048, 
    'yrd': .9144,
    'mi': 1609.34,
    'm':  1,
    'km': 1000
}

// let unit_scale = convr_unit_m[user_unit]

// let unit_convr = user_dist * unit_scale

// let unit_scale_out = convr_unit_m[user_out_unit]

// let m_convr_out = unit_convr / unit_scale_out
// let m_convr_out = document.getElementById('m_convr_out')

// let result = (`${user_dist} ${user_unit} is ${m_convr_out} ${user_out_unit}`)
let result = document.getElementById('result')

button.addEventListener('click', function(e) {
    
    let to_meters = distance.value * convr_unit_m[from_unit.value]

    let output = to_meters / convr_unit_m[to_unit.value]
    
    result.innerText = `${distance.value} ${from_unit.value} is ${output} ${to_unit.value}`
    console.log(result)
    console.log(distance)
})


// alert(result)

// console.log(result)