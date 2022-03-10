let completed = document.getElementById('completeList')
let incomplete = document.getElementById('incompleteList')
let i = 0
let itemList = []


function loadLocalData() {
    localData = JSON.parse(localStorage.getItem('todoItems'))
    
    for (const item in localData) {
        itemList.push(localData[item])
        
    }
}

loadLocalData()
console.log(localStorage)

function addNewitem() {
    let newItem = document.getElementById("newListItem").value
    let listItem = document.createElement("li")
    listItem.innerHTML = `<button onclick='completeItem(this)'>Complete</button>${newItem}<button onclick='removeItem(this)'>Remove</button>`
    listItem.setAttribute('id', `list_item${i}`)
    i++
    incomplete.appendChild(listItem)

    itemList.push([newItem, false])
    localStorage.setItem('todoItems', JSON.stringify(itemList))
}

function removeItem(element) {
    element.parentElement.remove()
}

function completeItem(element) {
    completed.appendChild(element.parentElement)
    element.disabled = 'disabled'
    element.parentElement.classList.add('marked')
}