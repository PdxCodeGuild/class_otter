var searchQuotesApp = new Vue({
    el: '#searchQuotesApp',
    data: {
        searchText: '',
        searchType: 'keyword'
    },
    methods: {
        searchForQuotes: function() {
            // TODO: search for quote with this.searchText and this.searchType
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.searchText,
                    type: this.searchType
                },
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then((response) => {
                quotesListApp.currentPage = response.data.page;
                
                if (response.data.last_page && quotesListApp.currentPage == 1) {
                    quotesListApp.shouldPaginate = false;
                }
                else
                {
                    quotesListApp.shouldPaginate = true;
                }

                quotesListApp.quotes.length = 0;
                let resultsLength = response.data.quotes.length;
                
                for (let i = 0; i < resultsLength; i++) {
                    quotesListApp.quotes.push(response.data.quotes[i]);
                }
            });
        }
    }
});

var quotesListApp = new Vue({
    el: '#quotesListApp',
    data: {
        quotes: [],
        shouldPaginate: false,
        currentPage: 1
    },
    methods: {
        loadRandomQuotes: function() {
            for (var i = 0; i < 5; i++)
            {
                getRandomQuote(this);   
            }
        }
    },
    created: function() {
        this.loadRandomQuotes();
    }
});

function getRandomQuote(app) {
    axios({
        method: 'get',
        url: 'https://favqs.com/api/qotd',
    }).then((response) => {
        app.quotes.push(response.data.quote);
    }).catch(error => {
        // TODO: handle error
        console.log(error);
    });
}