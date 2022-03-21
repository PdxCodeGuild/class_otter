// Build a Vue application that allows a user to search for quotes on FavQs.

// Requirements:

// Your app must use Vue to fetch data and interact with the results.
// Let the user enter a search term and select whether to search by keyword, author, or tag.
// Implement pagination buttons when the search returns more than 25 quotes.
// When the page first loads, show the user a set of completely random quotes.
// You must have at least one Vue component in your app.

var app = new Vue({
    el: '#app',
    data: {
        quote: {},
        results: {},
        userText: "",
        selectedType: "",
        pageSelected: 1,
        // isthisShown: false
    },
    methods: {
        getQuote: function () {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => this.quote = response.data)
        },
        nextPage: function () {
            this.pageSelected++
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
                params: {
                    filter: this.userText,
                    type: this.selectedType,
                    page: this.results.page + 1

                }
            }).then(response => this.results = response.data)

            this.results.page

        },
        lastPage: function () {
            this.pageSelected--
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
                params: {
                    filter: this.userText,
                    type: this.selectedType,
                    page: this.results.page - 1

                }
            }).then(response => this.results = response.data)

        },

        userQuote: function () {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                },
                params: {
                    filter: this.userText,
                    type: this.selectedType,
                    page: this.results.page + 1

                }
            }).then(response => this.results = response.data)

        }
    },

    created: function () {
        this.getQuote()
    }
})