// Assignment:
// https://github.com/PdxCodeGuild/class_otter/blob/bruce/4%20JavaScript/mob/04%20Todo%20List.md

// Let's make a simple todo-list which supports the following operations:

// add an item to the list
// remove an item from the list
// mark an item as completed
// Removed items should disappear entirely.
// Completed items should appear at the bottom (or in a separate list) with a line through them.

// <header> ToDo List

// This is the thing we're adding
// <label placeholder=''></label>
// <input>
// <button> Add todo - listener

// List of Todos
// Way to Complete and Remove for each item
// <ul>
// <li><buttonToComplete><buttonToRemove>

// Completed ToDo
// <ul>
// <li>

// This is going to be put inside the <header> and we are going to give it  text of 'ToDo List'.
let pageHeader = document.createElement('h1')

// Label for input box
let inputElementLabel = document.createElement('label')
// Input box
let inputBox = document.createElement('input')
// Button to execute script.
let todoAddButton = document.createElement('button')

// List of todos
let uncompletedListUl = document.createElement('ul')
uncompletedListUl.id = 'uncompleted-list'
// We create the items in a function. Function is being called by add button.
    // Create the <li>s.
    // let listItem = document.createElement('li')

let completedListUl = document.createElement('ul')
completedListUl.id = 'completed-list'



document.body.appendChild(inputElementLabel)
document.body.appendChild(inputBox)
document.body.appendChild(todoAddButton)

// Uncompleted and completed list elements.
document.body.appendChild(uncompletedListUl)
document.body.appendChild(completedListUl)

todoAddButton.addEventListener('click', addTodoToList)
todoAddButton.innerText = "Add a Task"

inputBox.placeholder = "Enter task here"

////////////////
// addTodoToList()
////////////////
function addTodoToList(event) {
    let listItem = document.createElement('li')
    // Add this <li> inside the <ul>
    uncompletedListUl.appendChild(listItem)
    // uncompletedListUl.prepend(listItem)
    // task = inputBox.value
    // listItem.innerText = task

    let completeButton = document.createElement('button')
    completeButton.addEventListener('click', completeItem)
    let deleteButton = document.createElement('button')
    deleteButton.addEventListener('click', deleteItem)

    completeButton.innerText = "Complete the item"

    deleteButton.innerText = "Delete the item"


    listItem.appendChild(completeButton)
    listItem.appendChild(deleteButton)

    console.log(listItem)
    console.log(listItem.id)
}


function completeItem() {
    console.log(this.parentElement)
    // Add the whole parent elemeni to the completed list.
    
    completedListUl.appendChild(this.parentElement)
    // Remove the whole parent element from the uncompleted list.
    this.parentElement.remove()
    // if item.delete is checked, 
    console.log(`Completed: ${this}`)
}


function deleteItem() {
    // Is there are way we can tell the remover which element this is in?

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