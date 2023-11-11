<template>

  <Background/>

  <VueButton @mouseup="moveToDashboard" class="dashboard-button">&#x25C0; &nbsp; Dashboard</VueButton>
  <VueButton @click="moveToCheckout" class="checkout-button">
    Checkout
    <img class="cart-icon" src="../../../assets/img/shopping-cart.png" alt="Shopping cart icon.">
  </VueButton>

  <div class="center">
    <h1>Order History</h1>

    <div class="small-center scroll">

      <table>

        <tr v-for="item in orderHistory">
          <td style="padding-top: 20px;">
            <span style="font-weight: normal">{{item.order_date}} &nbsp;&nbsp;&nbsp;&nbsp;</span>
            {{ item.qty }} {{ getTitle(item.name, item.qty) }} &nbsp;&nbsp;&nbsp;&nbsp; {{ Math.round(item.price * item.qty) / 100 }}
            <br>
            <ul class="details" v-for="detail in formatDetails(item.details)">
              <li>{{ detail }}</li>
            </ul>
          </td>
          <td class="price">
            <VueButton @mouseup="addToCart(item)" class="add-to-cart" v-if="item.alreadyAdded">
              Added! Add again?
            </VueButton>
            <VueButton @mouseup="addToCart(item)" class="add-to-cart" v-else>
              Add to Cart
            </VueButton>
          </td>
        </tr>

      </table>
    </div>

  </div>

</template>

<script>
import Background from "@/components/Background.vue";
import VueButton from "@/components/Button.vue";

const SERVER_URL = "http://localhost:8000/"

export default {
  name: 'OrderHistory',
  components: {
    Background,
    VueButton,
  },
  data() {
    return {
      orderHistory: [
        {name: 'Berry Blast cone', price: 259, qty: 2, order_date: '01-01-2000'},
        {name: 'CYO cone', price: 499, qty: 1, order_date: '01-01-2000', details: {
            cone: 'waffle', scoops: ['chocolate', 'strawberry'], toppings: ['sprinkles']
          }
        },
        {name: 'Strawberry cheesecake cone', price: 259, qty: 1, order_date: '01-01-2000'},
        {name: "S'mores cone", price: 259, qty: 1, order_date: '01-01-2000'},
        {name: 'CYO cone', price: 499, qty: 1, order_date: '01-01-2000', details: {
            cone: 'waffle', scoops: ['chocolate', 'strawberry'], toppings: ['sprinkles']
          }
        },
        {name: 'CYO cone', price: 499, qty: 1, order_date: '01-01-2000', details: {
            cone: 'waffle', scoops: ['chocolate', 'strawberry'], toppings: ['sprinkles']
          }
        },
      ],
      cart: [],
    }
  },
  created() {
    if (this.$route.query.cart) {
      this.cart = JSON.parse(this.$route.query.cart);
    }

    const id = localStorage.getItem('userEmail');
    const token = localStorage.getItem('token');

    fetch(SERVER_URL + `orders/order_search?userID=${id}`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      }
        })
        .then(res => {
          return res.json();
        })
        .then(resp => {
          console.log(resp);
        })
        .catch(err => {
          console.log(`An error occurred: ${err}`);
        });
  },
  methods: {
    getTitle(name, qty) {
      if (qty > 1) {
        return `${name}s`;
      }
      return name;
    },
    moveToDashboard() {
      if (confirm("Are you sure you want to return to the dashboard? The contents of your cart will not be saved.")) {
        this.$router.push({path: '/dashboard', query: {}});
      }
    },
    moveToCheckout() {
      this.$router.push({path: '/customer/checkout', query: {cart: JSON.stringify(this.cart)}});
    },
    formatDetails(details) {
      if (details === undefined) {
        return;
      }
      let toReturn = [`${details.cone.charAt(0).toUpperCase() + details.cone.slice(1)} cone`];
      for (let i = 0; i < details.scoops.length; i++) {
        toReturn.push(`Scoop ${details.scoops[i]}`);
      }
      for (let i = 0; i < details.toppings.length; i++) {
        const toppingName = details.toppings[i];
        toReturn.push(toppingName.charAt(0).toUpperCase() + toppingName.slice(1));
      }
      return toReturn;
    },
    addToCart(item) {
      console.log(`Adding ${item.qty} of ${item.name} to the cart`);
      this.cart.push({name: item.name, price: item.price, qty: item.qty, details: item.details});
      item.alreadyAdded = true;
    },
  },
}
</script>

<style scoped>

div.scroll {
  overflow-x: hidden;
  overflow-y: auto;
}

.add-to-cart {
  font-size: 12pt;
  padding: 0;
  margin: 3pt;
}

input {
  width: 70%;
  height: 6%;
  display: inline-block;
}

hr {
  border: 2px solid black;
}

ul {
  list-style-type: none;
  line-height: .5em;
  margin-top: 2mm;
}

.price {
  text-align: right;
}

table {
  margin: 20px 40px 20px 20px;
  width: 95%;
}

td {
  vertical-align: bottom;
  border-bottom: black solid 1px;
}

.details {
  font-weight: normal;
  padding-left: 125px;
}

.dashboard-button {
  position: fixed;
  top: 12%;
  left: 2%;
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

.small-center {
  margin: auto;
  width: 50%;
  height: 55%;
  position: fixed;
  z-index: 1;
  top: 30%;
  left: 25%;
  color: rgba(40, 40, 40);
  font-weight: bold;
  text-align: left;
  background-color: rgba(244, 255, 256, .95);
}

h1 {
  margin-top: 3%;
  font-size: 20pt;
}

.checkout-button {
  position: fixed;
  top: 12%;
  left: 85%;
}

.cart-icon {
  width: 20%;
}


</style>
