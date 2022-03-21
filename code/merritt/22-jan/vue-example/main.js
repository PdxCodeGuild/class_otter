var app6 = new Vue({
    el: '#app-6',
    data: {
      message: 'Hello Vue!'
    },
    methods: {

    },
    mounted: function() {
        console.log("all of our page elemetns are loaded!")
    },
    updated: function() {
        console.log("our page has been updated!")
    }
  })