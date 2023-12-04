<template>

  <Background/>

  <VueButton @click="moveToMenu" class="button0">&#x25C0; &nbsp; Menu</VueButton>
  <VueButton @click="moveToHistory" class="button1">&#x25C0; &nbsp; History</VueButton>

  <div class="center">
    <h1>Order Details</h1>

    <div class="small-center scroll">

      <table>

        <tr v-for="item in orderInfo">
          <td>
            {{ item.qty }} {{ getTitle(item.name, item.qty) }}
            &nbsp;&nbsp;&nbsp;<span @mouseup="removeFromCart(orderInfo.indexOf(item))">X</span>
            <br>
            <ul class="details" v-for="detail in formatDetails(item.details)">
              <li>{{ detail }}</li>
            </ul>
          </td>
          <td class="price">{{ Math.round(item.price * item.qty * 100) / 100 }}</td>
        </tr>

        <tr class="taxBox">
          <td>Tax</td>
          <td class="price">{{tax()}}</td>
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
          <td class="price">${{ Math.round((tax() + subTotal()) * 100) / 100 }}</td>
        </tr>

      </table>

    </div>

    <div class="address-field">
      <p style="display: inline-block; font-weight: normal">&nbsp;&nbsp;Delivery address &nbsp;&nbsp;</p>
      <input
          type="text"
          class="form-control"
          aria-label="Small"
          aria-describedby="inputGroup-sizing-sm"
          autocomplete="off"
          v-model.lazy.trim="address"
      >
    </div>

    <VueButton @mouseup="placeOrder" class="order-button">Purchase & Place Order</VueButton>

  </div>

</template>

<script>
import Background from "@/components/Background.vue";
import VueButton from "@/components/Button.vue";

const SALES_TAX_RATE = .07; //source: https://www.avalara.com/taxrates/en/state-rates/utah/cities/logan.html
const SERVER_URL = "http://localhost:8000/";

export default {
  name: 'Checkout',
  components: {
    Background,
    VueButton,
  },
  data() {
    return {
      orderInfo: [],
      address: '',
    }
  },
  created() {
    if (this.$route.query.cart) {
      this.orderInfo = JSON.parse(this.$route.query.cart);
    }
  },
  methods: {
    removeFromCart(index) {
      if (confirm("Are you sure you want to remove this item from your cart?")) {
        this.orderInfo = this.orderInfo.slice(0, index).concat(this.orderInfo.slice(index + 1));
      }
    },
    moveToMenu() {
      this.$router.push({path: '/customer/menu', query: {cart: JSON.stringify(this.orderInfo)}})
    },
    moveToHistory() {
      this.$router.push({path: '/customer/history', query: {cart: JSON.stringify(this.orderInfo)}})
    },
    placeOrder() {

      if (this.orderInfo.length <= 0) {
        alert("You cannot place an empty order!");
        return;
      }

      if (this.address === "") {
        alert("You must input a delivery address to place your order.");
        return;
      }

      const id = localStorage.getItem('userEmail');
      const token = localStorage.getItem('token');

      let body = {
        cones: [],
        userID: id,
        //droneID: 1,
        location: this.address,
      }

      for (let i = 0; i < this.orderInfo.length; i++) {
        for (let j = 0; j < this.orderInfo[i].qty; j++) {
          body.cones.push({
            cone: this.orderInfo[i].details.cone,
            toppings: this.orderInfo[i].details.toppings,
            iceCream: this.orderInfo[i].details.scoops,
            cost: this.orderInfo[i].price,
          });
        }
      }

      fetch(SERVER_URL + `drone_operator/get_delivering_drones?cone_count=${body.cones.length}`, {
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

            console.log(body.cones.length);
            console.log(resp);

            if (resp.error === "Not enough drones.") {
              alert("We're so sorry, but no drones are available at this time to complete your order. Please try again later.");
              return "no drones";
            }

            body.droneID = resp[0].id;

            console.log(this.orderInfo);

            console.log(body);

            return fetch(SERVER_URL + `orders/add`, {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
              },
              body: JSON.stringify(body)
            });
          })
          .then(res => {
            if (res === "no drones") {
              return "no drones";
            }
            return res.json();
          })
          .then(resp => {
            if (resp === "no drones") {
              return "no drones";
            }
            console.log(resp);

            const orderID = resp.orderID;
            console.log(orderID);
            this.$router.push({path: '/customer/track-order', query: {id: orderID}})
          })
          .catch(err => {
            console.log(`An error occurred: ${err}`);
            alert(`We're so sorry, an error occurred! Please reach out to customer support with the following information:\n${err}`);
          });
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
    getTitle(name, qty) {
      if (qty > 1) {
        return `${name}s`;
      }
      return name;
    },
    subTotal() {
      let subTotal = 0;
      for (let i = 0; i < this.orderInfo.length; i++) {
        subTotal += (this.orderInfo[i].price * this.orderInfo[i].qty);
      }
      return Math.round(subTotal * 100) / 100;
    },
    tax() {
      let theTax = SALES_TAX_RATE * this.subTotal();
      return Math.round(theTax * 100) / 100;
    },
  },
}
</script>

<style scoped>

div.scroll {
  overflow-x: hidden;
  overflow-y: auto;
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
}

.details {
  font-weight: normal;
}

.button0 {
  position: fixed;
  top: 12%;
  left: 20px;
  width: 150px;
}

.button1 {
  position: fixed;
  top: 20%;
  left: 20px;
  width: 150px;
}

.order-button {
  position: fixed;
  top: 83%;
  left: 36%;
  z-index: 1;
  width: 350px;
}

.address-field {
  position: fixed;
  top: 76%;
  left: 25%;
  width: 600px;
  font-weight: bolder;
  font-size: 16pt;
}

.center {
  margin: auto;
  width: 70%;
  height: 78%;
  position: fixed;
  z-index: 1;
  top: 15%;
  left: 20%;
  color: white;
  font-weight: bold;
  text-align: center;
  border-radius: 20px;
  background-color: rgba(17, 17, 17, .8);
}

.small-center {
  margin: auto;
  width: 64%;
  height: 40%;
  position: fixed;
  z-index: 1;
  top: 30%;
  left: 23%;
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
