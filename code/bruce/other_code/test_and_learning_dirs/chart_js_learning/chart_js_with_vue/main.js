// https://www.chartjs.org/docs/latest/getting-started/
// https://www.chartjs.org/docs/latest/developers/api.html


Vue.component('the-chart', {
    data: function() {
        return {
            chartHeading: "Chart Heading",

        // This is the Chart object's 'config':
            chartConfig: {
                type: 'line',

                data: {
                    labels: [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7,
                    ],

                    datasets: [{
                        label: 'One Thing',
                        backgroundColor: 'rgb(166, 3, 3)',
                        borderColor: 'rgb(166, 3, 3)',
                        data: [0, 1, 3, 6, 10, 15, 21],
                    },
                    {
                        label: 'Something Else',
                        backgroundColor: 'rgb(90, 115, 2)',
                        borderColor: 'rgb(90, 115, 2)',
                        data: [21, 15, 10, 6, 3, 2, 1],
                    }],
                },

                options: {} 
            },
        }
    },
    // props: ['chartConfig'],
    template: `
        <div>
            <button v-on:click="loadChart">Load the chart</button>
            <button v-on:click="updateChart">Update the chart</button>
            <p>{{ chartHeading }}</p>
            <canvas id="myChart" class="component-class"></canvas>
        </div>
    `,
    methods: {
        loadChart: function() {

            // let theElusiveChart = Chart.getChart("myChart");
            // console.log(`Beginning of loadChart: theElusiveChart:`, theElusiveChart)
            // theElusiveChart.destroy()
            // console.log(theElusiveChart)

            // console.log(myChart)
            // console.log(myChart.id)

            // console.log("Preparing to print 'Chart.instances[0]'.")
            // console.log(Chart.instances[0])
            // console.log("Printed 'Chart.instances[0]'.")
            
            // console.log(this.chartConfig.data.labels)
            // console.log(this.chartConfig.data.datasets[0].data)

            // console.log(`Printing Chart Instance 0:`, Chart.instances[0])
            
            const myChart = new Chart(
                document.getElementById('myChart'),
                this.chartConfig
            )
                
            // console.log(`Printing Chart Instance 0:`, Chart.instances[0])

            // console.log(myChart)
            // console.log(`Destroying ${myChart}.`)
            // myChart.destroy()
            
            // console.log(myChart)

            // theElusiveChart = Chart.getChart("myChart");
            // console.log(`theElusiveChart:`, theElusiveChart)

        },
        
        updateChart: function() {
            // // If chart doesn't already exist: loadChart.
            let theElusiveChart = Chart.getChart("myChart");
            theElusiveChart.destroy()
            const myChart = new Chart(
                document.getElementById('myChart'),
                this.chartConfig
            )

            // console.log(`Updating theElusiveChart:`, theElusiveChart)
            // theElusiveChart.config = this.chartConfig
            // theElusiveChart.update()
            // console.log(`theElusiveChart:`, theElusiveChart)

        }
    },

    mounted: function() {
        console.log(`Chart created!`)
    }
})


const vm = new Vue({
    el: '#app',

    data: {
        rootComponentHeading: "Root Component Heading",

    },

    methods: {

    },

    created: function() {
        console.log(`Root created!`)
    }
})
