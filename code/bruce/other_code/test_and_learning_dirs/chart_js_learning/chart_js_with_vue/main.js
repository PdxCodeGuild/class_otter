// https://www.chartjs.org/docs/latest/getting-started/


Vue.component('the-chart', {
    data: function() {
        return {
            chartHeading: "Chart Heading"
        }
    },
    template: `
        <div>
            <p>{{ chartHeading }}</p>
        </div>
    `,
    methods: {
    }
})


const vm = new Vue({
    el: '#app',

    data: {
        rootComponentHeading: "Root Component Heading",

        // This is the Chart object's 'config':
        chartConfig: {
            type: 'line',

            data: {
                labels: [
                    'January',
                    'February',
                    'March',
                    'April',
                    'May',
                    'June',
                    'Neverland',
                    'Outta sight',
                ],

                datasets: [{
                    label: 'My First dataset',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: [0, 10, 5, 2, 20, 30, 45],
                }],
            },
            options: {} 
        }
    },

    methods: {
        loadChart: function() {

            console.log(this.chartConfig.data.labels)
            console.log(this.chartConfig.data.datasets[0].data)

            const myChart = new Chart(
                document.getElementById('myChart'),
                this.chartConfig
            )
        }
    },

    created: function() {
        console.log(`We're created!`)

        this.loadChart()
    }
})
