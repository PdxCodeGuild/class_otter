// url, method, headers, params

// Component ideas:
    // search form section
    // a 'quote' component - This will allow me to decide and change the content of a quote in any of the areas of the page.
    // ???

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
            }).then((response) => {
                // Vue Object:
                // console.log(this)
                this.qotd = response.data

            //     /////// Optional Learning block //////
            //     // Response Object:
            //     // console.log(response)
            //     // Quote Object and other things:
            //     console.log(response.data)
            //     return this.qotd
            // }).then((payload) => {
            //     payload.quote.author = `Author used to be: ${payload.quote.author}`
            //     console.log(payload)
            //     ///////////////////////////////////////

            }).catch(error => {
                console.log(error.response.data)
            })
        },
        loadLincolnQuotes: function() {
            console.log(`Getting some Lincoln Quotes`)
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
            }).then((response) => {
                console.log("Response received")
                // console.log(response.data)
                // console.log(`Type of 'response.data': ${typeof response.data}`)
                this.results = response.data
                console.log("End Response")
                // console.log(`Type of 'typeof this.results': ${typeof this.results}`)
                // // object
                // console.log(`Type of 'typeof this.results.quotes': ${typeof this.results.quotes}`)
                // // object
                // // Returns one quote object.
                // console.log(this.results.quotes[0])
                console.log(this.results.quotes[0].author)
                console.log(this.results.quotes[0].body)
            }).catch(error => {
                console.log(error.response.data)
            })
        }
    },
    created: function() {
        this.loadQotd()
    }
})