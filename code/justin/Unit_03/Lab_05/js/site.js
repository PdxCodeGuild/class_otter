let idIncrementor = 0;
function GetTodoID() {
    let nextID = idIncrementor;
    
    idIncrementor++;
    localStorage.setItem('idIncrementor', `${idIncrementor}`);

    return nextID;
}

function LoadLocalData() {
    idIncrementor = localStorage.getItem('idIncrementor');
    idIncrementor = (idIncrementor) ? idIncrementor : 0;

    let localTodoItems = JSON.parse(localStorage.getItem('todoItems'));
    if (localTodoItems) {
        for (let i = 0; i < localTodoItems.length; i++) {
            let todoItem = localTodoItems[i];
            todoListApp.todoList.push({
                id: todoItem.id,
                text: todoItem.text,
                isCompleted: todoItem.isCompleted
            });
        }
    }
}

function FindIndexByID(itemList, itemID) {
    let index = -1;
    for (let i = 0; i < itemList.length; i++) {
        if (itemList[i].id == itemID) {
            return i;
        }
    }

    console.log(`No item with id: ${itemID} found in todoList.`);
    return index;
}


var addItemApp = new Vue({
    el: '#addItemApp',
    data: {
        newItemText: ''
    },
    methods: {
        addNewItem: function() {
            todoListApp.todoList.push({
                id: GetTodoID(),
                text: addItemApp.newItemText,
                isCompleted: false
            });
            localStorage.setItem('todoItems', JSON.stringify(todoListApp.todoList));
        }
    }
})

Vue.component('todo-item', {
    props: ['item'],
    template: `<li class="row">
                <a :class='["col s1 waves-effect waves-light btn green", item.isCompleted && "disabled"]' v-on:click="$emit(\'complete\', item.id)"><i class="material-icons left">done</i></a>
                <span class="col s10">{{ item.text }}</span>
                <a class="col s1 waves-effect waves-light btn red" v-on:click="$emit(\'remove\', item.id)"><i class="material-icons left">delete_forever</i></a></li>`
})

var todoListApp = new Vue({
    el: '#todoListApp',
    data: {
        todoList: []
    },
    methods: {
        complete: function(itemID) {
            let index = FindIndexByID(this.todoList, itemID);
            if (index != -1) {
                this.todoList[index].isCompleted = true;
                localStorage.setItem('todoItems', JSON.stringify(this.todoList));
            }
        },
        remove: function(itemID) {
            let index = FindIndexByID(this.todoList, itemID);
            if (index != -1) {
                this.todoList.splice(index, 1);
                localStorage.setItem('todoItems', JSON.stringify(this.todoList));
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




LoadLocalData();
