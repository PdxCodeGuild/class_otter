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

    let deleteButton = document.createElement('button')
    deleteButton.addEventListener('click', deleteItem)

    completeButton.innerText = "Complete the item"
    deleteButton.innerText = "Delete the item"

    listItem.appendChild(justTheTask)
    listItem.appendChild(completeButton)
    listItem.appendChild(deleteButton)
}


function completeItem() {
    const elementToAppend = Object.create(this.parentElement)
    console.log(` element to append ${elementToAppend}`)
    let task = this.parentElement.firstChild.innerText
    console.log(`${task}!!`)
    console.log(`${task}`)
    let lineItem = document.createElement('li')
    lineItem.innerHTML = `<s>${task}</s>`

    let deleteButton = document.createElement('button')
    deleteButton.addEventListener('click', deleteItem)
    deleteButton.innerText = "Delete the item"
    lineItem.appendChild(deleteButton)
    completedListUl.appendChild(lineItem)

    this.parentElement.remove()
}


function deleteItem() {
    console.log(`typeof this: ${typeof this}`)
    console.log(`this: ${this}`)
    console.log(`this.innerText: ${this.innerText}`)

    console.log(`typeof this.parentElement: ${typeof this.parentElement}`)
    console.log(`this.parentElement: ${this.parentElement}`)
    console.log(`this.parentElement.innerText: ${this.parentElement.innerText}`)

    this.parentElement.remove()
    // this.remove()
    console.log('Deleted')
}