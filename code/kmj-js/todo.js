let add = document.getElementById("add")
let remove = document.getElementById("remove")
let complete = document.getElementById("complete")
let todo = document.getElementById("todo")
let completed = document.getElementById("completed")
let type_text = document.getElementById("type_text")
let todoList = []

add.addEventListener('click', function(){
    todoList.push(type_text.value)
    for(let item of todoList) {
        console.log(item)
        todo.innerText = item
    }
})

remove.addEventListener('click', function(){
    todo.remove()
})

// completed.addEventListener('click', function(){
    
// })
