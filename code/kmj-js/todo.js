let add = document.getElementById("add")
let remove = document.getElementById("remove")
let complete = document.getElementById("complete")
let todo = document.getElementById("todo")
let completed = document.getElementById("completed_list")
let type_text = document.getElementById("type_text")
let item_list = []



add.addEventListener('click', function(){
    node = document.createElement("li");
    list_item = document.createTextNode(type_text.value);
    node.appendChild(list_item);
    let complete = document.createElement("button");
    complete.innerHTML = "Complete";
    node.appendChild(complete);
    let remove = document.createElement("button");
    remove.innerHTML = "Remove";
    node.appendChild(remove);
    document.getElementById("item_list").appendChild(node);
})



remove.addEventListener('click', function(){
    todo.remove()
})

// completed.addEventListener('click', function(){
    
// })
