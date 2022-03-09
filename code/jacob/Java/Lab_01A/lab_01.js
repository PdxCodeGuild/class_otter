var newConvert = {ft: 0.3048, mi: 1609.34, m: 1, km: 1000, yd: 0.9144, in: 0.0254}
var new_distance = prompt("What is the distance?: ")
var units = prompt("What are the units?: ")

var newConversion = new_distance * newConvert[units]

var metersConvert = {ft: 3.2808, mi: 0.00062137, m: 1, km: 0.001, yd: 1.0936, in: 39.37}

var convertTo = prompt("What are the output units?: ")

var newOutput = newConversion * metersConvert[convertTo]
alert(Math.round(newOutput*1000)/1000)
alert('Hello World!')