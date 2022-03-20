const vm = new Vue({
    el: "#app",
    data: {
        todos: [
            {id: 1, text: "Wag the dog", completed: true},
            {id: 2, text: "Butter the cat", completed: false},
            {id: 3, text: "Pick up the milk", completed: false}
        ],
        newTodo: {id: 4, text: "", completed: false}
    },
    computed: {
        incompleteTodos: function() {
            // let incompleteTodos = []
            // for (let i=0; i < this.todos.length; i++) {
            //     if (!this.todos[i].completed) {
            //         incompleteTodos.push(this.todos[i])
            //     }
            // }
            // return incompleteTodos
            return this.todos.filter(function(todo) {
                return !todo.completed
            })
        },
        completeTodos: function() {
            // let completeTodos = []
            // for (let i=0; i < this.todos.length; i++) {
            //     if (this.todos[i].completed) {
            //         completeTodos.push(this.todos[i])
            //     }
            // }
            // return completeTodos
            return this.todos.filter(function(todo) {
                return todo.completed
            })
        },
    },
    methods: {
        addTodo: function() {
            this.todos.push({
                id: this.newTodo.id,
                text: this.newTodo.text,
                completed: this.newTodo.completed
            })
            this.newTodo.id++
            this.newTodo.text = ""
        },
        toggleTodo: function(todo) {
            // if (todo.completed === true) {
            //     todo.completed = false
            // } else {
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