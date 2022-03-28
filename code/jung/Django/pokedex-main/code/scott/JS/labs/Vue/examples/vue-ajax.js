const vm = new Vue({
    el: "#app",
    data: {
        qotd: {},
        results: {}
    },
    methods: {
        loadQotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd'
            }).then((response) => {
                this.qotd = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        loadQuotes: function() {
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
        this.loadQotd()
    }
})