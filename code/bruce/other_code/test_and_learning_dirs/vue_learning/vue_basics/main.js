
const app1 = new Vue({
    el: '#app1',
    data: {
        heading: 'GoodBuy, World!',
        timeLoaded: 'Page loaded at ' + new Date().toLocaleString(),
        elementSeen: true,
        newTodoText: '',
        uncompletedTodos: [
            { text: "Scrub the kittens"},
            { text: "phil fude bole"},
            { text: "Watch kittens play"},
            { text: "Scrub Bunbun"},
        ],
        completedTodos: [
            { text: "Pet Bunbun"},
            { text: "Make sure kittens don't starve"},
            { text: "Video tape the kittens"},
        ],
        somethingSaid: "I'm something said!",

        the: {
            userText: '',
        },
        userText: '',
        modelPlaceholder: "Type something here",
        counterOfClicks: 0,
        barPadding: 5,
        barSpacer: '-o-',
        barString: '',

        shoppingList: [
            { name: 'Car', selected: false },
            { name: 'Cat', selected: false },
            { name: 'Dog', selected: false },
            { name: 'Dew', selected: false },
        ]
    },
    methods: {
        reverseMessage: function() {
            this.somethingSaid = this.somethingSaid.split('').reverse().join('')
        },
        moveToRight: function() {
            this.barPadding += 1
            this.barString = this.barSpacer.repeat(this.barPadding)
        },
        moveToLeft: function() {
            if (this.barPadding >= 1) {
                this.barPadding -= 1
                this.barString = this.barSpacer.repeat(this.barPadding)
            } else {
                // Do nothing
            }
        },
        addTheTodo: function(newTodoText) {
            // Add 'newTodoText' to 'uncompletedTodos'.
            console.log(`Adding todo: ${newTodoText}`)
            // This line seems to add a 'key' to the 'todos'?
            this.uncompletedTodos.push({text: newTodoText, isCompleted: false})
            this.newTodoText = ''
        },
        completeTodo: function(todo, index) {
            console.log(`Completing: ${this.uncompletedTodos[index].text}`)
            console.log(`Completing: ${todo.text}`)
            this.uncompletedTodos.splice(index, 1)
            this.completedTodos.push(todo)
            // this.completedTodos.push(this.uncompletedTodos.splice(index, 1))
        },
        uncompleteTodo: function(todo, index) {
            console.log(`Uncompleting: ${this.completedTodos[index].text}`)
            console.log(`Uncompleting: ${todo.text}`)
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
    created: function() {
        // Do something
        this.barString = this.barSpacer.repeat(this.barPadding)
        console.log("We're created!")
    }
})

