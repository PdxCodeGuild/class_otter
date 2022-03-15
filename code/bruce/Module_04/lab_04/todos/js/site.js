// Resources:
// https://v2.vuejs.org/v2/guide/
// Avoid 'if' and 'for' in same element:
// https://v2.vuejs.org/v2/style-guide/#Avoid-v-if-with-v-for-essential
// Vue API:
// https://v2.vuejs.org/v2/api/
// List Rendering:
// https://v2.vuejs.org/v2/guide/list.html
// Event Handling:
// https://v2.vuejs.org/v2/guide/events.html
// Form Input Bindings:
// https://v2.vuejs.org/v2/guide/forms.html

const app1 = new Vue({
    el: '#app',
    data: {
        contentHeading: 'The ToDos',
        uncompletedTodosHeading: 'Uncompleted ToDos',
        completedTodosHeading: 'Completed ToDos',
        newTodoText: '',
        uncompletedTodos: [
            { text: "Scrub the kittens", isCompleted: false},
            { text: "phil fude bole", isCompleted: false},
            { text: "Watch kittens play", isCompleted: false},
            { text: "Scrub Bunbun", isCompleted: false},
        ],
        completedTodos: [
            { text: "Pet Bunbun", isCompleted: true},
            { text: "Make sure kittens don't starve", isCompleted: true},
            { text: "Video tape the kittens", isCompleted: true},
        ],
    },
    methods: {
        addTheTodo: function(newTodoText) {
            // Add 'newTodoText' to 'uncompletedTodos'.
            console.log(`Adding todo: ${newTodoText}`)
            // This line seems to add a 'key' to the 'todos'?
            this.uncompletedTodos.push({text: newTodoText, isCompleted: false})
        },
        completeTodo: function(todo, index) {
            console.log(`Completing: ${this.uncompletedTodos[index].text}`)
            console.log(`Completing: ${todo.text}`)
            todo.isCompleted = true
            this.uncompletedTodos.splice(index, 1)
            this.completedTodos.push(todo)
            // this.completedTodos.push(this.uncompletedTodos.splice(index, 1))
        },
        uncompleteTodo: function(todo, index) {
            console.log(`Uncompleting: ${this.completedTodos[index].text}`)
            console.log(`Uncompleting: ${todo.text}`)
            todo.isCompleted = false
            this.completedTodos.splice(index, 1)
            this.uncompletedTodos.push(todo)
            // this.uncompletedTodos.push(this.completedTodos.splice(index, 1))
        },
        deleteUncompletedTodo: function(todo, index) {
            console.log(`Deleting: ${this.uncompletedTodos[index].text}`)
            console.log(`Deleting: ${todo.text}`)
            this.uncompletedTodos.splice(index, 1)
        },
        deleteCompletedTodo: function(todo, index) {
            console.log(`Deleting: ${this.completedTodos[index].text}`)
            console.log(`Deleting: ${todo.text}`)
            this.completedTodos.splice(index, 1)
        },
    },
})

