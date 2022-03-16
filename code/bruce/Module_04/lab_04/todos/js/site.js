// Start server:
// python -m http.server
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
// Displaying Filtered/Sorted Results:
// https://v2.vuejs.org/v2/guide/list.html#Displaying-Filtered-Sorted-Results
// Array.prototype.filter()
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
// Array.prototype.push()
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push
// Array.prototype.splice()
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice
// Array.prototype.indexOf()
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf

const app1 = new Vue({
    el: '#app',
    data: {

        theBindStyle: 'left',
        mainButtonHeading: 'Button Interface for ToDos',
        uncompletedToDosHeading: 'Uncompleted ToDos',
        completedToDosHeading: 'Completed ToDos',
        newToDoText: '',

        checkboxHeading: 'Checkbox Interface for ToDos',
        checkboxTodosHeading: 'ToDos',
        nextId: 11,
        todos: [
            { text: "Get fuzzy!", isCompleted: false, id: 1},
            { text: "Scrub him!", isCompleted: false, id: 2},
            { text: "Make sure they're fed!", isCompleted: false, id: 3},
            { text: "Give em a comfy bed.", isCompleted: false, id: 4},
            { text: "Scrub the kittens", isCompleted: false, id: 5},
            { text: "Watch kittens play", isCompleted: false, id: 6},
            { text: "Scrub Dezzi", isCompleted: false, id: 7},
            { text: "Pet Bunbun", isCompleted: true, id: 8},
            { text: "Make sure kittens don't starve", isCompleted: true, id: 9},
            { text: "Video tape the kittens", isCompleted: true, id: 10},
        ],
    },
    methods: {
        // Functions for the button-operation part.
        addTheToDo: function(newToDoText) {
            console.log(`Adding todo: ${newToDoText}`)
            this.todos.push({text: newToDoText, isCompleted: false, id: this.nextId})
            console.log(`Length todos: ${this.todos.length}`)
            console.log(`Next ID: ${this.nextId}`)
            this.nextId++
            console.log(`Next ID: ${this.nextId}`)
            this.newToDoText = ''
        },
        completeToDo: function(todo) {
            console.log(`Completing: ${this.todos[this.todos.indexOf(todo)].text}`)
            console.log(`Completing: ${todo.text}`)
            todo.isCompleted = true
        },
        uncompleteToDo: function(todo) {
            console.log(`Uncompleting: ${this.todos[this.todos.indexOf(todo)].text}`)
            console.log(`Uncompleting: ${todo.text}`)
            todo.isCompleted = false
        },
        deleteToDo: function(todo) {
            console.log(`Deleting: ${this.todos[this.todos.indexOf(todo)].text}`)
            console.log(`Deleting: ${todo.text}`)
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
    },
    // 'computed' properties to sort the 'todos' by 'isComplete'.
    computed: {
        incompleteTodos: function () {
            // Return list of todos where isCompleted == false.
            return this.todos.filter(function(todo) {
                return todo.isCompleted === false
            })
        },
        completeTodos: function () {
            // Return list of todos where isCompleted == true.
            return this.todos.filter(function(todo) {
                return todo.isCompleted === true
            })
        },
      },
})

