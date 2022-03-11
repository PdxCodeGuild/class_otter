// Assignment:
// https://github.com/PdxCodeGuild/class_otter/blob/bruce/4%20JavaScript/mob/04%20Todo%20List.md

let pageHeader = document.createElement('h1')
pageHeader.innerText = "Scott, Josse, and Bruce's Awesome ToDo and Task List"

let inputElementLabel = document.createElement('label')
inputElementLabel.innerText = "Add a new task: "
let inputBox = document.createElement('input')
inputBox.placeholder = "Enter task here"
let todoAddButton = document.createElement('button')
todoAddButton.innerText = "Add the Task"
todoAddButton.addEventListener('click', addTodoToList)

let uncompletedListHeading = document.createElement('h2')
uncompletedListHeading.innerText = 'Uncompleted Items'
let uncompletedListUl = document.createElement('ul')
uncompletedListUl.id = 'uncompleted-list'

let completedListHeading = document.createElement('h2')
completedListHeading.innerText = 'Completed Items'
let completedListUl = document.createElement('ul')
completedListUl.id = 'completed-list'


// These 'appendChild' add the HTML elements, created above, to the <body> of the HTML rendered in the browser.
document.body.appendChild(pageHeader)
document.body.appendChild(inputElementLabel)
document.body.appendChild(inputBox)
document.body.appendChild(todoAddButton)
document.body.appendChild(uncompletedListHeading)
document.body.appendChild(uncompletedListUl)
document.body.appendChild(completedListHeading)
document.body.appendChild(completedListUl)


function addTodoToList() {
    let listItem = document.createElement('li')
    uncompletedListUl.appendChild(listItem)
    task = inputBox.value

    let taskTextSpan = document.createElement('span')
    taskTextSpan.innerText = task
    
    completeButton = createCompleteButton()
    deleteButton = createDeleteButton()
    
    listItem.appendChild(taskTextSpan)
    listItem.appendChild(completeButton)
    listItem.appendChild(deleteButton)
}


function completeItem() {
    elementToComplete = this.parentElement

    let task = elementToComplete.firstChild.innerText
    /////////
    task = `<s>${task}</s>`
    elementToComplete.firstChild.innerHTML = task
    /////////
    // let taskStrikeThrough = document.createElement('s')
    // taskStrikeThrough.innerText = task
    // elementToComplete.firstChild.firstChild.replaceWith(taskStrikeThrough)
    /////////

    uncompleteButton = createUncompleteButton()
    elementToComplete.appendChild(uncompleteButton)

    // Remove 'this' (the complete button).
    this.remove()
    
    completedListUl.appendChild(elementToComplete)
}


function unCompleteItem() {
    elementToUncomplete = this.parentElement
    let task = elementToUncomplete.firstChild.innerText

    elementToUncomplete.firstChild.innerText = task

    completeButton = createCompleteButton()
    elementToUncomplete.firstChild.after(completeButton)

    // Remove 'this' (the uncomplete button).
    this.remove()
    
    uncompletedListUl.appendChild(elementToUncomplete)
}


function deleteItem() {
    // Remove the whole task <li> (which is the parent element of 'this').
    // So, 'this' (being a child element of <li>) is removed as well.
    this.parentElement.remove()
}


function createCompleteButton() {
    let completeButton = document.createElement('button')
    completeButton.innerText = "Complete the item"
    completeButton.addEventListener('click', completeItem)
    return completeButton
}


function createUncompleteButton() {
    let uncompleteButton = document.createElement('button')
    uncompleteButton.innerText = "Uncomplete the item"
    uncompleteButton.addEventListener('click', unCompleteItem)
    return uncompleteButton
}


function createDeleteButton() {
    let deleteButton = document.createElement('button')
    deleteButton.innerText = "Delete the item"
    deleteButton.addEventListener('click', deleteItem)
    return deleteButton
}
