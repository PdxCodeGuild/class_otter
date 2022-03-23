let idIncrementor = 0;


function loadLocalStorage() {
    idIncrementor = localStorage.getItem('idIncrementor');
    idIncrementor = (idIncrementor) ? idIncrementor : 0;

    let localFavorites = JSON.parse(localStorage.getItem('favorites'));
    if (localFavorites) {
        for (let i = 0; i < localFavorites.length; i++) {
            let item = localFavorites[i];
            triviaListApp.triviaList.push({
                id: item.id,
                text: item.text,
                isFavorite: item.isFavorite
            });
        }
    }
}

function saveFavorites() {
    favoritesList = [];
    for (let i = 0; i < triviaListApp.triviaList.length; i++) {
        if (triviaListApp.triviaList[i].isFavorite) {
            favoritesList.push(triviaListApp.triviaList[i]);
        }
    }

    localStorage.setItem('favorites', JSON.stringify(favoritesList));
}


function getID() {
    let nextID = idIncrementor;
    
    idIncrementor++;
    localStorage.setItem('idIncrementor', `${idIncrementor}`);

    return nextID;
}

function FindIndexByID(itemList, itemID) {
    let index = -1;
    for (let i = 0; i < itemList.length; i++) {
        if (itemList[i].id == itemID) {
            return i;
        }
    }

    console.log(`No item with id: ${itemID} found in item list.`);
    return index;
}


var triviaListApp = new Vue({
    el: '#triviaListApp',
    data: {
        triviaList: [],
        selectedNumber: ''
    },
    methods: {
        getTriviaForSelectedNumber: function() {
            this.getTrivia(this.selectedNumber);
        },
        getTrivia: function(numberForTrivia) {
            if (isNaN(parseInt(numberForTrivia))) {
                numberForTrivia = 'random';
            }
            
            axios({
                method: 'get',
                url: `http://numbersapi.com/${numberForTrivia}/trivia`,
            }).then((response) => {
                this.triviaList.push({
                    id: getID(),
                    text: response.data,
                    isfavorite: false
                });
            }).catch(error => {
                console.log(error);
            });
        },
        favorite: function(itemID) {
            let index = FindIndexByID(this.triviaList, itemID);
            if (index != -1) {
                //this.triviaList[index].isFavorite = true;
                
                // TODO: Figure out why this hack was needed
                let item = this.triviaList[index];
                item.isFavorite = true;
                this.triviaList.splice(index, 1);
                this.triviaList.push(item);
                
                saveFavorites();
            }
        },
        remove: function(itemID) {
            let index = FindIndexByID(this.triviaList, itemID);
            if (index != -1) {
                this.triviaList.splice(index, 1);
                saveFavorites();
            }
        }
    },
    computed: {
        newList: function() {
            newList = [];
            for (let i = 0; i < this.triviaList.length; i++) {
                if (!this.triviaList[i].isFavorite) {
                    newList.push(this.triviaList[i]);
                }
            }

            return newList;
        },
        favoritesList: function() {
            favoritesList = [];
            for (let i = 0; i < this.triviaList.length; i++) {
                if (this.triviaList[i].isFavorite) {
                    favoritesList.push(this.triviaList[i]);
                }
            }

            return favoritesList;
        }
    },
    created: function() {
        this.getTrivia('random');
    }
});


Vue.component('trivia-item', {
    props: ['trivia'],
    template: `<div class="card">
                    <div class="card-content">
                        <p>{{ trivia.text }}</p>
                        <a :class='["col s1 waves-effect waves-light btn green", trivia.isFavorite && "disabled"]' v-on:click="$emit(\'favorite\', trivia.id)"><i class="material-icons left">favorite</i></a>
                        <a class="col s1 waves-effect waves-light btn red" v-on:click="$emit(\'remove\', trivia.id)"><i class="material-icons left">delete_forever</i></a></li>
                    </div>
                </div>`
});

loadLocalStorage();