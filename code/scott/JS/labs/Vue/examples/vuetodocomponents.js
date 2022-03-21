Vue.component('add-todo', {
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

Vue.component('todo-item', {
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

const vm = new Vue({
    el: "#app",
    data: {
        todos: [
            {id: 1, text: "Wag the dog", completed: true},
            {id: 2, text: "Butter the cat", completed: false},
            {id: 3, text: "Pick up the milk", completed: false}
        ]
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