var app4 = new Vue({
    el: '#app-4',
    data: {
      todos: [
        { text: 'Learn JavaScript'},
        { text: 'Learn Vue' },
        { text: 'Build something awesome' }
      ],
      numbers: [
          1,
          2,
          5,
          1000
      ],
      message: 'Hello World!'
    },
    methods: {
        reverseMessage: function(message, num, event) {
            console.log(message)
            console.log(num)
            console.log(event)
            this.message = this.message.split('').reverse().join('')
        }
    },
    mounted: function() {
        console.log("vue app loaded!")
    },
    updated: function() {
        console.log("something changed on our webpage!")
    }
  })