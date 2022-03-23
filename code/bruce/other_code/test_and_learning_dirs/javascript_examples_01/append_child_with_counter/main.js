// 'theButton' is used to add stuff to the 'div'.
let theButton = document.querySelector('button')

// We're going to add stuff to the 'div'.
let theDiv = document.querySelector('div')
    
theButton.innerText = "Add a 'p' element"
theButton.addEventListener('click', addParagraphElement)

function addParagraphElement() {
    // 'Declare' the 'identifier', 'theChild'.
    let theChild = document.createElement('p')
    // Append 'theChild' to the end of 'theDiv'.
    theDiv.appendChild(theChild)
    
    // Declare an identifier 'pNodeList' and assign it's value to the list of 'p' elements.
    pNodeList = document.getElementsByTagName('p')
    // Assign the length of 'pNodeList' to variable identifier 'pNodeCount'.
    pNodeCount = pNodeList.length
    
    // Create a text string to put in current 'p' element (theChild) and print to console.
    textString = "Paragraph: " + pNodeCount
    theChild.innerText = textString
    
    console.log(textString)
    // 'theDiv.childElementCount' returns the number of child elements of 'theDiv'.
    console.log("The <div> has " + theDiv.childElementCount + " elements in it.")
}

