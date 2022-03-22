Vue.component('add-a-todo', {
    data: function() {
        return {
            id: 6,
            text: "",
            completed: false
        }
    },
    template: `
        <div>
            <input type="text" placeholder="Todo description" v-model="text" @keyup.enter="addTodo">
            <button @click="addTodo">Add To List</button>
        </div>
    `,
    methods: {
        addTodo: function() {
            this.$emit('add-todo', {
                id: this.id,
                text: this.text,
                completed: this. completed
            })
            this.id++
            this.text = ""
        }
    }
})

// 'the-todo-li' matches with '<the-todo-li>' in index.html.
// The component name is kebab-case. The component name shows up in the <tag> in index.html.
Vue.component('the-todo-li', {
    data: function() {
        return {
            editMode: false
        }
    },
    // props can be camelCase (toDoo) which matches with kebab-case (to-doo) in index.html.
    // props 'toDoo' matches with 'to-doo' in `v-bind:to-doo="aTodoItem"` in index.html.
    // props 'toDoo' matches with 'toDoo' below in template.
    // props 'toDoo' matches with 'toDoo' below in 'mounted' and 'destroyed' methods.
    props: ['toDoo'],
    template: `
        <li>
            <input v-if="editMode" v-model="toDoo.text" type="text" v-on:keyup.enter="editMode = !editMode">
            <template v-else>{{ toDoo.text }}</template>
            <input type="checkbox" v-model="toDoo.completed">
            <button v-on:click="editMode = editMode ? false : true">{{ editMode ? "Save" : "Edit" }}</button>
            <button v-on:click="editMode = !editMode">{{ editMode ? "Save" : "Edit" }}</button>
            <button @click="toggleComponentTodo(toDoo)">Tog-Func</button>
            <button @click="$emit('toggle-item', toDoo)">Tog-Emit</button>
            <!-- Can use button two ways -->
            <!-- The '@click=' can have either: -->
            <!-- "removeTodo(toDoo)" | Calls 'this' component's removeTodo, which then emits. -->
            <!-- OR -->
            <!-- "$emit('remove-item', toDoo)" | Which directly emits. -->
            <button @click="removeTodo(toDoo)">Del-Func</button>
            <button @click="$emit('remove-item', toDoo)">Del-Emit</button>
        </li>
    `,
    methods: {
        removeTodo: function(todo) {
            console.log(`Removing: ${todo.text} - ${todo.id}`)
            this.$emit('remove-item', todo)
        },
        toggleComponentTodo: function(todo) {
            console.log(`Before Toggle: ${todo.text} - ${todo.completed}`)
            this.$emit('toggle-item', todo)
        }
    },
    mounted: function() {
        console.log(`mounted: ${this.toDoo.text}`)
    },
    destroyed: function() {
        console.log(`destroyed: ${this.toDoo.text}`)
    },
})

const vm = new Vue({
    el: "#app",
    data: {
        todos: [
            {id: 1, text: "Wag the dog", completed: true},
            {id: 2, text: "Butter the cat", completed: false},
            {id: 3, text: "Burn out!", completed: true},
            {id: 4, text: "Fade away!", completed: false},
            {id: 5, text: "Rock OUT!", completed: false},
        ],
    },
    computed: {
        incompleteTodos: function() {
            return this.todos.filter(function(todo) {
                return !todo.completed
            })
        },
        completeTodos: function() {
            return this.todos.filter(function(todo) {
                return todo.completed
            })
        },
    },
    methods: {
        addTodo: function(payload) {
            this.todos.push(payload)
        },
        removeRootTodo: function(todo) {
            todo = this.todos.splice(this.todos.indexOf(todo), 1)
        },
        toggleRootTodo: function(todo) {
            todo.completed = !todo.completed
            console.log(`After Toggle: ${todo.text} - ${todo.completed}`)
        }
    }
})