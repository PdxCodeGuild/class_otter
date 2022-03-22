const app = Vue.createApp({ // in vue3, no 'el' option (we'll define that later)
    data: function() { // in vue3, data must be a function even in the root component
        return {
            todos: [
                {id: 1, text: "Wag the dog", completed: true},
                {id: 2, text: "Butter the cat", completed: false},
                {id: 3, text: "Pick up the milk", completed: false}
            ]
        }
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
        addTodo: function(payload) {
            this.todos.push(payload)
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

app.component('add-todo', { // in vue3, components need to be defined
                            // AFTER the root component and they use
                            // '<nameofappvariable>.component()' instead
                            // of 'Vue.component()'
    data: function() {
        return {
            id: 4,
            text: "",
            completed: false
        }
    },
    template: `
        <div>
            <input type="text" placeholder="add a todo" v-model="text" @keyup.enter="addTodo">
            <button @click="addTodo">Add To List</button>
        </div>
    `,
    methods: {
        addTodo: function() {
            this.$emit('add', {
                id: this.id,
                text: this.text,
                completed: this.completed
            })
            this.id++
            this.text = ""
        }
    }
})

app.component('todo-item', { // in vue3, components need to be defined
                             // AFTER the root component and they use
                             // '<nameofappvariable>.component()' instead
                             // of 'Vue.component()'
    data: function() {
        return {
            editMode: false
        }
    },
    props: ['todo'],
    template: `
        <li>
            <input v-if="editMode" type="text" v-model="todo.text">
            <template v-else>{{ todo.text }}</template>
            <input type="checkbox" v-model="todo.completed">
            <!-- <button @click="$emit('toggle', todo)">✔</button> -->
            <button @click="editMode = !editMode">{{ editMode ? "Done" : "Edit" }}</button>
            <button @click="$emit('remove', todo)">×</button>
        </li>
    `,
    methods: {
        removeTodo: function(todo) {
            this.$emit('remove', todo)
        },
        toggleTodo: function(todo) {
            this.$emit('toggle', todo)
        }
    },
    mounted: function() {
        console.log(`mounted ${this.todo.text}`)
    },
    destroyed: function() {
        console.log(`removed ${this.todo.text}`)
    }
})

app.mount('#app') // in vue3, mount the app to your HTML after defining
                  // the root app instance and all of your components.
                  // this replaces the 'el' option in the root component
                  // options object.


// There are of course many other small changes between vue2 and vue3,
// and extra options for larger and more complicated projects. That said,
// the above example shows the basic syntax changes between defining and
// mounting a vue2 and vue3 app. Notice that I didn't actually have to
// change anything inside my components themselves, and only made minor
// modifications to my root instance.