const vm = new Vue({
    el: '#app',
    data: {
        results: {}
    },
    methods: {
        quotesbytag: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="4b3888849b4ef0bec9f217ffd39869a9"`
                },
                params: {
                    filter: "work",
                    type: "tag"
                }
            }).then(response => {
                this.results = response.data
            })
        },
        quotesbyauthor: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="4b3888849b4ef0bec9f217ffd39869a9"`
                },
                params: {
                    filter: "thomas edison",
                    type: "author"
                }
            }).then(response => {
                this.results = response.data
            })
        },
        quotesbykeyword: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="4b3888849b4ef0bec9f217ffd39869a9"`
                },
                params: {
                    filter: "work",
                    type: "keywords"
                }
            }).then(response => {
                this.results = response.data
            })
        }
    }
})