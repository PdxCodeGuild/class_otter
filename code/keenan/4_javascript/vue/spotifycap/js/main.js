const vm = new Vue({
    el: "#app",
    data: {
        info: {},
    },


    methods: {
        // writing a get authorization function to get our token
        getAuth: function() {
            const params = new URLSearchParams ()
            params.append('grant_type','client_credentials')
            const authstring = btoa(`${client_id}:${client_secret}`, 'utf-8')
            axios({
                method: 'post',
                url: 'https://accounts.spotify.com/api/token',
                data: params,
                headers: {
                    'Authorization': `Basic ${ authstring }`,
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then(response => this.info = response.data)
        }    
    },
    created: function() {
        this.getAuth()
    }

})
    //     axios ({ 
    //         method: 'get',
    //         url: 'https://api.spotify.com/v1',
    //         headers: {
    //             Authorization: 
    //         },
            
    //     }).then(response => (this.info = response))
    //   }

      




// redirect URI - http://localhost:8080 this was saved in spotify developer tools
// base spotiy API URL:  https://api.spotify.com
// https://api.spotify.com/v1
//       const client_id = process.env.SPOTIFY_API_ID; // Your client id 
// const client_secret = process.env.SPOTIFY_CLIENT_SECRET; // Your secret 
// headers: {
//     Authorization: `Token token="${apiKey}"`
// }