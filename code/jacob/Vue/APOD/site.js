const vm = new Vue({
    el: "#app",
    data: {
        apod: {},
        arand: {},
        message: "This is working!",
        userFilter: "",
        showRand: true
    },

    methods: {
        loadAPOD: function() {
            axios({
                method: 'get',
                url: 'https://api.nasa.gov/planetary/apod',
                params: {
                    
                    api_key: `${apikey}`,
                    // date: "2021-07-14"
                    // count: 3
                    date: this.userFilter
                    
                }
            }).then((response) => {
                this.apod = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
            
        },
        loadRand: function() {
            axios({
                method: 'get',
                url: 'https://api.nasa.gov/planetary/apod',
                params: {
                    
                    api_key: `${apikey}`,
                    count: 3
                
                }
            }).then((response) => {
                this.arand = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        }
    },
    
    created: function() {
        this.loadRand()
        
    }
})