<template>

  <Background/>

  <VueButton @click="moveToDashboard" class="dashboard-button">&#x25C0; &nbsp; Menu</VueButton>
  <VueButton @click="moveToCheckout" class="checkout-button">
    Checkout
    <img class="cart-icon" src="../../../assets/img/shopping-cart.png" alt="Shopping cart icon.">
  </VueButton>

  <div class="center">

    <table class="outer-table">
      <tr>
        <td style="width: 50%"><h2>Featured</h2></td>
        <td><h2>Create Your Own</h2></td>
      </tr>

      <tr>

        <td>
          <table>
            <tr v-for="row in featured" style="height: 40%;">

              <td v-for="item in row" style="width: 50%;">
                <div class="small-center">

                  <h3>{{item.name}}</h3>
                  <img :class="item.css" :src="item.image" alt="Photo of featured cone.">

                  <div>
                    <p class="featured-price">${{ Math.round(item.price) / 100 }}</p>
                    <div @click="addToCart" class="this-button">
                      &nbsp;<img class="cart-icon" src="../../../assets/img/shopping-cart.png" alt="Shopping cart icon.">
                    </div>
                  </div>

                </div>
              </td>

            </tr>
          </table>
        </td>

        <td>
          <table style="width:100%;">
            <tr>
              <td>

                <div class="small-center">
                  <h3>Number of Scoops</h3>
                  <p style="text-align: center">&#x25C0; 2 &#9658;</p>

                  <h3>Flavor(s)</h3>
                  <p class="descript">&#x25C0; Strawberry &#9658;</p>
                  <p class="descript">&#x25C0; Strawberry &#9658;</p>
                </div>
              </td>
              <td>
                <div class="small-center">
                  <h3>Cone</h3>
                  <p class="descript">&#x25C0; Waffle &#9658;</p>
                </div>
                <div class="small-center">
                  <h3>Toppings</h3>
                  <p class="descript">&#x25C0; Cookie Dough &#9658;</p>
                </div>
                <VueButton @click="addToCart" class="add-to-cart">
                  Add to Cart
                  <img class="cart-icon" src="../../../assets/img/shopping-cart.png" alt="Shopping cart icon.">
                </VueButton>

              </td>
            </tr>
          </table>
        </td>

      </tr>
    </table>

  </div>

</template>

<script>
import Background from "@/components/Background.vue";
import VueButton from "@/components/Button.vue";

import featured0 from '../../../assets/img/featured0.png';
import featured1 from '../../../assets/img/featured1.png';
import featured2 from '../../../assets/img/featured2.png';
import featured3 from '../../../assets/img/featured3.png';

export default {
  name: 'Menu',
  components: {
    Background,
    VueButton,
  },
  data() {
    return {
      orderInfo: [
        {name: 'Berry Blast cone', price: 259, qty: 2},
        {name: 'CYO cone', price: 499, qty: 1, details: {
            cone: 'waffle', scoops: ['chocolate', 'strawberry'], toppings: ['sprinkles']
          }}
      ],
      featured: [
        [
          {name: "S'mores", price: 123, image: featured0, css: 'featured-image f0'},
          {name: 'Berry Blast', price: 123, image: featured1, css: 'featured-image f1'},
        ],
        [
          {name: 'Strawberry Cheesecake', price: 123, image: featured2, css: 'featured-image f2'},
          {name: 'Peanut Butter', price: 123, image: featured3, css: 'featured-image f3'},
        ],
      ],
    }
  },
  methods: {
    moveToDashboard() {
      this.$router.push({path: '/customer/menu', query: {}})
    },
    moveToCheckout() {
      this.$router.push({path: '/customer/checkout', query: {}})
    },
    addToCart() {
      //TODO: add to cart
    },
  },
}
</script>

<style scoped>

.descript {
  font-weight: normal;
  text-align: center;
}

.add-to-cart {
  position: absolute;
  left: 60%;
  top: 85%;
}

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

.outer-table {
  margin: 20px 20px 20px 20px;
  width: 95%;
}

.dashboard-button {
  position: fixed;
  top: 12%;
  left: 2%;
}

.checkout-button {
  position: fixed;
  top: 12%;
  left: 85%;
}

.center {
  margin: auto;
  width: 70%;
  height: 70%;
  position: fixed;
  z-index: 1;
  top: 20%;
  left: 15%;
  color: white;
  font-weight: bold;
  text-align: center;
  border-radius: 20px;
  background-color: rgba(17, 17, 17, .8);
}

h2 {
  margin-top: 3%;
  font-size: 18pt;
}


</style>
