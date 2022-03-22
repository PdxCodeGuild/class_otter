var app = new Vue({
    el: '#app',
    data: {
        todos: [
            { text: 'play games', completed: false },
            { text: 'learn stuff', completed: false },
            { text: 'take a nap', completed: false }
        ],
        newTodo: ''
    },
    methods: {
        addTodo: function () {
            this.todos.push({ text: this.newTodo, completed: false })
            this.newTodo = '';
        },
        deleteTodo: function (todos) {
            this.todos.splice(this.todos.indexOf(todos), 1);

        },

    }

});
