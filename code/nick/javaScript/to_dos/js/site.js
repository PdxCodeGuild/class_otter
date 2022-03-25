var app = new Vue({
    el: '#app',
    data: {
        todos: [
            { id: 1, text: 'play games', completed: false },
            { id: 2, text: 'learn stuff', completed: false },
            { id: 3, text: 'take a nap', completed: false }
        ],
        computed: {
            incompleteTodos: function () {
                let incompleteTodos = []
                for (let i = 0; this.length; i++) {
                    if (!this.todos[i].completed === false) {
                        incompleteTodos.push(this.todos[i])
                    }
                }
                return incompleteTodos
            },
            completeTodo: function () {
                let completeTodos = []
                for (let i = 0; this.length; i++) {
                    if (!this.todos[i].completed === false) {
                        completeTodos.push(this.todos[i])
                    }
                }
                return completeTodos
            }
        }
    },
    methods: {
        addTodo: function () {
            this.todos.push({ text: this.newTodo, completed: false })
            this.newTodo = '';
        },
        deleteTodo: function (todos) {
            this.todos.splice(this.todos.indexOf(todos), 1);

        },
        completeTodo: function () {
            console.log('button works')
        }

    }

});
