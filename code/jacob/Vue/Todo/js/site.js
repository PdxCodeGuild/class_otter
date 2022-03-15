new Vue({
    el: '#app',
    data: {
        message: 'My Todo List',
        todos: [
            {id: 1, text: "Walk the dog", completed: false},
            {id: 2, text: "Wash the car", completed: false}
        ],
        newTodos: {id: 3, text: "", completed: false},
        
    },
    
    methods: {
        addTodo: function(){
            this.todos.push({
                id: this.newTodos.id,
                text: this.newTodos.text,
                completed: this.newTodos.completed
            })
            this.newTodos.id++
            this.newTodos.text=""
        },
        removeTodo: function(todo){
            this.todos.splice(this.todos.indexOf(todo), 1)
        },
        completed: function(todo){
            // todo.completed = !todo.completed     this is the short way to do:
            if (todo.completed === false){
                todo.completed = true
            }
            else{
                todo.completed = false
            }
        }
    },

    computed: {
        incomplete: function(){
            let undone = []
            for(let i=0; i<this.todos.length; i++){
                if (this.todos[i].completed === false){
                    undone.push(this.todos[i])
                    
                }
            }    
            return undone    
        },
        complete: function(){
            let done = []
            for(let i= 0; i<this.todos.length; i++){
                if (this.todos[i].completed === true){
                    done.push(this.todos[i])
                }
            }
            return done
        }
    }

})