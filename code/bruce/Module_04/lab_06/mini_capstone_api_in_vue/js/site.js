// url, method, headers, params
// feed_key, created_at, value


Vue.component('storage-component', {
    data: function() {
        return {
            // Sample data from feed: "temperatureesp8266":
                "id": "0EZHPBF3YEHK7QX47N6Q0TCMV5",
                "value": "69.79",
                "feed_id": 1303967,
                "feed_key": "temperatureesp8266",
                "created_at": "2022-03-19T23:17:31Z",
                "location": {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            "0.0",
                            "0.0",
                            "0.0"
                        ]
                    }
                },
                "lat": "0.0",
                "lon": "0.0",
                "ele": "0.0",
                "created_epoch": 1647731851,
                "expiration": "2022-04-18T23:17:31Z"

        }
    }
})


Vue.component('search-component', {
    // Move search functionality to this component.
    data: function() {
        return {

            ///////////////////////////////////////
            // Feed properties:
            // This is the array we will be updating with data from the feed:
            esp8266DataArray: [],
            // feedResponseArray: [],
            userName: 'FlynntKnapp',
            userKey: 'cc8d6fdeba6b4d0aa6901988169ec8d6',
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

            hoursTimeDiff: 1,
            hoursTimeDiffString: 'hours',
    
            defaultHoursReturnLength: 24,
            temperatureFeedReturnLength: 600,

            sampleUrls: [
                'https://io.adafruit.com/api/v2/{username}/feeds/{feed_key}/data/chart?hours=1',
            ],
            ///////////////////////////////////////


            testText: 'Some Text',
            testToggle: false,

        }
    },
    // props: ['feedResponseArray'],
    template: `
        <section>
            <h2>Adafruit IO Feed</h2>

            <p>
                <button @click="loadEsp8266TemperatureData">Load Livingroom Temperature Feed</button>
                <!-- <button @click="loadEsp8266TemperatureChartData">Load Livingroom Chart Temperature Feed</button> -->
                <button>Load Livingroom Humidity Feed</button>
            </p>

            
            <!--  -->
            <!--  -->
            
        </section>
    `,
    methods: {

        loadEsp8266TemperatureData: function() {
            axios({
                method: 'get',
                url: `https://io.adafruit.com/api/v2/${ this.userName }/feeds/${ this.esp8266TemperatureKey }/data?limit=${ this.temperatureFeedReturnLength }`,
                params: {
                    'X-AIO-Key': this.userKey,
                }
            }).then((response) => {
                // console.log(response)  // Response Object
                // console.log(response.data)  // Response Array
                // console.log(response.data[0])  // First element of Array
                // this.feedResponseArray = response.data
                // this.sendSomethingToRoot(response.data)
                this.esp8266DataArray = response.data
                this.sendESP8266ToRoot(response.data)
            }).catch(error => {
                console.log(error.response.data)
            })
        },

        loadEsp8266TemperatureChartData: function() {
            axios({
                method: 'get',
                // url: `https://io.adafruit.com/api/v2/${ this.userName }/feeds/${ this.esp8266TemperatureKey }/data?limit=${ this.defaultHoursReturnLength }`,
                // 'https://io.adafruit.com/api/v2/{username}/feeds/{feed_key}/data/chart?hours=1'
                url: `https://io.adafruit.com/api/v2/${ this.userName }/feeds/${ this.esp8266TemperatureKey }/data/chart?${ this.hoursTimeDiffString }=${ this.hoursTimeDiff }?limit=${ this.defaultHoursReturnLength }`,
                params: {
                    'X-AIO-Key': this.userKey,
                }
            }).then((response) => {
                // console.log(response)  // Response Object
                // console.log(response.data)  // Response Array
                // console.log(response.data[0])  // First element of Array
                // this.feedResponseArray = response.data
                // this.sendSomethingToRoot(response.data)
                this.esp8266DataArray = response.data
                this.sendESP8266ChartDataToRoot(response.data)
            }).catch(error => {
                console.log(error.response.data)
            })
        },

        sendSomethingToRoot: function(childComponentObject) {
            console.log(`Sending something to Root! - `, childComponentObject)
            this.$emit('send-to-root', childComponentObject)
        },

        sendESP8266ToRoot: function(childComponentObject) {
            console.log(`Sending ESP8266 to Root! - `, childComponentObject)
            this.$emit('send-esp8266-to-root', childComponentObject)
        },

        sendESP8266ChartDataToRoot: function(childComponentObject) {
            console.log(`Sending ESP8266 to Root! - `, childComponentObject)
            this.$emit('send-esp8266-chart-to-root', childComponentObject)
        },

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



Vue.component('the-chart-example', {
    data: function() {
        return {
            chartHeading: "Example Chart Heading",

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
            <h2>{{ chartHeading }}</h2>
            <button v-on:click="loadChart">Load Example chart</button>
            <button v-on:click="updateChart">Update Example chart</button>
            <button v-on:click="destroyChart">Remove Example chart</button>
            <canvas id="myExampleChart" class="component-class"></canvas>
        </div>
    `,
    methods: {
        loadChart: function() {

            const myExampleChart = new Chart(
                document.getElementById('myExampleChart'),
                this.chartConfig
            )
        },
        
        updateChart: function() {
            let theElusiveChart = Chart.getChart("myExampleChart")

            //////////////////////////////////////
            // To Update existing chart:
            // theElusiveChart.update()
            //////////////////////////////////////


            //////////////////////////////////////
            // To Destroy and create new chart:
            if (theElusiveChart !== undefined) {
                theElusiveChart.destroy()
                const myExampleChart = new Chart(
                    document.getElementById('myExampleChart'),
                    this.chartConfig
                    )
            }
            //////////////////////////////////////
                
        },

        destroyChart: function() {
            let theElusiveChart = Chart.getChart("myExampleChart")
            if (theElusiveChart !== undefined) {
                theElusiveChart.destroy()
            }
        }
    },

    mounted: function() {
        console.log(`Chart mounted!`)
    }
})


Vue.component('temperature-chart', {
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
                        label: 'Living Room Temperature',
                        backgroundColor: 'rgb(166, 3, 3)',
                        borderColor: 'rgb(166, 3, 3)',
                        data: [
                            0,
                            1,
                            3,
                            6,
                            10,
                            15,
                            21],
                    }],
                },

                options: {} 
            },
        }
    },
    props: ['chartDataObject'],
    template: `
        <div>
            <h2>{{ chartHeading }}</h2>
            <div>
            <!-- <button v-on:click="createLabels">Extract Labels</button> -->
            <!-- <button v-on:click="createValues">Extract Values</button> -->
            <button v-on:click="loadDataFromRoot">Update Chart Config</button>
            </div>
            <div>
                <button v-on:click="loadChart">Load Temperature chart</button>
                <button v-on:click="updateChart">Update Temperature chart</button>
                <button v-on:click="destroyChart">Remove Temperature chart</button>
            </div>
            <canvas id="esp8266TemperatureChart" class="component-class"></canvas>
        </div>
    `,
    methods: {
        createLabels: function() {
            this.$emit('create-labels')
        },
        
        createValues: function() {
            this.$emit('create-values')
        },

        // "chartConfig.data.datasets.0.data.0"
        // "chartConfig.data.labels.0"
        loadDataFromRoot: function() {
            this.createLabels()
            this.createValues()
            this.chartConfig.data.labels = []
            this.chartConfig.data.datasets[0].data = []
            console.log(`Chart Data Object`, this.chartDataObject)
            console.log(`Getting data from Root!`)
            this.chartConfig.data.labels = this.chartDataObject.labelArray
            this.chartConfig.data.datasets[0].data = this.chartDataObject.valueArray
        },

        loadChart: function() {
            this.destroyChart()
            console.log(`rootChartDataObject`, this.chartDataObject)

            const esp8266TemperatureChart = new Chart(
                document.getElementById('esp8266TemperatureChart'),
                this.chartConfig
            )
        },
        
        updateChart: function() {
            let theElusiveChart = Chart.getChart("esp8266TemperatureChart")

            //////////////////////////////////////
            // To Update existing chart:
            // theElusiveChart.update()
            //////////////////////////////////////


            //////////////////////////////////////
            // To Destroy and create new chart:
            if (theElusiveChart !== undefined) {
                theElusiveChart.destroy()
                const esp8266TemperatureChart = new Chart(
                    document.getElementById('esp8266TemperatureChart'),
                    this.chartConfig
                    )
            }
            //////////////////////////////////////
                
        },

        destroyChart: function() {
            let theElusiveChart = Chart.getChart("esp8266TemperatureChart")
            if (theElusiveChart !== undefined) {
                theElusiveChart.destroy()
            }
        },
    },

    mounted: function() {
        console.log(`Chart mounted!`)
    }
})

// Vue.component('temperature-chart-chart-data', {
//     data: function() {
//         return {
//             chartHeading: "Chart Heading",

//         // This is the Chart object's 'config':
//             chartConfig: {
//                 type: 'line',

//                 data: {
//                     labels: [
//                         1,
//                         2,
//                         3,
//                         4,
//                         5,
//                         6,
//                         7,
//                     ],

//                     datasets: [{
//                         label: 'Living Room Temperature',
//                         backgroundColor: 'rgb(166, 3, 3)',
//                         borderColor: 'rgb(166, 3, 3)',
//                         data: [
//                             0,
//                             1,
//                             3,
//                             6,
//                             10,
//                             15,
//                             21],
//                     }],
//                 },

//                 options: {} 
//             },
//         }
//     },
//     props: ['rootChartChartDataObject'],
//     template: `
//         <div>
//             <h2>{{ chartHeading }}</h2>
//             <div>
//             <button v-on:click="createLabels">Extract Labels</button>
//             <button v-on:click="createValues">Extract Values</button>
//             <button v-on:click="loadDataFromRoot">Update Chart Config</button>
//             </div>
//             <div>
//                 <button v-on:click="loadChart">Load Temperature chart</button>
//                 <button v-on:click="updateChart">Update Temperature chart</button>
//                 <button v-on:click="destroyChart">Remove Temperature chart</button>
//             </div>
//             <canvas id="esp8266TemperatureChartChart" class="component-class"></canvas>
//         </div>
//     `,
//     methods: {
//         createLabels: function() {
//             this.$emit('create-labels')
//         },
        
//         createValues: function() {
//             this.$emit('create-values')
//         },

//         // "chartConfig.data.datasets.0.data.0"
//         // "chartConfig.data.labels.0"
//         loadDataFromRoot: function() {
//             this.chartConfig.data.labels = []
//             this.chartConfig.data.datasets[0].data = []
//             console.log(`Chart Data Object`, this.chartDataObject)
//             console.log(`Getting data from Root!`)
//             this.chartConfig.data.labels = this.chartDataObject.labelArray
//             this.chartConfig.data.datasets[0].data = this.chartDataObject.valueArray
//         },

//         loadChart: function() {
//             this.destroyChart()
//             console.log(`rootChartDataObject`, this.chartDataObject)

//             const esp8266TemperatureChartChart = new Chart(
//                 document.getElementById('esp8266TemperatureChartChart'),
//                 this.chartConfig
//             )
//         },
        
//         updateChart: function() {
//             let theElusiveChart = Chart.getChart("esp8266TemperatureChartChart")

//             //////////////////////////////////////
//             // To Update existing chart:
//             // theElusiveChart.update()
//             //////////////////////////////////////


//             //////////////////////////////////////
//             // To Destroy and create new chart:
//             if (theElusiveChart !== undefined) {
//                 theElusiveChart.destroy()
//                 const esp8266TemperatureChartChart = new Chart(
//                     document.getElementById('esp8266TemperatureChartChart'),
//                     this.chartConfig
//                     )
//             }
//             //////////////////////////////////////
                
//         },

//         destroyChart: function() {
//             let theElusiveChart = Chart.getChart("esp8266TemperatureChartChart")
//             if (theElusiveChart !== undefined) {
//                 theElusiveChart.destroy()
//             }
//         },
//     },

//     mounted: function() {
//         console.log(`Chart mounted!`)
//     }
// })


const vm = new Vue({
    el: '#app',
    data: {
        // feed_key, created_at, value
        // "esp8266DataArray.0.feed_key"
        // "esp8266DataArray.0.created_at"
        // "esp8266DataArray.0.value"
        esp8266DataArray: [],
        esp8266ChartDataArray: [],

        rootChartDataObject: {
            labelArray: [],
            valueArray: [],
        },

        rootChartChartDataObject: {},



        objectReceivedFromChildComponent: {},

        rootTestText: 'Initial Root text!',
        rootTestObject: {
            id: 1,
            text: 'Root Object Text!'
        }
    },

    methods: {

        saveSomethingToRootComponent: function(payload) {
            // This 'payload' was received from 'search-component':
            console.log(`Root is printing something from search! - `, payload)
            // Save 'payload' to some 'property' in Root component:
            console.log(`Saving as 'this.objectReceivedFromChildComponent!' - `, payload)
            this.objectReceivedFromChildComponent = payload
            // Console log the value saved to Root component:
            console.log(`Value of 'objectReceivedFromChildComponent' in Root component! - `, this.objectReceivedFromChildComponent)
        },

        saveESP8266ToRootComponent: function(payload) {
            // This 'payload' was received from 'search-component':
            console.log(`Root is printing something from search! - `, payload)
            // Save 'payload' to some 'property' in Root component:
            console.log(`Saving as 'this.esp8266DataArray!' - `, payload)
            this.esp8266DataArray = payload
            // Console log the value saved to Root component:
            console.log(`Value of 'esp8266DataArray' in Root component! - `, this.esp8266DataArray)
        },

        saveESP8266ChartToRootComponent: function(payload) {
            this.esp8266ChartDataArray = payload
        },

        createLabelArray: function() {
            this.rootChartDataObject.labelArray = []
            for (let i = 0; i < this.esp8266DataArray.length; i++) {
                this.rootChartDataObject.labelArray.push(this.esp8266DataArray[i].created_at)
            }
        },

        createValueArray: function() {
            this.rootChartDataObject.valueArray = []
            for (let i = 0; i < this.esp8266DataArray.length; i++) {
                this.rootChartDataObject.valueArray.push(this.esp8266DataArray[i].value)
            }
        },

        replaceChartConfigWithThisStuff: function() {

        }
    },

    mounted: function() {
        // this.loadEsp8266TemperatureData()
    }
})
