
var app4 = new Vue({
    el: '#app-4',
    data: {
        todos: [
            { text: 'Learn JavaScript', id: 1, complete: false },
            { text: 'Learn Vue', id: 2, complete: false },
            { text: 'Build something awesome', id: 3, complete: false }
        ],
        newText: "",
        completedList: [],
        nextId: 4,


    },

    methods: {
        create_todo: function () {
            this.todos.push(
                {
                    text: this.newText, id: this.nextId, complete: false,

                }
            )
            this.nextId += 1
        },

        completed: function (todo) {

            if (todo.complete === false) {

                console.log(`i am line 27 ${todo.complete}`)

                todo.complete = true

                console.log(`i am line 29 ${todo.complete}`)

                console.log(`i am completed before: ${this.elcompletedList}`)

                this.completedList.push(todo)

                console.log(`i am completed after: ${this.completedList}`)

                // this.todos.splice(0, 1);
                this.todos.splice(this.todos.indexOf(todo), 1);


            } else {
                todo.complete = false
            }

        },

        remove: function (remove) {

            this.todos.splice(remove, 1);

        }

    },




})
