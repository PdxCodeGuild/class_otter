// url, method, headers, params

// Component ideas:
    // search form section
    // a 'quote' component - This will allow me to decide and change the content of a quote in any of the areas of the page.
    // ???

// Authors:
    // martin-luther-king-jr
    // maya angelou


Vue.component('quote-search', {
    data: function() {
        return {
            searchTypes: [
                'keyword',
                'author',
                'tag'
            ],
            searchType: '',
            searchTerm: '',
        }
    },
    template: `
        <div>
            <h2>Search for Quotes</h2>
            <label for="search-type">Search by: </label>
            <select v-model="searchType" name="search-type" id="search-type">
                <option disabled value=''>Select a search type</option>
                <option v-for="typeOption in this.searchTypes" v-bind:value="typeOption">{{ typeOption }}</option>
            </select>
            <input v-model="searchTerm" v-on:keyup.enter="submitComponentSearchRequest" placeholder="Search Term">
            <button @click="submitComponentSearchRequest">Search</button>
            <p>{{ searchType }}:{{ searchTerm }}</p>
        </div> 
    `,
    methods: {
        submitComponentSearchRequest: function() {
            console.log(`Emitting  ${this.searchType}:${this.searchTerm} search to root component!!!`)
            // console.log(`Search Type: ${this.searchType}`)
            // console.log(`Search Term: ${this.searchTerm}`)
            this.$emit('search-quotes', {
                type: this.searchType,
                term: this.searchTerm,
            })
        }
    }
})


Vue.component('quote-component', {
    data: function() {
        return {
        }
    },
    props: ['quoteComponent'],
    template: `
        <li>
            <p>{{ quoteComponent.body }}</p>
            <p><a :href="quoteComponent.url" target="_blank">{{ quoteComponent.author }}</a></p>
        </li>
    `,
})


const vm = new Vue({
    el: '#app',
    data: {
        qotd: {},
        token: `Token token="855df50978dc9afd6bf86579913c9f8b"`,
        results: {},
        searchType: '',
        searchTerm: '',
        displayedSearchTerm: '',
        currentPage: 1,
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
                    "Authorization": this.token
                }
            }).then((response) => {
                this.results = response.data
                this.displayedSearchTerm = this.results.quotes[0].author
            }).catch(error => {
                console.log(error.response.data)
            })
        },

        searchAndLoadQuotes: function(payload) {
            console.log(`Getting some ${payload.type}:${payload.term} Quotes`)
            this.displayedSearchTerm = payload.term
            this.searchType = payload.type
            if (payload.term === 'keyword') {
                payload.type = ''
            }
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: payload.term,
                    type: payload.type
                },
                headers: {
                    "Authorization": this.token
                }
            }).then((response) => {
                this.results = response.data
                if (payload.type === 'author') {
                    this.displayedSearchTerm = this.results.quotes[0].author
                }
            }).catch(error => {
                console.log(error.response.data)
            })
        },

        nextPage: function() {
            console.log("Go to next page!")
        },
        
        previousPage: function() {
            console.log("Go to previous page!")

        },
    },
    created: function() {
        this.loadQotd()
    }
})