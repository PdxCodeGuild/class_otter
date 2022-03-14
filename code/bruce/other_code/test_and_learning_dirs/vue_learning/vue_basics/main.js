
const app1 = new Vue({
    el: '#app1',
    data: {
        heading: 'GoodBuy, World!',
        timeLoaded: 'Page loaded at ' + new Date().toLocaleString(),
        elementSeen: true,
        todos: [
            { text: "Scrub the kittens", isCompleted: false},
            { text: "phil fude bole", isCompleted: false},
            { text: "Watch kittens play", isCompleted: false},
            { text: "Scrub Bunbun", isCompleted: false},
        ],
        somethingSaid: "I'm something said!",
        userText: '',
        modelPlaceholder: "Type something here",
        counterOfClicks: 0,
        barPadding: 5,
        barSpacer: '-o-',
        barString: '',
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
            this.barPadding -= 1
            this.barString = this.barSpacer.repeat(this.barPadding)
        },
        completeTodo: function(todo) {
            console.log(todo)
            console.log(`Completing: ${todo.text}`)
            todo.isCompleted = true
            console.log(`${todo.text} is completed: ${todo.isCompleted}`)
        },
        uncompleteTodo: function(todo) {
            console.log(todo)
            console.log(`Uncompleting: ${todo.text}`)
            todo.isCompleted = false
            console.log(`${todo.text} is completed: ${todo.isCompleted}`)
        },
    }
})

