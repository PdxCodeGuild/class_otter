
let type_text = document.getElementById("type_text")

let add = document.getElementById("add")
let remove = document.getElementById("remove")
let complete = document.getElementById("complete")

let item_list = []
let completed = document.getElementById("completed_list")
let todo_data = []
let completed_data = []

add.addEventListener('click', function(){
    let last_node = document.createElement("li");
    let list_item = document.createTextNode(type_text.value);
    todo_data.push(type_text.value);
    last_node.appendChild(list_item);
    let complete = document.createElement("button");



    complete.innerHTML = "Complete";
    complete.addEventListener('click', function(){
        completed.appendChild(last_node)
        console.log(list_item)
        completed_data.push(list_item.nodeValue)
        console.log(completed_data)
        todo_data.splice(todo_data.indexOf(list_item.nodeValue), 1)
        complete.remove()
        localStorage.setItem('todo_data', JSON.stringify(todo_data))
        localStorage.setItem('completed_data', JSON.stringify(completed_data))
    })
    last_node.appendChild(complete);

    let remove = document.createElement("button");
    remove.innerHTML = "Remove";
    remove.addEventListener('click', function(){
        todo_data.splice(todo_data.indexOf(list_item.nodeValue), 1)
        completed_data.splice(completed_data.indexOf(list_item.nodeValue), 1)
        remove.parentElement.remove()
        })
    last_node.appendChild(remove);

    document.getElementById("item_list").appendChild(last_node);
// Now adding local storage info

    localStorage.setItem('todo_data', JSON.stringify(todo_data))
    localStorage.setItem('completed_data', JSON.stringify(completed_data))
})

// for (let i = 0; i < localStorage.length; i++){

// }


// completed.addEventListener('click', function(){
    
// })
