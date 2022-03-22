// url, method, headers, params

// Sample data from feed: "temperatureesp8266":
// {
//     "id": "0EZHPBF3YEHK7QX47N6Q0TCMV5",
//     "value": "69.79",
//     "feed_id": 1303967,
//     "feed_key": "temperatureesp8266",
//     "created_at": "2022-03-19T23:17:31Z",
//     "location": {
//         "type": "Feature",
//         "geometry": {
//             "type": "Point",
//             "coordinates": [
//                 "0.0",
//                 "0.0",
//                 "0.0"
//             ]
//         }
//     },
//     "lat": "0.0",
//     "lon": "0.0",
//     "ele": "0.0",
//     "created_epoch": 1647731851,
//     "expiration": "2022-04-18T23:17:31Z"
// }


Vue.component('search-component', {
    // Move search functionality to this component.
    data: function() {
        return {
            esp8266DataArray: {},
            userName: 'FlynntKnapp',
            // Feeds:
            // temperatureesp8266
            // humidityesp8266
            // humidityesp32
            // temperatureesp32
            // batteryvoltageesp32
    
            esp8266TemperatureKey: 'temperatureesp8266',
            // humidityesp8266
            // humidityesp32
            // temperatureesp32
            // batteryvoltageesp32
    
            defaultFeedReturnLength: 5,
            feedReturnLength: 7,

            testText: 'Some Text',
            testToggle: false,
        }
    },
    template: `
        <section>
            <h2>The Super Special Search component!</h2>
            <p>¿Something's gonna be here?</p>
            <input type="checkbox" v-model="testToggle"><span>{{ testToggle }}</span>
            <input type="text" v-model="testText"><span>{{ testText }}</span>
        </section>
    `,
    methods: {
        sendDataToRoot: function() {
            
        }
    },
    mounted: function() {
        
    }
})


Vue.component('temperature-display-li', {
    data: function() {
        return {

        }
    },
    props: ['temperatureDisplayLi'],
    template: `
        <li >{{ temperatureDisplayLi.feed_key}} : {{ temperatureDisplayLi.value }} : {{ temperatureDisplayLi.created_at }}</li>
    `
})


Vue.component('temperature-display-table', {
    data: function() {
        return {

        }
    },
    props: ['temperatureDisplayTable'],
    template: `
        <tr>
            <td>{{ temperatureDisplayTable.created_at }}</td>
            <td>{{ temperatureDisplayTable.feed_key }}</td>
            <td>{{ temperatureDisplayTable.value }}</td>
        </tr>
    `
})



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
            <button v-on:click="loadChart">Load chart</button>
            <button v-on:click="updateChart">Update chart</button>
            <button v-on:click="destroyChart">Remove chart</button>
            <h2>{{ chartHeading }}</h2>
            <canvas id="myChart" class="component-class"></canvas>
        </div>
    `,
    methods: {
        loadChart: function() {

            const myChart = new Chart(
                document.getElementById('myChart'),
                this.chartConfig
            )
        },
        
        updateChart: function() {
            let theElusiveChart = Chart.getChart("myChart")

            //////////////////////////////////////
            // To Update existing chart:
            // theElusiveChart.update()
            //////////////////////////////////////


            //////////////////////////////////////
            // To Destroy and create new chart:
            if (theElusiveChart !== undefined) {
                theElusiveChart.destroy()
                const myChart = new Chart(
                    document.getElementById('myChart'),
                    this.chartConfig
                    )
            }
            //////////////////////////////////////
                
        },

        destroyChart: function() {
            let theElusiveChart = Chart.getChart("myChart")
            if (theElusiveChart !== undefined) {
                theElusiveChart.destroy()
            }
        }
    },

    mounted: function() {
        console.log(`Chart mounted!`)
    }
})


const vm = new Vue({
    el: '#app',
    data: {
        esp8266DataArray: {},
        userName: 'FlynntKnapp',
        // Feeds:
        // temperatureesp8266
        // humidityesp8266
        // humidityesp32
        // temperatureesp32
        // batteryvoltageesp32

        esp8266TemperatureKey: 'temperatureesp8266',
        // humidityesp8266
        // humidityesp32
        // temperatureesp32
        // batteryvoltageesp32

        defaultFeedReturnLength: 5,
        feedReturnLength: 7,


    },

    methods: {

        loadEsp8266TemperatureData: function() {
            axios({
                method: 'get',
                url: `https://io.adafruit.com/api/v2/${ this.userName }/feeds/${ this.esp8266TemperatureKey }/data?limit=${ this.defaultFeedReturnLength }`,
                params: {
                    'X-AIO-Key': 'cc8d6fdeba6b4d0aa6901988169ec8d6',
                }
            }).then((response) => {
                // console.log(response)  // Response Object
                // console.log(response.data)  // Response Array
                // console.log(response.data[0])  // First element of Array
                // console.log(response.data[0].feed_key)  // First element 'feed_key'
                // console.log(response.data[0].id)  // First element 'id'
                // console.log(response.data[0].value)  // First element 'value'
                this.esp8266DataArray = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
    },

    mounted: function() {
    }
})
