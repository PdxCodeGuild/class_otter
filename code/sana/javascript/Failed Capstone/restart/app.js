let vm = new Vue({
    el: '#app',
    data: {
        quoteResponse: {}
    },
    methods: {
        loadQuote: function() {
            axios({
                method: "get",
                url: "https://api.kanye.rest/",
            }).then(response => {
                this.quoteResponse = response.data;
            })
        }
    },
});