let add = document.getElementById("add")
let remove = document.getElementById("remove")
let complete = document.getElementById("complete")
let todo = document.getElementById("todo")
let completed = document.getElementById("completed_list")
let type_text = document.getElementById("type_text")
let item_list = []



add.addEventListener('click', function(){
    let last_node = document.createElement("li");
    let list_item = document.createTextNode(type_text.value);
    last_node.appendChild(list_item);
    let complete = document.createElement("button");

    complete.innerHTML = "Complete";
    complete.addEventListener('click', function(){
        last_node.remove()
        completed.appendChild(last_node)
        complete.remove()
    })
    last_node.appendChild(complete);

    let remove = document.createElement("button");
    remove.innerHTML = "Remove";
    remove.addEventListener('click', function(){
        last_node.remove()
    })
    last_node.appendChild(remove);
    document.getElementById("item_list").appendChild(last_node);
})


// completed.addEventListener('click', function(){
    
// })
