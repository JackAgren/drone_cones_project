<template>

  <table>
    <tr v-for="row in featured" style="height: 40%;">

      <td v-for="item in row" style="width: 50%;">
        <div class="small-center">

          <div v-if="item.inStock">
            <h3>{{item.name}}</h3>
            <img :class="item.css" :src="item.image" alt="Photo of featured cone.">

            <div>
              <p class="featured-price">${{ Math.round(item.price * 100) / 100 }}</p>
              <div @click="addToCart(item)" class="this-button">
                &nbsp;<img class="cart-icon" src="../../assets/img/shopping-cart.png" alt="Shopping cart icon.">
              </div>
            </div>
          </div>

          <div v-else style="opacity: 30%;">
            <h3>{{item.name}}</h3>
            <img :class="item.css" :src="item.image" alt="Photo of featured cone.">

            <div>
              <p class="featured-price">${{ Math.round(item.price * 100) / 100 }}</p>
            </div>
          </div>

        </div>
      </td>

    </tr>
  </table>

</template>

<script>
import Background from "@/components/Background.vue";
import VueButton from "@/components/Button.vue";

import featured0 from '../../assets/img/featured0.png';
import featured1 from '../../assets/img/featured1.png';
import featured2 from '../../assets/img/featured2.png';
import featured3 from '../../assets/img/featured3.png';

export default {
  name: 'FeaturedMenu',
  emits: ['sendToCart'],
  components: {
    Background,
    VueButton,
  },
  data() {
    return {
      featured: [
        [
          {name: "S'mores", price: 1.23, image: featured0, css: 'featured-image f0', details: {
              cone: "Waffle", scoops: ["Vanilla", "Chocolate"], toppings: ["S'mores", "Chocolate Sauce"]
            }, inStock: false},
          {name: 'Berry Blast', price: 1.23, image: featured1, css: 'featured-image f1', details: {
              cone: "Waffle", scoops: ["Strawberry", "Strawberry"], toppings: ["Mixed Berries", "Sprinkles"]
            }, inStock: false},
        ],
        [
          {name: 'Strawberry Cheesecake', price: 1.23, image: featured2, css: 'featured-image f2', details: {
              cone: "Waffle", scoops: ["Cheesecake", "Cheesecake"], toppings: ["Strawberries"]
            }, inStock: false},
          {name: 'Peanut Butter', price: 1.23, image: featured3, css: 'featured-image f3', details: {
              cone: "Waffle", scoops: ["Peanut Butter", "Peanut Butter"], toppings: ["Oreo", "Chocolate Sauce"]
            }, inStock: false},
        ],
      ],
      inventory: undefined,
    }
  },
  methods: {
    addToCart(cone) {
      const item = {name: cone.name, price: cone.price, qty: 1, details: cone.details}

      console.log(item);
      this.$emit('sendToCart', item);

      alert("Added to cart!");
    },
    inStock(item) {

      console.log(item);

      if (this.inventory.find(obj => { return obj.description === item.cone}) === undefined) {
        return false;
      }

      for (let i = 0; i < item.scoops.length; i++) {
        if (this.inventory.find(obj => { return obj.description === item.scoops[i]}) === undefined) {
          console.log(item.scoops[i]);
          return false;
        }
      }

      for (let i = 0; i < item.toppings.length; i++) {
        if (this.inventory.find(obj => { return obj.description === item.toppings[i]}) === undefined) {
          console.log(item.toppings[i]);
          return false;
        }
      }

      return true;
    },
  },
  created() {
    const token = localStorage.getItem('token');
    fetch('http://localhost:8000/inventory/inventory_search?description=ALL', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      },
    })
        .then(res => {
          return res.json();
        })
        .then(resp => {
          this.inventory = resp;

          for (let i = 0; i < this.featured.length; i++) {
            this.featured[i][0].inStock = this.inStock(this.featured[i][0].details);
            this.featured[i][1].inStock = this.inStock(this.featured[i][1].details);
          }
        });
  }
}
</script>

<style scoped>

.featured-price {
  margin: 0;
  position: absolute;
  top: 87%;
  display: inline-block;
}

.this-button img {
  width: 80%;
}

.this-button {
  margin: 0;
  display: inline-block;
  width: 20%;
  height: 18%;
  border-radius: 15px;
  padding: 5px 5px 5px 5px;
  cursor: pointer;
  background-color: rgb(115, 221, 67);
  color: white;
  transition: background-color 0.3s;
  float: right;
  position: absolute;
  left: 75%;
  top: 75%;
}

.this-button:hover {
  background-color:  rgb(64, 126, 36);
}

.f0 {
  width: 60%;
}

.f1 {
  width: 60%;
}

.f2 {
  width: 55%;
}

.f3 {
  width: 65%;
}

.featured-image {
  display: block;
  margin: auto;
}

h3 {
  font-size: 12pt;
  text-align: center;
  margin-top: 2mm;
}

.small-center {
  padding: 10px 10px 0 10px;
  margin: 10px;
  color: rgba(40, 40, 40);
  font-weight: bold;
  text-align: left;
  background-color: rgba(244, 255, 256, .95);
  position: relative;
}

.cart-icon {
  width: 20%;
}

input {
  width: 70%;
  height: 6%;
  display: inline-block;
}

hr {
  border: 2px solid black;
}

h2 {
  margin-top: 3%;
  font-size: 18pt;
}


</style>
