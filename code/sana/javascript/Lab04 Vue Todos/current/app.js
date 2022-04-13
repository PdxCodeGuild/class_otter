new Vue({
    el: '#tasklist',
    data() {
        return {
            tasks: [
            {name: 'Tuesday: go to the store'},
            {name: 'Wednesday : buy apples'},
            {name: 'Thursday: but oranges'},
        ]
        }
},
methods: {
    newTask: function() {
        if(!this.tasks.name) {
            return
        }
        this.tasks.push ({
            name: this.tasks.name,
            del: ''

        });
        this.tasks.name = "";
    },
    delTask: function (task) {
        this.tasks.splice(this.tasks.indexOf(task), 1)
    }
}
})