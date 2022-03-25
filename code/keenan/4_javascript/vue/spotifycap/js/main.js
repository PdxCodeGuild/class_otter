const vm = new Vue({
    el: "#app",
    data: {
        info: {},
        releases: {},
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
            }).then(response => {
                this.info = response.data,
                this.getGenres()
            })
        },

        getGenres: function() {
            // const country = SE;
            const limit = 10;
            const offset = 5;
            axios({
                method: "get",
                url: "https://api.spotify.com/v1/browse/new-releases",
                headers: {
                    'Authorization': `Bearer ${ this.info.access_token }`
                }
            }).then(response => this.releases = response.data)
            // there is not response.data, in releases it would be something like releases.albums.items which is the list of 20 objects
        }

        


        // putting this on hold beacuse I don't understand the input criteria
        // spotifySearch: function () {
        //     // this needs to include a 'search' field for user input to search
        //     axios({
        //         method: 'get'
        //         url: 'https://api.spotify.com/v1/search'
        //         headers: {
        //             'Authorization': `Bearer ${ this.info.access_token}`,
        //         }
        //     })
        //     console.log(response.data)
        // }    
    },
    created: function() {
        this.getAuth()
    }

})


// what is the usage for the async keyword for a function like my getAuth..?
// instead of at line 39 could i use a (), iffy? reviewing info from this yt vid https://www.youtube.com/watch?v=SbelQW2JaDQ&t=408s

// 

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