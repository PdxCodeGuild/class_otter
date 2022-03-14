new Vue({
    el: '#app',
    data: {
        message: 'My Todo List',
        todos: [
            {id: 1, text: "Walk the dog", completed: false},
            {id: 2, text: "Wash the car", completed: false}
        ],
        newTodos: {id: 3, text: "", completed: false}
    },
    
    methods: {
        addTodo: function(){
            this.todos.push({
                id: this.newTodos.id,
                text: this.newTodos.text,
                completed: this.newTodos.completed
            })
            this.newTodos.id++
            this.newTodos.text=""
        },
        removeTodo: function(todo){
            this.todos.splice(this.todos.indexOf(todo), 1)
        }
    }
})