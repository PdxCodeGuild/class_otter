// url, method, headers, params


const vm = new Vue({
    el: '#app',
    data: {
        qotd: {}
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
                // Response Object:
                // console.log(response)
                // Quote Object and other things:
                console.log(response.data)
            })
        }
    },
    created: function() {
        this.loadQotd()
    }
})