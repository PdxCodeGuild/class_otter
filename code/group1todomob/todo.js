let completed = document.getElementById('completeList')
let incomplete = document.getElementById('incompleteList')
let i = 0
function addNewitem() {

    let newItem = document.getElementById("newListItem").value
    let listItem = document.createElement("li")
    listItem.innerHTML = `<button>Complete</button>${newItem}<button onclick='removeItem(this)'>Remove</button>`
    listItem.setAttribute('id', `list_item${i}`)
    i++
    incomplete.appendChild(listItem)
}

function removeItem(element) {
    element.parentElement.remove()

}