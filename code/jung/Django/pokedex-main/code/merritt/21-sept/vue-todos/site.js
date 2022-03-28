new Vue({
    el: '#app',
    data: {
        todos: [
            {id: 1, text: "Wag the dog", completed: false},
            {id: 2, text: "Butter the cat", completed: true},
            {id: 3, text: "Pet the parrot", completed: false}
        ],
        newTodo:  {id: 4, text: "", completed: false}
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
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        // toggleTodo: function(todo) {
        //     todo.completed = todo.completed ? false : true
        // }
    },
    computed: {
        incompleteTodos: function() {
            // let incompleteTodos = []
            // for (let i=0; i<this.todos.length; i++) {
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
            // for (let i=0; i<this.todos.length; i++) {
            //     if (this.todos[i].completed) {
            //         completeTodos.push(this.todos[i])
            //     }
            // }
            // return completeTodos
            return this.todos.filter(function(todo) {
                return todo.completed
            })
        }
    }
})