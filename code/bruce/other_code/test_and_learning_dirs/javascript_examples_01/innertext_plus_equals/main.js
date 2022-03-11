let elementToAddTextTo = document.querySelector('p')
let buttonToControlStuff = document.querySelector('button')

elementToAddTextTo.innerText = "#"

buttonToControlStuff.type = 'button'
buttonToControlStuff.innerText = 'Add a "#"!'

buttonToControlStuff.addEventListener('click', addAnotherPoundSignToText)

function addAnotherPoundSignToText() {
    elementToAddTextTo.innerText += "#"
}