Vue.component("memoryGame", {
  data: function() {
    return {
      cardData: [
        { id:1, value:"", show: false},
        { id:2, value:"", show: false},
        { id:3, value:"", show: false},
        { id:4, value:"", show: false},
        { id:5, value:"", show: false},
        { id:6, value:"", show: false},
        { id:7, value:"", show: false},
        { id:8, value:"", show: false},
        { id:9, value:"", show: false},
        { id:10, value:"", show: false},
        { id:11, value:"", show: false},
        { id:12, value:"", show: false},
        { id:13, value:"", show: false},
        { id:14, value:"", show: false},
        { id:15, value:"", show: false},
        { id:16, value:"", show: false},
      ],
      currentVal: null,
      result: '',
      pokemon: {},
      pokemon_list: [],
      random_pokemon_list: [],

    }
  },
  template: `
    <div>
      <div class="game-board">
        <h3> {{result}} </h3>
        <h4>Current Card: {{currentVal}} </h4>
        <div class="cardHolder">
          <div class="card" v-for="(card, index) in cardData" :key="index">
            <button :class="card.show? 'show' : ''" @click="showCard(index, card.value)">
              <p v-if="!card.show">Click Here</p>
              <img v-if="card.show" :src="card.value">
            </button>
          </div>
        </div>
      </div>
    </div>
  `,
  methods: {
    showCard(card_id, card_value) {
      this.cardData[card_id].show=true;

      if(this.currentVal === null) {
        this.currentVal=card_value;
      }else if(card_value === this.currentVal) {
        this.result = "Good!"
        this.currentVal=null;
      }else {
        this.result = "Try again!"
        setTimeout(() => {
          this.cardData.map( card => card.show=false)
        }, 1000)
        this.currentVal = null
      }
    },

    listOldPokemon: function() {
      for (let i = 0; i < 8; i++) {
        axios({
          method: "get",
          url: `https://pokeapi.co/api/v2/pokemon/${Math.floor(1 + Math.random() * 151)}`,
        }).then((response) => {
          this.pokemon_list.push(response.data.sprites.other["official-artwork"].front_default)
        }).catch(error => {
          console.log(error.response.data)
        })
      }
    },

    listPokemon: function() {    
      let URL3 = `https://pokeapi.co/api/v2/pokemon/${Math.floor(1 + Math.random() * 151)}`
      let URL2 = `https://pokeapi.co/api/v2/pokemon/${Math.floor(1 + Math.random() * 151)}`
      let URL4 = `https://pokeapi.co/api/v2/pokemon/${Math.floor(1 + Math.random() * 151)}`
      let URL1 = `https://pokeapi.co/api/v2/pokemon/${Math.floor(1 + Math.random() * 151)}`
      let URL5 = `https://pokeapi.co/api/v2/pokemon/${Math.floor(1 + Math.random() * 151)}`
      let URL6 = `https://pokeapi.co/api/v2/pokemon/${Math.floor(1 + Math.random() * 151)}`
      let URL7 = `https://pokeapi.co/api/v2/pokemon/${Math.floor(1 + Math.random() * 151)}`
      let URL8 = `https://pokeapi.co/api/v2/pokemon/${Math.floor(1 + Math.random() * 151)}`

      const promise1 = axios.get(URL1)
      const promise2 = axios.get(URL2)
      const promise3 = axios.get(URL3)
      const promise4 = axios.get(URL4)
      const promise5 = axios.get(URL5)
      const promise6 = axios.get(URL6)
      const promise7 = axios.get(URL7)
      const promise8 = axios.get(URL8)

      Promise.all([promise1, promise2, promise3, promise4, promise5, promise6, promise7, promise8]).then(values => {
        // console.log(values)
        let image_list = []
        for(let i = 0; i < values.length; i++){
          let n = values[i].data.sprites.other["official-artwork"].front_default
          if(! sameURL(n)) {
            image_list.push(n)
          } else {
            i--;
          }
        }
        function sameURL(n) {
          return image_list.find((e) => (e === n));
        }

        // take image list make 2times = total 8 pairs of images
        let num = 1;
        while(num>0) {
          image_list = image_list.concat(image_list)
          num--
        }
        console.log(image_list)

        // shuffle them around in place OR randomly pick them


        // console.log(random_pokemon_image)
        // for-loop
        // .splice .pop (get rid of each url that's used)
        for (let i = 0; i < this.cardData.length; i++) {
          const random_pokemon_image = Math.floor(Math.random() * image_list.length);
          let random_img = image_list[random_pokemon_image]
          let random_name = 
          this.cardData[i].value = random_img
          let index = image_list.indexOf(random_img);
          if (index > -1) {
            image_list.splice(index, 1)
          }
        }
        console.log(image_list)
        // console.log(image_list[random_pokemon_image])
      })
    }
  },

  created: function(){
    this.listPokemon()
  }
})

new Vue({
  el: "#app",
})