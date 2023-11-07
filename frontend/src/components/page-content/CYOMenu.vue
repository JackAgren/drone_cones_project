<template>

  <table style="width:100%;">
    <tr>
      <td>

        <div class="small-center">
          <h3>Number of Scoops</h3>

          <div style="padding-left: 25%;" class="no-highlight">
            <p @click="decreaseScoops" class="arrow-button" :style="checkIfDisabled('remove scoop')">&#x25C0;</p>
            <p class="scoop-count">{{scoopCount}}</p>
            <p @click="increaseScoops" class="arrow-button" :style="checkIfDisabled('add scoop')">&#x25B6;</p>
          </div>

          <h3>Flavor(s)</h3>
          <div v-for="scoop in scoopCount" style="padding-left: 10%;">
            <p @click="decreaseFlavor(scoop - 1)" class="arrow-button">&#x25C0;</p>
            <p class="flavor"> {{ scoops[scoop - 1] }} </p>
            <p @click="advanceFlavor(scoop - 1)" class="arrow-button">&#x25B6;</p>
            <img class="icecream" :src="getScoopLink(scoop - 1)">
          </div>

        </div>
      </td>
      <td>

        <div class="small-center">
          <h3>Cone</h3>

          <div style="padding-left: 25%;">
            <p @click="decreaseCone" class="arrow-button">&#x25C0;</p>
            <p class="cone-label"> {{ cone }} </p>
            <p @click="advanceCone" class="arrow-button">&#x25B6;</p>
            <img class="cone" :src="getConeLink()">
          </div>

        </div>

        <div class="small-center">
          <h3>Toppings</h3>

          <div>
            <p @click="decreaseTopping" class="arrow-button">&#x25C0;</p>
            <p class="cone-label">{{currentTopping}}</p>
            <p @click="advanceTopping" class="arrow-button">&#x25B6;</p>
            <img class="cone" :src="getToppingLink()">
          </div>

          <VueButton @mouseup="addTopping" class="add-topping">
            {{toppingButton}}
          </VueButton>

        </div>


        <VueButton @mouseup="addToCart()" class="add-to-cart">
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

import vanilla from "@/assets/ice-cream/vanilla.png";
import chocolate from "@/assets/ice-cream/chocolate.png";
import strawberry from "@/assets/ice-cream/strawberry.png";
import mint from "@/assets/ice-cream/mint.png";
import peanutbutter from "@/assets/ice-cream/peanutbutter.png";
import pistachio from "@/assets/ice-cream/pistachio.png";
import mystery from "@/assets/ice-cream/mystery.png";

import wafflebowl from "@/assets/img/waffle-bowl.png"
import sugarcone from "@/assets/img/sugar-cone.png"
import bowl from "@/assets/img/bowl.png";
import wafflecone from "@/assets/img/waffle-cone.png"

import cookiedough from "@/assets/img/cookie.png"
import oreo from "@/assets/img/oreo.png"
import sprinkles from "@/assets/img/sprinkles.png"
import sauce from "@/assets/img/choco-syrup.png"

const MIN_SCOOPS = 1;
const MAX_SCOOPS = 3;
const FLAVORS = ['Chocolate', 'Strawberry', 'Vanilla', 'Aggie Blue Mint', 'Peanut Butter', 'Pistachio', 'Mystery'];
const CONES = ['Waffle', 'Sugar', 'Waffle Bowl', 'Cup'];
const TOPPINGS = ['Cookie Dough', 'A Very Famous Chocolate Cookie', 'Sprinkles', 'Chocolate Sauce'];

export default {
  name: 'Menu',
  emits: 'sendToCart',
  components: {
    Background,
    VueButton,
  },
  data() {
    return {
      scoopCount: 2,
      scoops: ["Chocolate", "Chocolate", "Chocolate"],
      cone: "Sugar",
      toppings: [],
      currentTopping: "Cookie Dough",
      toppingButton: "Add",
    }
  },
  methods: {
    addTopping() {
      this.toppings.push(this.currentTopping);
      this.toppingButton = "Added!";
    },
    getConeLink() {
      switch(this.cone) {
        case "Waffle":
          return wafflecone;
        case "Sugar":
          return sugarcone;
        case "Waffle Bowl":
          return wafflebowl;
        default:
          return bowl;
      }
    },
    getToppingLink() {
      switch(this.currentTopping) {
        case "Cookie Dough":
          return cookiedough;
        case "A Very Famous Chocolate Cookie":
          return oreo;
        case "Chocolate Sauce":
          return sauce;
        default:
          return sprinkles;
      }
    },
    decreaseTopping() {
      this.toppingButton = "Add";
      const currentIndex = TOPPINGS.indexOf(this.currentTopping);
      if (currentIndex > 0) {
        this.currentTopping = TOPPINGS[currentIndex - 1];
      } else {
        this.currentTopping = TOPPINGS[TOPPINGS.length - 1];
      }
    },
    advanceTopping() {
      this.toppingButton = "Add";
      const currentIndex = TOPPINGS.indexOf(this.currentTopping);
      if (currentIndex < TOPPINGS.length - 1) {
        this.currentTopping = TOPPINGS[currentIndex + 1];
      } else {
        this.currentTopping = TOPPINGS[0];
      }
    },
    decreaseCone() {
      const currentIndex = CONES.indexOf(this.cone);
      if (currentIndex > 0) {
        this.cone = CONES[currentIndex - 1];
      } else {
        this.cone = CONES[CONES.length - 1];
      }
    },
    advanceCone() {
      const currentIndex = CONES.indexOf(this.cone);
      if (currentIndex < CONES.length - 1) {
        this.cone = CONES[currentIndex + 1];
      } else {
        this.cone = CONES[0];
      }
    },
    decreaseFlavor(index) {
      const currentIndex = FLAVORS.indexOf(this.scoops[index]);
      if (currentIndex > 0) {
        this.scoops[index] = FLAVORS[currentIndex - 1];
      } else {
        this.scoops[index] = FLAVORS[FLAVORS.length - 1];
      }
    },
    advanceFlavor(index) {
      const currentIndex = FLAVORS.indexOf(this.scoops[index]);
      if (currentIndex < FLAVORS.length - 1) {
        this.scoops[index] = FLAVORS[currentIndex + 1];
      } else {
        this.scoops[index] = FLAVORS[0];
      }
    },
    getScoopLink(index) {
      let name = this.scoops[index];
      switch(name) {
        case "Chocolate":
          return chocolate;
        case "Strawberry":
          return strawberry;
        case "Aggie Blue Mint":
          return mint;
        case "Peanut Butter":
          return peanutbutter;
        case "Pistachio":
          return pistachio;
        case "Mystery":
          return mystery;
        default:
          return vanilla;
      }
    },
    checkIfDisabled(button) {
      if ((button === 'remove scoop' && this.scoopCount === MIN_SCOOPS) || (button === 'add scoop' && this.scoopCount === MAX_SCOOPS)) {
        return "opacity: 50%";
      }
      return "";
    },
    calculatePrice() {
      return 499;
    },
    addToCart() {
      const item = {name: 'CYO cone', price: this.calculatePrice(), qty: 1, details: {
          cone: this.cone, scoops: this.scoops.slice(0, this.scoopCount), toppings: this.toppings
        }}

      console.log(item);
      this.$emit('sendToCart', item);
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

.add-topping {
  width: 45%;
  margin-bottom: 10px;
  margin-left: 60%;
}

.cone {
  width: 100px;
  display: block;
  margin: auto;
  padding-bottom: 10px;
}

.icecream {
  width: 75px;
  display: block;
  margin: auto;
  padding-bottom: 10px;
}

.no-highlight {
  user-select: none; /*chrome and Opera*/
  -moz-user-select: none; /*Firefox*/
  -webkit-text-select: none; /*IOS Safari*/
  -webkit-user-select: none; /*Safari*/
}

.scoop-count {
  text-align: center;
  font-size: 20pt;
  display: inline-block;
  padding-left: 20px;
  padding-right: 20px;
}

.flavor {
  text-align: center;
  display: inline-block;
  padding-left: 20px;
  padding-right: 20px;
}

.cone-label {
  text-align: center;
  display: inline-block;
  padding-left: 20px;
  padding-right: 20px;
}

.arrow-button {
  cursor: pointer;
  display: inline-block;
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
