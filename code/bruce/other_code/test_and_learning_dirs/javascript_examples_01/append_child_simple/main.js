// 'theButton' is used to add stuff to the 'div'.
let theButton = document.querySelector('button')

// We're going to add stuff to the 'div'.
let theDiv = document.querySelector('div')

theButton.innerText = "Do something!"
theButton.addEventListener('click', doSomething)

function doSomething() {

    let theChild = document.createElement('p')
    theChild.innerText = "Paragraph"
    theDiv.appendChild(theChild)
}