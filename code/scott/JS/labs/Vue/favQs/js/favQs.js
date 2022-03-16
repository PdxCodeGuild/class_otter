const App = {
	data() {
		return {
            randomQuote: '',
			quotes: [],
            lastPage: true,
            authorPage: 1,
            keywordPage: 1,
            tagPage: 1,
            tag: '', // User Input for Tag Search
            author: '', // User Input for Author Search
			keyword: '', //User Input for Keyword
            type: '',
		}
    },

    created() {
        this.getRandomQuote()
    },

    methods: {

        getRandomQuote() {            
            axios({
                method: 'get',
                url: 'https://favqs.com/api/qotd',
                headers: {Accept: 'application/json'}
            })
            .then(response => {
                console.log(response.data)
                this.randomQuote = response.data.quote.body
            })
        },

        getQuoteByKeyword() {
            this.type = 'keyword'
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/`,
                headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.keyword, page: 1 }
            })
            .then(response => {
                console.log(response.data.last_page)
                this.lastPage = response.data.last_page
                this.quotes = response.data.quotes
            })
        },

        // getQuoteByTag() {
            // this.type = 'tag'
            // axios({
        // },

        // getQuoteByAuthor() {
           
        // },


        }
    }


Vue.createApp(App).mount('#app')
//  axios({
    // method: 'get',
    // url: 'https://favqs.com/api/qotd',
    // headers: {
        // 'x-api-key': 'api_key'
    // }
// }).then((response) => {
    // console.log(response.data)
// })


// axios({
    // method: 'post',
    // url: 'https://favqs.com/api/qotd',
    // data: {
        // name: 'joe',
        // age: '34'
    // }
// }).then((response) => {
    // console.log(response.data)
// })