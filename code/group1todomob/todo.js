

let completed = document.getElementById('completeList')
let incomplete = document.getElementById('incompleteList')


let newItem = document.getElementById("newListItem").value
let listItem = document.createElement("li")
listItem.innerHTML = `<li><button>Complete</button>${newItem}<button>Remove</button></li>`
incomplete.appendChild(listItem)



