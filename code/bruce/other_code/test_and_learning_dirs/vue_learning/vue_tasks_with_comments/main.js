
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

            // // This won't work properly since it's a reference to single instance. It will only create new references to that original instance.
            // this.taskList.push(this.newTask)

            // Need to do it this way.
            this.taskList.push({
                // This is pushing the values of each identifier to a new object to be added to 'taskList'.
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
            // task.isCompleted = task.isCompleted ? false : true
        },

        deleteTask: function(task) {
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

        // Using anonymous function:
        // completedTasks: function() {
        //     return this.taskList.filter(function(task) {
        //         return task.isCompleted
        //     })
        // },

        // Using arrow function:
        completedTasks: function() {
            return this.taskList.filter(task =>  task.isCompleted)
        },
    }
})