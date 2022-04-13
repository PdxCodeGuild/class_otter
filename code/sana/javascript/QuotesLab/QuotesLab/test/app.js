let vm = new Vue({
    el: '#app',
    data: {
        quoteResponse: {}
    },
    methods: {
        loadQuote: function() {
            axios({
                method: "get",
                url: "https://favqs.com/api/quotes",
                headers: {
                "Authorization": `Token token="4b3888849b4ef0bec9f217ffd39869a9"`
                },
            }).then(response => {
                this.quoteResponse = response.data;
            })
        }
    },
});