// let index = new Vue({
//     el: '#index',
//     delimiters: ['[[', ']]'],
//     data: {
//         message: 'Pokedex Lab',
//         pokemon: '',
//     },
//     methods: {

//     },
//     created: async function () {
//         let response = await axios({
//             method: 'get',
//             url: 'api/'
//         })
//         this.pokemon = response.data.data
//     }
// })

// let pokemon = new Vue({
//     el: '#pokemon',
//     delimiters: ['[[', ']]'],
//     data: {
//         message: 'worked',
//         mon: ''
//     },
//     created: async function () {
//         let path = window.location.pathname
//         let number = path.split('/')[2]
//         let response = await axios({
//             method: 'get',
//             url: 'api/'
//         })
//         this.mon = response.data
//     }
