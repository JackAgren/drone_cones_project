<template>

  <Background/>

  <VueButton @mouseup="moveToDashboard" class="dashboard-button">&#x25C0; &nbsp; Dashboard</VueButton>
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
          <FeaturedMenu @sendToCart="addToOrder"/>
        </td>

        <td>
          <!--<CYOMenu @addToCart($event)/>-->
          <CYOMenu @sendToCart="addToOrder"/>
        </td>

      </tr>
    </table>

  </div>

</template>

<script>
import Background from "@/components/Background.vue";
import VueButton from "@/components/Button.vue";
import FeaturedMenu from "@/components/page-content/FeaturedMenu.vue";
import CYOMenu from "@/components/page-content/CYOMenu.vue";

export default {
  name: 'Menu',
  components: {
    FeaturedMenu,
    Background,
    VueButton,
    CYOMenu,
  },
  data() {
    return {
      cart: [],
    }
  },
  created() {
    if (this.$route.query.cart) {
      this.cart = JSON.parse(this.$route.query.cart);
    }
  },
  methods: {
    addToOrder(item) {
      console.log("we got it!");
      console.log(item);
      this.cart.push(item);
    },
    moveToDashboard() {
      if (confirm("Are you sure you want to return to the dashboard? The contents of your cart will not be saved.")) {
        this.$router.push({path: '/dashboard', query: {}})
      }
    },
    moveToCheckout() {
      this.$router.push({path: '/customer/checkout', query: {cart: JSON.stringify(this.cart)}})
    },
  },
}
</script>

<style scoped>

h3 {
  font-size: 12pt;
  text-align: center;
  margin-top: 2mm;
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
