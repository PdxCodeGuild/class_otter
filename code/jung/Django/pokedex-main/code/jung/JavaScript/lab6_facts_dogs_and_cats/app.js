const vm = new Vue({
    el: "#app",
    data: {
        dogP: {},
        dogF: {},
        catP: {},
        catF: {},
        selectedFile: null
    },
    methods: {
        showMoreDogs: function() {
            this.dogPic()
            this.dogFact()
        },
        showMoreCats: function() {
            this.catPic()
            this.catFact()
        },
        onFileSelected: function(event) {
            this.selectedFile = event.target.files[0]
        },
        dogPic: function() {
            axios({
                method: "get",
                url: "https://api.thedogapi.com/v1/images/search",
                headers: {
                    "x-api-key": "5dab5794-0114-42ac-aa43-50486fa89a30"
                },
            }).then((response) => {
                this.dogP = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        dogFact: function() {
            axios({
                method: "get",
                url: "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
            }).then((response) => {
                this.dogF = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        catFact: function() {
            axios({
                method: "get",
                url: "https://catfact.ninja/fact"
            }).then((response) => {
                this.catF = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        catPic: function() {
            axios({
                method: "get",
                url: "https://api.thecatapi.com/v1/images/search",
                headers: {
                    "x-api-key": "bcb64dd2-9475-4126-9fb3-bfe8237bc5c0"
                },
            }).then((response) => {
                this.catP = response.data
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        catUpload: function() {
            let formData = new FormData()
            formData.append("file", this.selectedFile)
            axios({
                method: "post",
                url: "https://api.thecatapi.com/v1/images/upload",
                headers: {
                    "x-api-key": "bcb64dd2-9475-4126-9fb3-bfe8237bc5c0",
                    "Content-Type": "multipart/form-data"
                },
                data: formData
            }).then((response) => {
                console.log(response.data)
                alert("You uploaded a cat pic!")
            }).catch(error => {
                console.log(error.response.data)
            })
        },
        dogUpload: function() {
            let formData = new FormData()
            formData.append("file", this.selectedFile)
            axios({
                method: "post",
                url: "https://api.thedogapi.com/v1/images/upload",
                headers: {
                    "x-api-key": "5dab5794-0114-42ac-aa43-50486fa89a30",
                    "Content-Type": "multipart/form-data"
                },
                data: formData
            }).then((response) => {
                console.log(response.data)
                alert("You uploaded a dog pic!")
            }).catch(error => {
                console.log(error.response.data)
            })
        },

    },
    created: function() {
        this.catFact()
        this.dogPic()
        this.catPic()
        this.dogFact()
        this.dogUpload()
        this.catUpload()
        this.onFileSelected()
    }
})