const vm = new Vue({
    el: "#app",
    data: {
        quotes: {},
        results: {}
    },

    methods: {
        // this was calling for a single quote based on the api, now it should hopefully pull 25 random
        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => 
                this.quotes = response.data)
         },
        // this is calling for 25 quotes but is filtered by field and type
        loadLincoln: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: "abraham lincoln",
                    type: "author"
                },
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => this.results = response.data)
        }
    },

    created: function() {
        this.loadQuotes()
    }
})