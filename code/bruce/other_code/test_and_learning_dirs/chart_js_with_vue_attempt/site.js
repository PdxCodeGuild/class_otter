// https://vue-chartjs.org/guide/#browser
// https://www.chartjs.org/docs/latest/getting-started/

// const labels = [
//     'January',
//     'February',
//     'March',
//     'April',
//     'May',
//     'June',
// ];

// const data = {
//     labels: labels,
//     datasets: [{
//         label: 'My First dataset',
//         backgroundColor: 'rgb(255, 99, 132)',
//         borderColor: 'rgb(255, 99, 132)',
//         data: [0, 10, 5, 2, 20, 30, 45],
//     }]
// };

// const config = {
//     type: 'line',
//     data: data,
//     options: {}
// };

// const myChart = new Chart(
//     document.getElementById('myChart'),
//     config
// );


// It seems that identifier in 'props' (below) has to be 'camelCase' (exampleComponent) of 'kebab-case' (example-component) used in 'Vue.component()' declaration.
Vue.component('example-component', {
    data: function() {
        return {
            theOfficialComponentGreeting: '¿Official component greeting?',
        }
    },
    // It seems that identifier in 'props' has to be 'camelCase' (exampleComponent) of 'kebab-case' (example-component) used in 'Vue.component()' declaration above.
    props: ['exampleComponent'],
    template: `
        <div>
            <!-- <p>¿Chart component hard-coded greeting?</p> -->
            <!-- <p>{{ theOfficialComponentGreeting }}</p> -->
            <p>Root Component: {{ exampleComponent }}</p>
        </div>
    `
})


const vm = new Vue({
    el: '#app',
    
    data: {
        rootComponentGreeting: '¿Root component greeting?',
        theRootComponentArray: [ 'First', 'Second', 'Third'],
    },

    methods: {

    },

    created: function() {
        console.log("Created!")
    }
})