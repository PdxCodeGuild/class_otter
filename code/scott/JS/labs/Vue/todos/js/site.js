const App = {
	data() {
		return {
			todos: [],
			newTodo: '',
		}
	},
	computed: {
		incompleteTodos() {
			return this.todos.filter(todo => todo.completed === false)
		},
		completedTodos() {
			return this.todos.filter(todo => todo.completed === true)
		}
	},
	methods: {
		addNewTodo() {
			this.todos.push({
				text: this.newTodo,
				completed: false
			})
			this.newTodo = ''
		},
		toggleComplete(todo) {
			todo.completed = !todo.completed
		},
		deleteTodo(todo) {
			const index = this.todos.indexOf(todo)
			this.todos.splice(index, 1)
		}
	}
}
Vue.createApp(App).mount('#app')