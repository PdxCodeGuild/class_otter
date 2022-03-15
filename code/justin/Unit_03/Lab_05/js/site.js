var addItemApp = new Vue({
    el: '#addItemApp',
    data: {
        newItemText: ''
    },
    methods: {
        addNewItem: function() {
            todoListApp.todoList.push({id: GetTodoID(), text: addItemApp.newItemText, isCompleted: false});
        }
    }
})

Vue.component('todo-item', {
    props: ['item'],
    template: '<li><button v-on:click="item.isCompleted=true">Complete</button>{{ item.text }}<button>Remove</button></li>'
})

let idIncrementor = 0;
function GetTodoID() {
    let nextID = idIncrementor;
    idIncrementor++;
    return nextID;
}

var todoListApp = new Vue({
    el: '#todoListApp',
    data: {
        todoList: [
            { id: GetTodoID(), text: 'Learn JavaScript', isCompleted: false },
            { id: GetTodoID(), text: 'Learn Vue', isCompleted: false },
            { id: GetTodoID(), text: 'Build something awesome', isCompleted: false }
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