let completed = document.getElementById('completeList')
let incomplete = document.getElementById('incompleteList')
let uniqueIDIncrementor = 0
let itemList


function loadLocalData() {
    localData = JSON.parse(localStorage.getItem('todoItems'))

    if (localStorage.getItem('uniqueIDIncrementor'))
    {
        uniqueIDIncrementor = parseInt(localStorage.getItem('uniqueIDIncrementor'))
    }

    if (localStorage.getItem('todoItems')) {
        itemList = JSON.parse(localStorage.getItem('todoItems'))

        for (const item in localData) {
            let listItem = document.createElement("li")
            listItem.setAttribute('id', `list_item${localData[item][0]}`)
            if (!localData[item][2])
            {
                listItem.innerHTML = `<a class="btn waves-effect waves-light green" onclick='completeItem(this)'><i class="material-icons left">done</i></a>${localData[item][1]}<a class="btn waves-effect waves-light red" onclick='removeItem(this)'><i class="material-icons left">clear</i></a>`
                incomplete.appendChild(listItem)
            }
            else
            {
                listItem.innerHTML = `<a class="btn waves-effect waves-light green disabled" onclick='completeItem(this)'><i class="material-icons left">done</i></a>${localData[item][1]}<a class="btn waves-effect waves-light red" onclick='removeItem(this)'><i class="material-icons left">clear</i></a>`
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
    listItem.innerHTML = `<a class="btn waves-effect waves-light green" onclick='completeItem(this)'><i class="material-icons left">done</i></a>${newItem}<a class="btn waves-effect waves-light red" onclick='removeItem(this)'><i class="material-icons left">clear</i></a>`
    listItem.setAttribute('id', `list_item${uniqueIDIncrementor}`)
    incomplete.appendChild(listItem)

    itemList.push([uniqueIDIncrementor, newItem, false])
    localStorage.setItem('todoItems', JSON.stringify(itemList))

    uniqueIDIncrementor++
    localStorage.setItem('uniqueIDIncrementor', `${uniqueIDIncrementor}`)
}

function removeItem(element) {
    id = parseInt(element.parentElement.id.replace('list_item', ''))
    for (let index = 0; index < itemList.length; index++) {
        if (itemList[index][0] === id) {
            itemList.splice(index, 1)
            break
        }
    }

    localStorage.setItem('todoItems', JSON.stringify(itemList))
    element.parentElement.remove()
}

function completeItem(element) {
    element.classList.add('disabled')
    element.parentElement.classList.add('marked')
    
    completed.appendChild(element.parentElement)

    id = parseInt(element.parentElement.id.replace('list_item', ''))
    for (let index = 0; index < itemList.length; index++) {
        if (itemList[index][0] === id) {
            itemList[index][2] = true
            break
        }
    }

    localStorage.setItem('todoItems', JSON.stringify(itemList))
}