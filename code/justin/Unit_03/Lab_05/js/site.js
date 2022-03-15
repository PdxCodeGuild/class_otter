var addItemApp = new Vue({
    el: '#addItemApp',
    data: {
        newItemText: ''
    }
})

Vue.component('todo-item', {
    props: ['item'],
    template: '<li><button>Complete</button>{{ item.text }}<button>Remove</button></li>'
})

var todoListApp = new Vue({
    el: '#todoListApp',
    data: {
        todoList: [
            { id: 0, text: 'Learn JavaScript', isCompleted: false },
            { id: 1, text: 'Learn Vue', isCompleted: false },
            { id: 2, text: 'Build something awesome', isCompleted: false }
          ]
    },
    computed: {
        incompleteItems: function() {
            incompleteList = [];
            for (let i = 0; i < this.todoList.length; i++) {
                if (!this.todoList[i].isCompleted) {
                    incompleteList.push(this.todoList[i]);
                }
            }

            return incompleteList;
        },
        completeItems: function() {
            completeList = [];
            for (let i = 0; i < this.todoList.length; i++) {
                if (this.todoList[i].isCompleted) {
                    completeList.push(this.todoList[i]);
                }
            }

            return completeList;
        }
    }
})