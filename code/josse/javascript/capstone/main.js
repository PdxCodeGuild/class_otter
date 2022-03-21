var app = new Vue({
    el: '#app',
    data: {
        books: {},
        userResults: {},
        userText: "",
        selectedType: ""


    },

    methods: {
        getBook: function () {
            axios({
                method: 'get',
                url: 'http://openlibrary.org/search.json',

            }).then(response => this.books = response.data)
        },


        userSearch: function () {
            let params = {}
            params[this.selectedType] = this.userText
            axios({
                method: 'get',
                url: 'http://openlibrary.org/search.json',
                params: params
            }).then(response => this.userResults = response.data)
        },
    },



    created: function () {
        this.userSearch()
    }

})