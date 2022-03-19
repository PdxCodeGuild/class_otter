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
            if (this.searchType === '') {
                this.searchType = 'keyword'
            }
            this.$emit('search-quotes', {
                type: this.searchType,
                term: this.searchTerm,
            })
            this.searchType = ''
            this.searchTerm = ''
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
        randomQuotes: [],
        searchType: '',
        searchTerm: '',
        quickButtonAuthorSearchName: '',
        displayedSearchTerm: '',
        currentPage: 1,
        isLastPage: false,
    },
    methods: {

        // loadSingleQuote: function() {
        //     axios({
        //         method: 'get',
        //         url: 'https://favqs.com/api/qotd'
        //     }).then((response) => {
        //         this.qotd = response.data
        //     }).catch(error => {
        //         console.log(error.response.data)
        //     })
        // },

        loadRandomQuotes: function() {
            this.results = {}
            this.randomQuotes = []
            for (let i = 0; i < 5; i++) {
                // console.log(i)
                axios({
                    method: 'get',
                    url: 'https://favqs.com/api/qotd'
                }).then((response) => {
                    this.qotd = response.data
                    // console.log(this.qotd.quote.body)
                    this.randomQuotes.push(this.qotd.quote)
                }).catch(error => {
                    console.log(error.response.data)
                })
            }
        },

        loadAuthorQuotes: function(author) {
            console.log(`Getting some ${ author } Quotes`)
            this.searchType = 'author'
            this.searchTerm = author
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    type: this.searchType,
                    filter: this.searchTerm,
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
            this.searchType = payload.type
            this.searchTerm = payload.term
            if (payload.term === 'keyword') {
                payload.type = ''
            }
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.searchTerm,
                    type: this.searchType,
                },
                headers: {
                    "Authorization": this.token
                }
            }).then((response) => {
                this.results = response.data
                if (payload.type === 'author') {
                    this.displayedSearchTerm = this.results.quotes[0].author
                } else {
                    this.displayedSearchTerm = this.searchTerm
                }
            }).catch(error => {
                console.log(error.response.data)
            })
        },

        nextPage: function() {
            if (!this.results.last_page) {
                console.log("Going to next page!")
                this.currentPage++
                console.log(`On last page (before request): ${this.results.last_page}`)
                // console.log(`On first page (before request): ${this.results.page === 1}`)
                
                axios({
                    method: 'get',
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        filter: this.searchTerm,
                        type: this.searchType,
                        page: this.results.page + 1
                    },
                    headers: {
                        "Authorization": this.token
                    }
                }).then((response) => {
                    this.results = response.data
                    console.log(`On last page (after request): ${this.results.last_page}`)
                    // console.log(`On first page (after request): ${this.results.page === 1}`)
                }).catch(error => {
                    console.log(error.response.data)
                })
            }
        },
        
        previousPage: function() {
            if (this.results.page !== 1) {
                console.log("Going to previous page!")
                this.currentPage--
                // console.log(`On last page (before request): ${this.results.last_page}`)
                console.log(`On first page (before request): ${this.results.page === 1}`)
                
                axios({
                    method: 'get',
                    url: 'https://favqs.com/api/quotes',
                    params: {
                        filter: this.searchTerm,
                        type: this.searchType,
                        page: this.results.page - 1
                    },
                    headers: {
                        "Authorization": this.token
                    }
                }).then((response) => {
                    this.results = response.data
                    // console.log(`On last page (after request): ${this.results.last_page}`)
                    console.log(`On first page (after request): ${this.results.page === 1}`)
                }).catch(error => {
                    console.log(error.response.data)
                })
            }
        },
    },

    created: function() {
        this.loadRandomQuotes()
    }
})