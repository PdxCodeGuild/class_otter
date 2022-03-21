
// 'a-task' in 'Vue.component()' matches '<a-task>' in index.html.
Vue.component('a-task', {
    data: function() {
        // This 'return' provides a brand new object when called.
        return {

        }
    },
    // props 'aaTask' (camelCase) matches with 'aa-task' (kebab-case) in `v-bind:aa-task="task"` in index.html.
    // props 'aaTask' (camelCase) matches with 'aaTask' (camelCase) in template below.
    // props 'aaTask' (camelCase) matches with 'aaTask' (camelCase) in component methods below.
    props: ['aaTask'],
    template: `
    <p>
        <input v-model="aaTask.isCompleted" type="checkbox" :id="aaTask.id">
        <label :for="aaTask.id">{{ aaTask.id }} : {{ aaTask.description }} : {{ aaTask.isCompleted }}</label>
        <button v-on:click="toggleCompletion(aaTask)">Toggle</button>
        <button v-on:click="deleteTask(aaTask)">Delete</button>
    </p>
    `,
    methods: {
        deleteTask: function(aaTask) {
            console.log(`Planning to remove: ${this.aaTask.description}.`)
            // Emit the event and send payload of 'aaTask'.
            // Multiple objects can be sent in payload. They will arrive as a 'params' array.
            // These seem to be positional parameters.
            // We can essentially send anything along with the event.
            this.$emit(`delete-component-task`, aaTask, "It's gonna be gone!")
        },
        
        toggleCompletion: function(aaTask) {
            console.log(`Planning to toggle: ${this.aaTask.description}.`)
            this.$emit(`toggle-component-task`, aaTask)
        }
    }
})


const vm = new Vue({
    el: "#app",
    data: {
        rootComponentGreeting: "Greetings, Earthling!",

        incompleteTaskHeading: "Incomplete Tasks:",
        completedTaskHeading: "Completed Tasks:",
        
        newTask: {
            id: 6,
            isCompleted: false,
            description: "",
        },

        taskList: [
            {id: 1, isCompleted: false, description: "Scrub some kittens!" },
            {id: 2, isCompleted: true, description: "Pet Bunbun!" },
            {id: 3, isCompleted: false, description: "Struggle Dezzi!" },
            {id: 4, isCompleted: false, description: "Butter the Cat!" },
            {id: 5, isCompleted: true, description: "Wag the Dog!" },
        ]
    },

    methods: {
        addTask: function() {
            this.taskList.push({
                id: this.newTask.id,
                isCompleted: this.newTask.isCompleted,
                description: this.newTask.description,
            })

            this.newTask.description = ""
            this.newTask.id++
        },

        toggleCompletion: function(task) {
            console.log(`Toggling: ${task.description}`)
            task.isCompleted = !task.isCompleted
        },

        deleteRootTask: function(task, payloadString) {
            // The emitted event's payload 'aaTask' is now referenced as 'task'.
            // The parameters are positional parameters.
            console.log(`Deleting: ${task.description}`)
            console.log(`Payload string: ${ payloadString }`)
            this.taskList.splice(this.taskList.indexOf(task), 1)
            console.log(`Deleted ${task.description}: ${this.taskList.indexOf(task) === -1}`)
        }
    },

    computed: {

        incompleteTasks: function() {
            return this.taskList.filter(function(task) {
                return !task.isCompleted
            })
        },

        completedTasks: function() {
            return this.taskList.filter(function(task) {
                return task.isCompleted
            })
        },

    }
})