const vm = new Vue({
    el: '#app',
    data: {
        todos: [
            {id: 1, text: 'do taxes', completed: false },
            {id: 2, text: 'go to the grocery store', completed: false },
            {id: 3, text: 'make coffee', completed:true}
        ],
        newtodo: {id: 4, text: "", completed: false},
    },

    methods: {
        add_todo: function() {
            this.todos.push({ 
                id: this.newtodo.id, 
                text: this.newtodo.text, 
                completed: this.newtodo.completed 
            })
            this.newtodo.id++
            this.newtodo.text = ""
        },

        delete_todo: function (todos) {
            this.todos.splice(this.todos.indexOf(todos), 1);
        },
    }
})
