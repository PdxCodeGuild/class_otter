


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
    
            temperatureFeedReturnLength: 600,

            ///////////////////////////////////////
        }
    },
    // props: ['feedResponseArray'],
    template: `
        <section>
            <h2>Search Interface</h2>

            <p>
                <button @click="loadEsp8266TemperatureData">Load Livingroom Temperature Feed</button>
                <button>Load Livingroom Humidity Feed</button>
            </p>
            
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
                this.sendESP8266ToRoot(response.data)
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
    },
    mounted: function() {
        
    }
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


Vue.component('temperature-chart', {
    data: function() {
        return {
            chartHeading: "Chart Interface",

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
                        backgroundColor: 'rgba(76, 89, 46, 1)',
                        borderColor: 'rgba(76, 89, 46, 1)',
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
            <button v-on:click="createLabels">Extract Labels</button><!--  -->
            <button v-on:click="createValues">Extract Values</button><!--  -->
            <button v-on:click="loadDataFromRoot">Update Chart Config</button>
            </div>
            <div>
                <button v-on:click="loadChart">Load Chart</button>
                <button v-on:click="updateChart">Update Chart</button>
                <button v-on:click="destroyChart">Remove Chart</button>
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

        loadDataFromRoot: function() {
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


const vm = new Vue({
    el: '#app',
    data: {
        esp8266DataArray: [],
        esp8266ChartDataArray: [],

        rootChartDataObject: {
            labelArray: [],
            valueArray: [],
        },

        objectReceivedFromChildComponent: {},
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
    },

    mounted: function() {
        // this.loadEsp8266TemperatureData()
    }
})
