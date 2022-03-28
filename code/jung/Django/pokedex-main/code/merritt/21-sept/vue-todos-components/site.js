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
        <input type="text" placeholder="stuff to do" v-model="text" @keyup.enter="addTodo">
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
        <button @click="editMode = editMode ? false : true">{{ editMode ? "Done" : "Edit" }}</button>
        <button @click="$emit('remove', todo)">×</button>
    </li>
    `,
    methods: {
        // removeTodo: function(todo) {
        //     this.$emit('remove', todo)
        // },
        // toggleEditMode: function() {
        //     this.editMode = this.editMode ? false : true
        // }
    },
    mounted: function() {
        console.log(`mounted ${this.todo.text}`)
    },
    destroyed: function() {
        console.log(`removed ${this.todo.text}`)
    }
})

new Vue({
    el: '#app',
    data: {
        todos: [
            {id: 1, text: "Wag the dog", completed: false},
            {id: 2, text: "Butter the cat", completed: true},
            {id: 3, text: "Pet the parrot", completed: false}
        ]
    },
    methods: {
        addTodo: function(payload) {
            this.todos.push(payload)
        },
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        // toggleTodo: function(todo) {
        //     todo.completed = todo.completed ? false : true
        // }
    },
    computed: {
        incompleteTodos: function() {
            // let incompleteTodos = []
            // for (let i=0; i<this.todos.length; i++) {
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
            // for (let i=0; i<this.todos.length; i++) {
            //     if (this.todos[i].completed) {
            //         completeTodos.push(this.todos[i])
            //     }
            // }
            // return completeTodos
            return this.todos.filter(function(todo) {
                return todo.completed
            })
        }
    }
})