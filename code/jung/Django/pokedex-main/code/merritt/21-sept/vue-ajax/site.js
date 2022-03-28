const vm = new Vue({
    el: '#app',
    data: {
        qotd: {},
        results: {}
    },
    methods: {
        loadQotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd'
            }).then(response => {
                this.qotd = response.data
            }).catch(console.log("error!"))
        },
        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes/',
                params: {
                    filter: 'abraham lincoln',
                    type: 'author'
                },
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                }
            }).then(response => this.results = response.data)
        }
    },
    created: function() {
        this.loadQotd()
    }
})