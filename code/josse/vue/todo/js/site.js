
var app4 = new Vue({
    el: '#app-4',
    data: {
        todos: [
            { text: 'Learn JavaScript', id: 0, complete: false },
            { text: 'Learn Vue', id: 1, complete: false },
            { text: 'Build something awesome', id: 2, complete: false }
        ],
        new_text: "",
        completed_list: []


    },

    methods: {
        create_todo: function () {
            this.todos.push(
                {
                    text: this.new_text, id: this.todos.length, complete: false,

                }
            )

        },

        completed: function (todo) {

            if (todo.complete === false) {
                console.log(`i am line 27 ${todo.complete}`)
                todo.complete = true
                console.log(`i am line 29 ${todo.complete}`)
                console.log(`i am completed before: ${this.elcompleted_list}`)
                this.completed_list.push(todo)
                console.log(`i am completed after: ${this.completed_list}`)
                this.todos.splice(this.todos.indexOf(todo), 1);


            } else {
                todo.complete = false
            }

        },

        remove: function (index) {

            this.todos.splice(index, 1);

        }

    },




})
