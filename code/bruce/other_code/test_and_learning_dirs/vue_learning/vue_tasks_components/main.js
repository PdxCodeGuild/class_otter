

Vue.component('a-task', {
    data: function() {
        // This 'return' provides a brand new object when called.
        return {

        }
    },
    props: ['aTask'],
    template: `
    <p>
        <input v-model="aTask.isCompleted" type="checkbox" :id="aTask.id">
        <label :for="aTask.id">{{ aTask.id }} : {{ aTask.description }} : {{ aTask.isCompleted }}</label>
        <button v-on:click="toggleCompletion(aTask)">Toggle</button>
        <button v-on:click="deleteTask(aTask)">Delete</button>
    </p>
    `,
    methods: {
        deleteTask: function(aTask) {
            console.log(`Planning to remove: ${aTask.description}.`)
            this.$emit(`deleteComponentTask`)
        },

        toggleCompletion: function(aTask) {
            console.log(`Planning to toggle: ${aTask.description}.`)
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
            console.log(`We're toggling completion from ${task.isCompleted} to ${!task.isCompleted} : ${task.description}`)

            task.isCompleted = !task.isCompleted
        },

        deleteRootTask: function(task) {
            this.taskList.splice(this.taskList.indexOf(task), 1)
            console.log(`Successfully removed ${ task.description }: ${ this.taskList.indexOf(task) === -1 }`)

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