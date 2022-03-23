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
        selectedNumber: '',
        favoriteCountTrivia: '',
    },
    methods: {
        getTriviaForSelectedNumber: function() {
            this.getTrivia(this.selectedNumber);
        },
        getFavoriteCountTrivia: function() {
            let favoritesCount = 0;
            for (let i = 0; i < this.triviaList.length; i++) {
                if (this.triviaList[i].isFavorite) {
                    favoritesCount++;
                }
            }

            axios({
                method: 'get',
                url: `http://numbersapi.com/${favoritesCount}/trivia`,
            }).then((response) => {
                this.favoriteCountTrivia = response.data;
            }).catch(error => {
                console.log(error);
            });
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
                this.getFavoriteCountTrivia();
            }
        },
        remove: function(itemID) {
            let index = FindIndexByID(this.triviaList, itemID);
            if (index != -1) {
                this.triviaList.splice(index, 1);
                
                saveFavorites();
                this.getFavoriteCountTrivia();
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
        this.getFavoriteCountTrivia();
    }
});


Vue.component('trivia-item', {
    props: ['trivia'],
    template: `<div class="card container-background">
                    <div class="card-content">
                        <p>{{ trivia.text }}</p>
                        <a :class='["col s1 waves-effect waves-light btn green", trivia.isFavorite && "disabled"]' v-on:click="$emit(\'favorite\', trivia.id)"><i class="material-icons left">favorite</i></a>
                        <a class="col s1 waves-effect waves-light btn red" v-on:click="$emit(\'remove\', trivia.id)"><i class="material-icons left">delete_forever</i></a></li>
                    </div>
                </div>`
});

loadLocalStorage();

let canvas;
let context;
let font_size;
let drops;
let characters;
function backgroundCanvasLoop() {
    canvas = document.getElementById("backgroundCanvas");
    context = canvas.getContext("2d");

    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;

    characters = ['0', '1', ' '];

    font_size = 10;
    var columns = canvas.width / font_size;
    drops = [];
    
    for(var x = 0; x < columns; x++) {
        drops[x] = 1;
    }

    setInterval(draw, 33);
}

function draw()
{
    context.fillStyle = "rgba(64, 64, 64, 0.05)";
    context.fillRect(0, 0, canvas.width, canvas.height);
    
    context.fillStyle = "#0F0";
    context.font = font_size + "px arial";

    for(var i = 0; i < drops.length; i++)
    {
        var text = characters[Math.floor(Math.random() * characters.length)];
        context.fillText(text, i * font_size, drops[i] * font_size);
        
        if(drops[i] * font_size > canvas.height && Math.random() > 0.975) {
            drops[i] = 0;
        }
        
        drops[i]++;
    }
}

backgroundCanvasLoop();