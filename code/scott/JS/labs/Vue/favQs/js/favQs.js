// Vue.component('quote-me', {
//     data: function() {
//         return {
//             filter: "",
//             type: ""
//         }
//     },
//     template: `
//         <div>
//         <h3>Enter your search text below..</h3>
//         <input type="type" placeholder="Enter Search Text Here" @keyup.enter="getQuote" v-model="filter">
//         <h3>Now select from the options below how you would like to search..</h3>
//         <select v-model="type">
//         <option disabled value="">Please select one</option>
//         <option>author</option>
//         <option>keyword</option>
//         <option>tag</option>
//         </select>
//         <h3>If everything is correct, click below!</h3>
//             <button @click="getQuote">Get Quote</button>
//         </div>
//         `,
//     methods: {
//         getQuote: function() {
//             this.$emit('quote', {type: this.type, filter: this.filter})
//             this.filter = ""
//             this.type = ""
//         }
//     }
// })



// const App = {
// 	data() {
// 		return {
//             randomQuote: '',
// 			quotes: [], //array literal
//             lastPage: true, //for paging
//             authorPage: 1, // method variable and start page
//             keywordPage: 1, // method variable and start page
//             tagPage: 1, // method variable and start page
//             tag: '', // variable and type for Tag Search
//             author: '', // variable and type for Author Search
// 			keyword: '', // variable and type for Keyword
//             type: '',
// 		}
//     },


const App = {
    data() {
        return {
            randomQuote: '',
            quotes: [],  //array literal
            lastPage: true, //for paging
            authorPage: 1, // method variable and start page
            keywordPage: 1, // method variable and start page
            tagPage: 1, // method variable and start page
            tag: '', // variable and type for Tag Search
            author: '', // variable and type for Author Search
            keyword: '', // variable and type for Keyword
            type: '', // variable used in assigning
        }
    },

    created() {
        this.getRandomQuote()
    },

    methods: {

        // loadRandom25: function() {
        //     axios({
        //         url: "https://favqs.com/api/quotes",
        //         method: "get",
        //         headers: {
        //             "Authorization": `Token token="${apiKey}"`
        //         },
        //     }).then(response => {
        //         this.results = response.data
        //     })
        // },

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

        getQuoteByTag() {
            this.type = 'tag'
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/`,
                headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.tag, type: 'tag', page: 1 }
            })
            .then(response => {
                // console.log(response.data.last_page)
                this.lastPage = response.data.last_page
                this.quotes = response.data.quotes

            })
        },
        
        getQuoteByAuthor() {
            this.type = 'author'
            axios({
                method: 'get',
                url: `https://favqs.com/api/quotes/`,
                headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                params: { filter: this.author, type: 'author', page: 1 }
            })
            .then(response => {
                // console.log(response.data)
                this.lastPage = response.data.last_page
                this.quotes = response.data.quotes
            })
        },

                        // Use Template literal to compare type & tag

        nextPage() {
            let myParams = {}
            if (this.type === 'tag') {
                myParams = { filter: this.tag, type: this.type, page: this.tagPage +=1 }
            }

            else if (this.type === 'author') {
                myParams = { filter: this.author, type: this.type, page: this.authorPage +=1 }
            }

            else if (this.type === 'keyword') {
                myParams = { filter: this.keyword, type: this.type, page: this.keywordPage +=1 }
            }

                axios({
                    method: 'get',
                    url: `https://favqs.com/api/quotes/`,
                    headers: {Accept: 'application/json', Authorization: 'Token token="855df50978dc9afd6bf86579913c9f8b"'},
                    params: myParams
                })
                .then(response => {
                    this.quotes = response.data.quotes
                    this.lastPage = response.data.last_page
                })
        }
    }
}

Vue.createApp(App).mount('#app')


App.component('quote', {
    props: ['quote'],
    template: ` 
        <article>
            <p>"{{ quote.body }}"" by {{ quote.author }}</p>
        </article> 
`
});
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