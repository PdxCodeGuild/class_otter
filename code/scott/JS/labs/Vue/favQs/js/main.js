Vue.component('quote-me', {
    data: function() {
        return {
            filter: "",
            type: ""
        }
    },
    template: `
        <div>
        <h3>Enter your search text below..</h3>
        <input type="type" placeholder="Enter Search Text Here" @keyup.enter="getQuote" v-model="filter">
        <h3>Now select from the options below how you would like to search..</h3>
        <select v-model="type">
        <option disabled value="">Please select one</option>
        <option>author</option>
        <option>keyword</option>
        <option>tag</option>
        </select>
        <h3>If everything is correct, click below!</h3>
            <button @click="getQuote">Get Quote</button>
        </div>
        `,
    methods: {
        getQuote: function() {
            this.$emit('quote', {type: this.type, filter: this.filter})
            this.filter = ""
            this.type = ""
        }
    }
})

const vm = new Vue({
    el: '#app',
    data: {
        quotes: [],
        filter: "",
        type: "",
        results: {}
    },
    methods: {
        quoteMe: function(options) {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="9da63a2761237f4747b2e83ecad6e91a"`
                },
                params: {
                    filter: options.filter,
                    type: options.type,
                }
            }).then(response => {
                this.results = response.data
            })
        },
    }
})