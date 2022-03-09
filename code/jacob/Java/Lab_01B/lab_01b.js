const newConvert = {ft: 0.3048, mi: 1609.34, m: 1, km: 1000, yd: 0.9144, in: 0.0254}

const metersConvert = {ft: 3.2808, mi: 0.00062137, m: 1, km: 0.001, yd: 1.0936, in: 39.37}


let processNumber = document.getElementById('process')
let results = document.getElementById('results')

processNumber.addEventListener('click', function(){
    
    
    let newDistance = parseFloat(document.getElementById('newDistance').value)
    let units = document.getElementById('units').value
    let convertTo = document.getElementById('convertTo').value

    let newConversion = newDistance * newConvert[units]
    let newOutput = newConversion * metersConvert[convertTo]
    
    results.innerText = (Math.round(newOutput*1000)/1000)

})
