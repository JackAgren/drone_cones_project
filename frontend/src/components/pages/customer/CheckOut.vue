<template>

  <Background/>

  <VueButton @click="moveToDashboard" class="dashboard-button">&#x25C0; &nbsp; Menu</VueButton>

  <div class="center">
    <h1>Order Details</h1>

    <div class="small-center">

      <table>

        <tr v-for="item in orderInfo">
          <td>
            {{ item.qty }} {{ item.name }}
            <br>
            <ul class="details" v-for="detail in formatDetails(item.details)">
              <li>{{ detail }}</li>
            </ul>
          </td>
          <td class="price">{{ Math.round(item.price * item.qty) / 100 }}</td>
        </tr>

        <tr class="taxBox">
          <td>Tax</td>
          <td class="price">{{tax}}</td>
        </tr>

        <tr>
          <td>
            <hr/>
          </td>
          <td>
            <hr/>
          </td>
        </tr>

        <tr>
          <td></td>
          <td class="price">${{total}}</td>
        </tr>

      </table>

      <p style="display: inline-block; font-weight: normal">&nbsp;&nbsp;Delivery address &nbsp;&nbsp;</p>
      <input type="text" class="form-control" aria-label="Small" aria-describedby="inputGroup-sizing-sm">

    </div>

    <VueButton @click="placeOrder" class="order-button">Purchase & Place Order</VueButton>

  </div>

</template>

<script>
import Background from "@/components/Background.vue";
import VueButton from "@/components/Button.vue";

export default {
  name: 'Checkout',
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
      ]
    }
  },
  methods: {
    moveToDashboard() {
      this.$router.push({path: '/customer/menu', query: {}})
    },
    placeOrder() {
      //TODO: place order
      this.$router.push({path: '/customer/track-order', query: {}})
    },
    formatDetails(details) {
      if (details === undefined) {
        return;
      }
      console.log(JSON.stringify(details));
      let toReturn = [`${details.cone.charAt(0).toUpperCase() + details.cone.slice(1)} cone`];
      for (let i = 0; i < details.scoops.length; i++) {
        toReturn.push(`1 scoop ${details.scoops[i]}`);
      }
      for (let i = 0; i < details.toppings.length; i++) {
        const toppingName = details.toppings[i];
        toReturn.push(toppingName.charAt(0).toUpperCase() + toppingName.slice(1));
      }
      return toReturn;
    },
  },
  computed: {
    tax() {
      //TODO: calc tax
      return 1.03;
    },
    total() {
      //TODO: calc total
      return 12.41;
    },
  }
}
</script>

<style scoped>

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
}

.details {
  font-weight: normal;
}

.dashboard-button {
  position: fixed;
  top: 12%;
  left: 2%;
}

.order-button {
  position: fixed;
  top: 80%;
  left: 36%;
  z-index: 1;
  width: 350px;
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
  height: 45%;
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


</style>
