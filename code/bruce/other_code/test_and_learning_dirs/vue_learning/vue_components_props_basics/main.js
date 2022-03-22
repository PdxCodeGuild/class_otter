

Vue.component('test-component', {
    data: function() {
        return {
            testComponentText: 'Component property text',
        }
    },
    // test-component-title
    props: ['testComponentTitle'],
    template: `
        <div>
            <h2>{{ testComponentTitle }}</h2>
            <p>Hard-coded text</p>
            <p>{{ testComponentText }}</p>
        </div>
    `,
    methods: {

    }
})


Vue.component('test-component-with-object', {
    data: function() {
        return {
            testComponentText: 'Component property text',
        }
    },
    props: ['objectFromRoot'],
    template: `
    <div>
        <h2>{{ objectFromRoot.text }}</h2>
        <p>Hard-coded text</p>
        <p>{{ objectFromRoot.id }}</p>
    </div>
    `,
    methods: {

    }
})


const vm = new Vue({
    el: '#app',
    data: {
        rootTestText: 'Initial Root text!',
        rootTestObject: {
            id: 1,
            text: 'Root Object Text!'
        }
    },

    methods: {

    },

    mounted: function() {
    }
})