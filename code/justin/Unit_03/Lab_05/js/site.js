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
    template: `<li class="row">
                <a :class='["col s1 waves-effect waves-light btn green", item.isCompleted && "disabled"]' v-on:click="item.isCompleted=true"><i class="material-icons left">done</i></a>
                <span class="col s10">{{ item.text }}</span>
                <a class="col s1 waves-effect waves-light btn red" v-on:click="$emit(\'remove\', item.id)"><i class="material-icons left">delete_forever</i></a></li>`
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
        todoList: []
    },
    methods: {
        remove: function(itemID) {
            let index = -1;
            for (let i = 0; i < this.todoList.length; i++) {
                if (this.todoList[i].id == itemID) {
                    index = i;
                    break;
                }
            }

            if (index != -1) {
                this.todoList.splice(index, 1);
            }
        }
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