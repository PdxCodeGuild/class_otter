// Assignment:
// https://github.com/PdxCodeGuild/class_otter/blob/bruce/4%20JavaScript/mob/04%20Todo%20List.md

// Let's make a simple todo-list which supports the following operations:

// add an item to the list - done 
// remove an item from the list - done
// mark an item as completed - done 
// Removed items should disappear entirely. - done
// Completed items should appear at the bottom (or in a separate list) with a line through them.

// This is going to be put inside the <header> and we are going to give it  text of 'ToDo List'.
let pageHeader = document.createElement('h1')

// Label element for input box.
let inputElementLabel = document.createElement('label')
// Input box element.
let inputBox = document.createElement('input')
// Button to execute the add todo function.
let todoAddButton = document.createElement('button')

// Uncompleted Items.
let uncompletedListheading = document.createElement('h2')
uncompletedListheading.innerText = 'Uncompleted Items'
let uncompletedListUl = document.createElement('ul')
uncompletedListUl.id = 'uncompleted-list'

// Completed Items.
let completedListheading = document.createElement('h2')
completedListheading.innerText = 'Completed Items'
let completedListUl = document.createElement('ul')
completedListUl.id = 'completed-list'

// Add the add-new-task elements to body.
document.body.appendChild(inputElementLabel)
document.body.appendChild(inputBox)
document.body.appendChild(todoAddButton)
inputBox.placeholder = "Enter task here"

// Add the uncompleted and completed list headings and uls to the body.
document.body.appendChild(uncompletedListheading)
document.body.appendChild(uncompletedListUl)
document.body.appendChild(completedListheading)
document.body.appendChild(completedListUl)

// Add an event listener on the add button.
todoAddButton.addEventListener('click', addTodoToList)
todoAddButton.innerText = "Add a Task"


////////////////
// addTodoToList()
////////////////
function addTodoToList(event) {
    let listItem = document.createElement('li')
    // Add this <li> inside the <ul>
    uncompletedListUl.appendChild(listItem)
    // uncompletedListUl.prepend(listItem)
    task = inputBox.value

    let justTheTask = document.createElement('span')
    justTheTask.innerText = task

    let completeButton = document.createElement('button')
    completeButton.addEventListener('click', completeItem)
    completeButton.innerText = "Complete the item"

    let deleteButton = document.createElement('button')
    deleteButton.addEventListener('click', deleteItem)
    deleteButton.innerText = "Delete the item"


    listItem.appendChild(justTheTask)
    listItem.appendChild(completeButton)
    listItem.appendChild(deleteButton)
}


// function completeItem() {
//     let elementToComplete = this.parentElement
//     task = elementToComplete.firstChild.innerText
//     console.log(`${task}`)
    
//     let lineItem = document.createElement('li')
//     lineItem.innerHTML = `<s>${task}</s>`

//     let deleteButton = document.createElement('button')
//     deleteButton.innerText = "Delete the item"
//     deleteButton.addEventListener('click', deleteItem)

//     let uncompleteButton = document.createElement('button')
//     uncompleteButton.innerText = "Uncomplete an item"
//     uncompleteButton.addEventListener('click', unCompleteItem)
//     lineItem.appendChild(uncompleteButton)

//     lineItem.appendChild(deleteButton)
//     completedListUl.appendChild(lineItem)

//     // this.parentElement.remove()
// }



function completeItem() {
    // Flag to specify if we are printing the console log lines to console.log.
    let doConsoleLog = false
    // let doConsoleLog = true

    // LOGIC AND FUNCTIONALITY
    // Get the task text (innerText) of the '<span>' (firstChild) element and assign it an 'identifier' (task).
    let task = this.parentElement.firstChild.innerText
    

    // 'this' is the complete button.
    pleaseConsoleLog(`this: ${this}`, doConsoleLog)
    // this: [object HTMLButtonElement]
    pleaseConsoleLog(`this.innerText: ${this.innerText}`, doConsoleLog)
    // this.innerText: Complete the item
    pleaseConsoleLog(`this.parentElement: ${this.parentElement}`, doConsoleLog)
    // this.parentElement: [object HTMLLIElement]
    pleaseConsoleLog(`this.parentElement.firstChild: ${this.parentElement.firstChild}`, doConsoleLog)
    // this.parentElement.firstChild: [object HTMLSpanElement]
    pleaseConsoleLog(`task: ${task}`, doConsoleLog)
    // task: t
    pleaseConsoleLog(`Before assignment text: ${this.parentElement.firstChild.innerText}`, doConsoleLog)


    // LOGIC AND FUNCTIONALITY
    // Wrap the previous 'task' with '<s></s>' and assign that new string to 'task'.
    task = `<s>${task}</s>`
    // Set the 'innerHTML' of the <span> element 'firstChild' to 'task'.
    this.parentElement.firstChild.innerHTML = task


    // The complete button is the 'nextElementSibling' of the task '<span>' 'firstChild'.
    pleaseConsoleLog(`Should be the 'innerText' of the 'complete' button: ${this.parentElement.firstChild.nextElementSibling.innerText}`, doConsoleLog)
    // Should be the 'innerText' of the 'complete' button: Complete the item
    pleaseConsoleLog(`After assignment text: ${this.parentElement.firstChild.innerText}`, doConsoleLog)
    // After assignment text: tttt
    pleaseConsoleLog(`After assignment html: ${this.parentElement.firstChild.innerHTML}`, doConsoleLog)
    // After assignment html: <s>tttt</s>
    pleaseConsoleLog(`Parent innerHTML: ${this.parentElement.innerHTML}`, doConsoleLog)
    // Parent innerHTML: <span><s>tttt</s></span><button>Complete the item</button><button>Delete the item</button>
    

    // LOGIC AND FUNCTIONALITY
    // Assign 'this.parentElement' (the parent list item element) to 'elementToMove' so we can add it to the completed list.
    elementToMove = this.parentElement
    // Can we add an 'uncomplete' button to 'elementToMove'?
    let uncompleteButton = document.createElement('button')
    uncompleteButton.innerText = "Uncomplete an item"
    uncompleteButton.addEventListener('click', unCompleteItem)
    elementToMove.appendChild(uncompleteButton)
    // Remove the complete button since we are moving the whole task 'li' element to the completed list.
    // Remember, from above, 'this' IS the complete button.
    // Magically, '' removes the complete button from the 'li' element even though we have assigned a variable to the 'li'.
    this.remove()

    // completedListUl.appendChild(this.parentElement)
    completedListUl.appendChild(elementToMove)
}


function unCompleteItem() {
    // Flag to specify if we are printing the console log lines to console.log.
    // let doConsoleLog = false
    let doConsoleLog = true


    elementToMove = this.parentElement
    // This line gets the 'TEXT' inside the '<s>TEXT</s>' in the <span>.
    let task = elementToMove.firstChild.innerText


    pleaseConsoleLog(`Before replacing <s>TEXT</s> with TEXT - firstChild: ${elementToMove.firstChild}`, doConsoleLog)
    pleaseConsoleLog(`Before replacing <s>TEXT</s> with TEXT - innerHTML: ${elementToMove.firstChild.innerHTML}`, doConsoleLog)
    pleaseConsoleLog(`Before replacing <s>TEXT</s> with TEXT - innerText: ${elementToMove.firstChild.innerText}`, doConsoleLog)


    // This line replaces the '<s>TEXT</s>' in the <span> with 'TEXT'.
    elementToMove.firstChild.innerText = task


    pleaseConsoleLog(`After replacing <s>TEXT</s> with TEXT - firstChild: ${elementToMove.firstChild}`, doConsoleLog)
    pleaseConsoleLog(`After replacing <s>TEXT</s> with TEXT - innerHTML: ${elementToMove.firstChild.innerHTML}`, doConsoleLog)
    pleaseConsoleLog(`After replacing <s>TEXT</s> with TEXT - innerText: ${elementToMove.firstChild.innerText}`, doConsoleLog)


    let completeButton = document.createElement('button')
    completeButton.addEventListener('click', completeItem)
    completeButton.innerText = "Complete the item"
    // Add the 'complete' button immediately after the task text element.
    this.parentElement.firstChild.after(completeButton)
    // Remove the 'uncomplete' button.
    this.remove()
    // Add the 'li' element to the 'ul'.
    uncompletedListUl.appendChild(elementToMove)
}


function deleteItem() {
    // Flag to specify if we are printing the console log lines to console.log.
    let doConsoleLog = false
    // let doConsoleLog = true

    pleaseConsoleLog(`typeof this: ${typeof this}`, doConsoleLog)
    // typeof this: object
    pleaseConsoleLog(`this: ${this}`, doConsoleLog)
    // this: [object HTMLButtonElement]
    pleaseConsoleLog(`this.innerText: ${this.innerText}`, doConsoleLog)
    // this.innerText: Delete the item

    pleaseConsoleLog(`typeof this.parentElement: ${typeof this.parentElement}`, doConsoleLog)
    // typeof this.parentElement: object
    pleaseConsoleLog(`this.parentElement: ${this.parentElement}`, doConsoleLog)
    // this.parentElement: [object HTMLLIElement]
    pleaseConsoleLog(`this.parentElement.innerText: ${this.parentElement.innerText}`, doConsoleLog)
    // this.parentElement.innerText: ttttComplete the itemDelete the item
    pleaseConsoleLog(`this.parentElement.innerHTML: ${this.parentElement.innerHTML}`, doConsoleLog)
    // this.parentElement.innerHTML: <span>tttt</span><button>Complete the item</button><button>Delete the item</button>


    pleaseConsoleLog(`Deleting: ${this.parentElement.firstChild.innerText}`, doConsoleLog)
    // Deleting: [object HTMLLIElement]

    // This is the only line where logic/functionality occurs in this function 'deleteItem'.
    this.parentElement.remove()


    pleaseConsoleLog(`Deleted: ${this.parentElement.firstChild.innerText}`, doConsoleLog)
    // Deleted: [object HTMLLIElement]
}


// Function to print strings to console.log when second parameter is 'true'.
function pleaseConsoleLog(thingToPrint, defaultPrint=true) {
    if (defaultPrint == true) {
        console.log(thingToPrint)
    }
}
