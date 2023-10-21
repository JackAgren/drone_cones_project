<template>

  <table style="width:100%;">
    <tr>
      <td>

        <div class="small-center">
          <h3>Number of Scoops</h3>
          <p class="scoop-count"><span @click="decreaseScoops">&#x25C0;</span> {{scoopCount}} <span @click="increaseScoops">&#x25B6;</span></p>

          <h3>Flavor(s)</h3>
          <p class="descript">&#x25C0; Strawberry &#x25B6;</p>
          <p class="descript">&#x25C0; Strawberry &#x25B6;</p>
        </div>
      </td>
      <td>
        <div class="small-center">
          <h3>Cone</h3>
          <p class="descript">&#x25C0; Waffle &#x25B6;</p>
        </div>
        <div class="small-center">
          <h3>Toppings</h3>
          <p class="descript">&#x25C0; Cookie Dough &#x25B6;</p>
        </div>
        <VueButton @click="addToCart" class="add-to-cart">
          Add to Cart
          <img class="cart-icon" src="../../assets/img/shopping-cart.png" alt="Shopping cart icon.">
        </VueButton>

      </td>
    </tr>
  </table>

</template>

<script>
import Background from "@/components/Background.vue";
import VueButton from "@/components/Button.vue";

const MIN_SCOOPS = 1;
const MAX_SCOOPS = 4;

export default {
  name: 'Menu',
  components: {
    Background,
    VueButton,
  },
  data() {
    return {
      scoopCount: 2,
    }
  },
  methods: {
    addToCart() {
      //TODO: add to cart
    },
    increaseScoops() {
      if (this.scoopCount < MAX_SCOOPS) {
        this.scoopCount++;
      }
    },
    decreaseScoops() {
      if (this.scoopCount > MIN_SCOOPS) {
        this.scoopCount--;
      }
    }
  },
}
</script>

<style scoped>

.scoop-count {
  text-align: center;
  font-size: 30pt;
  cursor: pointer;
}

.descript {
  font-weight: normal;
  text-align: center;
}

.add-to-cart {
  position: absolute;
  left: 60%;
  top: 85%;
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
