const vm = new Vue({
    el: "#app",
    message: "hello world",
    data: {
        todos: [
            {
                id: 1, text: "wag the dog", completed: true
            },
            {
                id: 2, text: "butter kity", completed: false
            },
            {
                id:3, text: "milk", completed: false
            }

        ],
        // newText: "", 
        // newId: 4
        NewTodo :{id:4, newText: "", completed:false}

    },
    computed: {
        incompleteTodos: function() {
            // let incompleteTodos = []
            // for (let i=0; i<this.todo.length; i++) {
            //     if (!this.todos[i].completed === false) {
            //         incompleteTodos.push(this.todos[i])
            //     }
            // }
            // return incompleteTodos
            return this.todos.filter(function(todo){
                return !todo.completed
            })
        },
    
        completeTodos: function() {
            // let completeTodos = []
            // for (let i=0; i<this.todo.length; i++) {
            //     if (!this.todos[i].completed === true) {
            //         completeTodos.push(this.todos[i])
            //     }
            // }
            // return completeTodos
            return this.todos.filter(function(todo){
                return todo.completed
            })
        },
    },
    methods: {
        addTodo: function() {
            // console.log("adding todo")
            // this.todos.push(this.newTodo)
            this.todos.push(
                {
                    id: this.NewTodo.id,
                    text: this.newtodo.text,
                    completed: this.newTodo.completed
                }
            )
            this.newTodo.id++
            this.newTodo.text = ""
        },
        toggleTodo: function(todo) {
            // if (todo.completed === true) {
            //     todo.completed = false
            // }
            // else {
            //     todo.completed = true
            // }
            // todo.completed = todo.completed ? false : true
            todo.completed = !todo.completed
        
        },
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        }
    }     
})

