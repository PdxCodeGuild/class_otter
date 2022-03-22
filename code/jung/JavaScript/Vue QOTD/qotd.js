const vm = new Vue({
    el: "#app",
    data: {
        qotd: {},
        quotes: [],
        previous: "",
        next: "",
        selected_choice: "",
        page: 1,
        choices: "",
        object: {}
    },

    methods: {
        getRandomQuote: function() {
            axios({
                method: "get",
                url: "https://favqs.com/api/qotd",
            }).then(response => this.qotd = response.data)
        },

        // Simplified
        getQuoteBy: function() {
            axios({
                method: "get",
                url: "https://favqs.com/api/quotes",
                params: {filter: this.choices, type: this.selected_choice, page: this.page},
                headers: {"Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`}
            }).then(response => {
                this.object = response.data
            })
        },

        // page
        previousPage: function() {
            this.page -= 1
            this.getQuoteBy()
        },

        nextPage: function() {
            this.page += 1
            this.getQuoteBy()
        },
    },
    
    created: function() {
        this.getRandomQuote()
    }

        // Original

        // getQuoteByKeyword: function() {
        //     axios({
        //         method: "get",
        //         url: "https://favqs.com/api/quotes",
        //         params: {filter: this.keyword, type: "keyword"},
        //         headers: {"Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`}
        //     }).then(response => this.quotes = response.data.quotes)
        // },

        // getQuoteByAuthor: function() {
        //     axios({
        //         method: "get",
        //         url: "https://favqs.com/api/quotes",
        //         params: {filter: this.author, type: "author"},
        //         headers: {"Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`}
        //     }).then(response => this.quotes = response.data.quotes)
        // },

        // getQuoteByTag: function() {
        //     axios({
        //         method: "get",
        //         url: "https://favqs.com/api/quotes",
        //         params: {filter: this.tag, type: "tag"},
        //         headers: {"Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`}
        //     }).then(response => this.quotes = response.data.quotes)
        // },
        ////////////////////////////////////////////////////////////////////////////////////

})