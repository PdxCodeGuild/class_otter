const vm = new Vue({
    el: "#app",
    data: {
        apod: {},
        message: "This is working!"
    },

    methods: {
        loadAPOD: function() {
            axios({
                method: 'get',
                url: 'https://api.nasa.gov/planetary/apod',
                params: {
                    
                    api_key: `${apikey}`,
                    date: "2021-07-14"
                    
                }
            }).then((response) => {
                this.apod = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        }
    },
    
    created: function() {
        this.loadAPOD()
    }
})