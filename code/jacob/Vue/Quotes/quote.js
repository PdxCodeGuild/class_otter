Vue.component('loadQotd', {
    data: function() {
        return {
            results: {},
            userFilter: "",
            userType: "",
            page: 1
        }
    },
    template:`
        <div>
            <input type="text" placeholder="New Search" v-model="userFilter">
            <select v-model="userType">
                    <option disabled value="">Please Select</option>
                    <option value="author">Author</option>
                    <option value="keyword">Keyword</option>
                    <option value="tag">Tag</option>
            </select>
            <button v-on:click="loadQuotes">Submit</button>
            <div v-for="result in results.quotes" v-bind:key="result.id">
                <p>{{ result.body }}</p>
                <p><a :href="result.url">{{ result.author }}</a></p>
                
            </div>
            <div v-if="results.last_page===false && results.page>1">
                <button v-on:click="nextQuotes">Next Page</button>
                <button v-on:click="lastQuotes">Last Page</button>
            </div>
            <div v-else-if="results.last_page===false">
                <button v-on:click="nextQuotes">Next Page</button>
            </div>
            <div v-else-if="results.last_page===true">
                <button v-on:click="lastQuotes">Last Page</button>
            </div>
        </div>
          
    `,
    methods: {
        loadQuotes: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.userFilter,
                    type: this.userType,
                    page: this.page,
                },
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => {
                this.results = response.data
                this.$emit('done-searching')
            })
        },
        nextQuotes: function() {
            this.page++
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.userFilter,
                    type: this.userType,
                    page: this.page,
                },
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => this.results = response.data)
        },
        lastQuotes: function() {
            this.page--
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                params: {
                    filter: this.userFilter,
                    type: this.userType,
                    page: this.page,
                },
                headers: {
                    "Authorization": `Token token="855df50978dc9afd6bf86579913c9f8b"`
                }
            }).then(response => this.results = response.data)
        },
        // loadColors: function(){
        //     if (this.userType === "author"){
        //         console.log("I work.")
        //     }
        // }
    }
})
const vm = new Vue({
    el: "#app",
    data: {
        qotd: {},
        showQuotes: true,
        userFilter: "",
        userType: "",
        page: 1,
    },

    methods: {
        loadQotd: function() {
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="${apikey}"`
                }
            }).then((response) => {
                this.qotd = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
            
        },

        
    },

    created: function() {
        this.loadQotd()
        
        }
})