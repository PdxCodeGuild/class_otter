var app = new Vue({
    el: '#app',
    data: {
      todos: [
        {
          id: 1,
          text: "Buy milk",
          completed: true
        },
        {
          id: 2,
          text: "Clean the tables",
          completed: false
        },
      ],
      newTodo: "",
      id: 3,
    },

    computed: {
      incompleteTodos () {
        return this.todos.filter(todo => todo.completed === false)
      },
      completeTodos () {
        return this.todos.filter(todo => todo.completed === true)
      }
    },
    
    methods: {
      addTodos() {
        this.todos.push({
          id: this.id++,
          text: this.newTodo,
          completed: false,
        })
      },
      toggle(todo) {
        todo.completed = !todo.completed; 
      },
      deleteTodo(todo) {
        let id = this.todos.indexOf(todo)
        this.todos.splice(id, 1)
      }
    }
  })