let num1 = document.getElementById('num1')
let p = document.getElementById('p')
let h1 = document.getElementById('title')
let num2 = document.getElementById('num2')
let calcBtn = document.getElementById('do-the-calc')
let results = document.getElementById('results')

p.innerText = "Goodbye world!"
p.addEventListener('click', function(){
    let button = document.createElement("button")
    button.innerText = "That tickles"
    button.addEventListener('click', function(){
        alert("Heehee!!!")
    })
    results.append(button)
})
p.classList.add("fancy")
// h1.innerHTML = `${h1.innerHTML}<p>More text here</p>`
let new_p = document.createElement('p')
new_p.innerText = "More text here"
h1.append(new_p)



num2.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        results.innerText = parseFloat(num1.value)+parseFloat(num2.value)+parseFloat(results.innerText)
    }
    console.log(event)
})