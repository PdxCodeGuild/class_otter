// <<a class="waves-effect waves-teal btn-flat">button</a>
// <a class="waves-effect waves-light btn-small">Button</a>
// References:
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toTimeString
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/getHours
// https://www.w3schools.com/jsref/jsref_getminutes.asp
// https://www.w3schools.com/jsref/jsref_gethours.asp
// 

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
            userKey: '',
            // Feeds:
            // temperatureesp8266
            // humidityesp8266
            // humidityesp32
            // temperatureesp32
            // batteryvoltageesp32

            availableFeeds: [
                'temperatureesp8266',
                'humidityesp8266',
                'humidityesp32',
                'temperatureesp32',
                'batteryvoltageesp32',
            ],
    
            esp8266TemperatureKey: 'temperatureesp8266',
    
            temperatureFeedReturnLength: 600,

            ///////////////////////////////////////
        }
    },
    // props: ['feedResponseArray'],
    template: `
        <section>
            <h3>Search Interface</h3>

            <p>
                <a class="waves-effect waves-teal btn-flat">Load Chosen Data Feed</a>
                <div class="input-field col s12">
                    <select>
                        <option value="" disabled selected>Select Feed ID</option>
                        <template v-for="feedChoice in availableFeeds">
                        <option :value="feedChoice">{{ feedChoice }}</option>
                        </template>
                    </select>
                    <label>Choose Data Feed</label>
                </div>
                <div>
                <a class="waves-effect waves-teal btn-flat" @click="loadEsp8266TemperatureData">Load Livingroom Temperature Feed</a>
                <a class="waves-effect waves-teal btn-flat" @click="getListOfFeeds">Get List of Feeds</a>
                <a class="waves-effect waves-teal btn-flat" @click="getFeedInfo">Get Feed Info</a>
                <a class="waves-effect waves-teal btn-flat">Load Livingroom Humidity Feed</a>
                </div>
            </p>
            
        </section>
    `,
    methods: {

        loadEsp8266TemperatureData: function() {
            axios({
                method: 'get',
                url: `https://io.adafruit.com/api/v2/${ this.userName }/feeds/${ this.esp8266TemperatureKey }/data?limit=${ this.temperatureFeedReturnLength }`,
                params: {
                    // 'X-AIO-Key': this.userKey,
                    'X-AIO-Key': adafruit.key,
                }
            }).then((response) => {
                this.sendESP8266ToRoot(response.data)
            }).catch(error => {
                console.log(error.response.data)
            })
        },

        getListOfFeeds: function() {
            axios({
                method: 'get',
                // https://io.adafruit.com/api/v2/{username}/feeds/
                url: `https://io.adafruit.com/api/v2/${ this.userName }/feeds/`,
                params: {
                    'X-AIO-Key': adafruit.key,
                }
            }).then((response) => {
                this.sendSomethingToRoot(response.data)
            }).catch(error => {
                console.log(error.response.data)
            })
        },

        getFeedInfo: function() {
            axios({
                method: 'get',
                // /{username}/feeds/{feed_key}
                url: `https://io.adafruit.com/api/v2/${ this.userName }/feeds/${ this.esp8266TemperatureKey }`,
                params: {
                    'X-AIO-Key': adafruit.key,
                }
            }).then((response) => {
                this.sendSomethingToRoot(response.data)
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
            this.$emit('send-esp-temp-to-root', childComponentObject)
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
                        backgroundColor: '#0d47a1',
                        borderColor: '#0d47a1',
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
            <h3>{{ chartHeading }}</h3>
            <div>
            <a class="waves-effect waves-teal btn-flat" v-on:click="createLabels">Extract Labels</a><!--  -->
            <a class="waves-effect waves-teal btn-flat" v-on:click="createValues">Extract Values</a><!--  -->
            <a class="waves-effect waves-teal btn-flat" v-on:click="loadDataFromRoot">Update Chart Config</a>
            </div>
            <div>
                <a class="waves-effect waves-teal btn-flat" v-on:click="loadChart">Load Chart</a>
                <a class="waves-effect waves-teal btn-flat" v-on:click="updateChart">Update Chart</a>
                <a class="waves-effect waves-teal btn-flat" v-on:click="destroyChart">Remove Chart</a>
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

            this.chartConfig.data.labels = this.chartDataObject.labelArray.reverse()
            this.chartConfig.data.datasets[0].data = this.chartDataObject.valueArray.reverse()
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
        // esp8266ChartDataArray: [],

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

        saveEsp8266ToRootComponent: function(payload) {
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
