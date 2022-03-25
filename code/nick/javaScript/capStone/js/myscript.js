new Vue({
    el: '#app',
    data() {
        return {
            title: 'List of countries',
            countries: [],
            country: {},
            show_country: false
        }
    }, methods: {
        fetchCountries: function () {
            let url = 'https://restcountries.com/v2/all';
            axios.get(url).then(response => {
                this.countries = response.data
                console.log(this.countries)
            })
        },
        showCountry: function (alphacode) {
            let allCountries = this.countries;
            let country = allCountries.filter(country => country.alpha2Code == alphacode)
            this.country = country
            this.show_country = true
            console.log(country)
        },
        showCountries: function () {
            this.show_country = false
        }
    },
    mounted() {
        this.fetchCountries()
    }
})








































// new Vue({
//     el: '#app',
//     data() {
//         return {
//             tools: []

//         }
//     },
//     mounted() {
//         axios.get('https://sheetsu.com/apis/v1.0su/a07ffabf39a3')
//             .then(response => (console.log(response.data), this.tools = response.data))
//     }
// })



// <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta http-equiv="X-UA-Compatible" content="IE=edge">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>Javascript Capstone</title>
// </head>
// <body>
//     <h1>inventory</h1>
//     <div id="app">
//         {{  tools }}
//         <ul id="v=for-object"></ul>
//     </div>
//     <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
//     <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
//     <script src="js/myscript.js"></script>
// </body>
// </html>