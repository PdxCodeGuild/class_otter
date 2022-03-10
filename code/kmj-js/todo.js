let add = document.getElementById("add")
let remove = document.getElementById("remove")
let complete = document.getElementById("complete")
let todo = document.getElementById("todo")
let completed = document.getElementById("completed")
let type_text = document.getElementById("type_text")


add.addEventListener('click', function(){
    todo.innerText += type_text.value

    
})

remove.addEventListener('click', function(){
    todo.remove()
})

// completed.addEventListener('click', function(){
    
// })
