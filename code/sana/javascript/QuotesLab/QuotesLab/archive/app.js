let vm = new Vue({
    el: '#app',
    data: {
        quoteResponse: {}
    },
    methods: {
        quotesbytag: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                // headers: {
                //     "Authorization": `Token token="4b3888849b4ef0bec9f217ffd39869a9"`
                // },
                params: {
                    filter: "work",
                    type: "tag"
                }
            }).then(response => {
                this.results = response.data
            })
        },
})