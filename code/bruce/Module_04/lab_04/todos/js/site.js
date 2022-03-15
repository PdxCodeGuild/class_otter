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

const app1 = new Vue({
    el: '#app',
    data: {
        mainHeading: 'Button ToDos',
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

        checkboxHeading: 'Checkbox ToDos',
        checkboxTodosHeading: 'ToDos',
        newText: '',
        nextId: 5,
        todos: [
            { text: "Scrub the kittens", isCompleted: false, id: 5},
            { text: "phil fude bole", isCompleted: false, id: 6},
            { text: "Watch kittens play", isCompleted: false, id: 7},
            { text: "Scrub Bunbun", isCompleted: false, id: 8},
            { text: "Pet Bunbun", isCompleted: true, id: 9},
            { text: "Make sure kittens don't starve", isCompleted: true, id: 10},
            { text: "Video tape the kittens", isCompleted: true, id: 11},
            { text: "Get fuzzy!", isCompleted: false, id: 1},
            { text: "Scrub him!", isCompleted: false, id: 2},
            { text: "Make sure they're fed!", isCompleted: false, id: 3},
            { text: "Give em a comfy bed.", isCompleted: false, id: 4},
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

        addTodo: function(newText) {
            console.log(`Adding todo: ${newText}`)
            // this.todos.length()
            // Add 'newText' to 'todos'.
            this.todos.push({text: newText, isCompleted: false, id: this.nextId})
            console.log(`Next ID: ${this.nextId}`)
            // incrementNextId()
            this.nextId++
            console.log(`Next ID: ${this.nextId}`)
        },
        deleteTodo: function(todo) {
            console.log(`ToDo: ${todo}`)
            console.log(`ToDo Is Completed: ${todo.isCompleted}`)
            console.log(`ToDo ID: ${todo.id}`)
            console.log(`Deleting: ${todo.text}`)
            // Need to figure out how to delete the item with specific id.
            // We have an array. What are methods to modify arrays?
            // 
        },
    },
    computed: {
        // a computed getter
        incompleteTodos: function () {
            // Return list of todos where isCompleted == true.
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

