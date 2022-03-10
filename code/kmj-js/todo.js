
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
        completed_data.push(type_text.value);
        last_node.remove()
        complete.remove()
        localStorage.removeItem(type_text.value);
    })
    last_node.appendChild(complete);

    let remove = document.createElement("button");
    remove.innerHTML = "Remove";
    remove.addEventListener('click', function(){
        last_node.remove()
        localStorage.removeItem(last_node);
    })
    last_node.appendChild(remove);

    document.getElementById("item_list").appendChild(last_node);
// Now adding local storage info

    localStorage.setItem('todo_data', JSON.stringify(todo_data))
    localStorage.setItem('completed_data', JSON.stringify(completed_data))
})


// completed.addEventListener('click', function(){
    
// })
