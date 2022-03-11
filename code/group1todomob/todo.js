let completed = document.getElementById('completeList')
let incomplete = document.getElementById('incompleteList')
let i = 0
let itemList


function loadLocalData() {
    localData = JSON.parse(localStorage.getItem('todoItems'))
    if (localStorage.getItem('todoItems')) {
        itemList = JSON.parse(localStorage.getItem('todoItems'))

        for (const item in localData) {
            let listItem = document.createElement("li")
            listItem.setAttribute('id', `list_item${localData[item][0]}`)
            if (!localData[item][2])
            {
                listItem.innerHTML = `<button onclick='completeItem(this)'>Complete</button>${localData[item][1]}<button onclick='removeItem(this)'>Remove</button>`
                incomplete.appendChild(listItem)
            }
            else
            {
                listItem.innerHTML = `<button onclick='completeItem(this) disabled="disabled"'>Complete</button>${localData[item][1]}<button onclick='removeItem(this)'>Remove</button>`
                listItem.classList.add('marked')
                completed.appendChild(listItem)
            }
        }
    }
    else {
        itemList = []
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

    itemList.push([i, newItem, false])
    localStorage.setItem('todoItems', JSON.stringify(itemList))
}

function removeItem(element) {
    element.parentElement.remove()
}

function completeItem(element) {
    completed.appendChild(element.parentElement)
    element.disabled = 'disabled'
    element.parentElement.classList.add('marked')

    id = element.parentElement.id.replace('list_item', '')
    console.log(id)
    itemList[id][2] = true
    localStorage.setItem('todoItems', JSON.stringify(itemList))
}