<template>

  <div class="grid-container">

    <div class="item2 small-center scoops">
        <h3>Number of Scoops</h3>

        <div style="align-content: center;" class="no-highlight">
          <p @click="decreaseScoops" class="arrow-button" :style="checkIfDisabled('remove scoop')">&#x25C0;</p>
          <p class="scoop-count">{{scoopCount}}</p>
          <p @click="increaseScoops" class="arrow-button" :style="checkIfDisabled('add scoop')">&#x25B6;</p>
        </div>

        <h3>Flavor(s)</h3>
        <div v-for="scoop in scoopCount" style="align-content: center;">
          <p @click="decreaseFlavor(scoop - 1)" class="arrow-button">&#x25C0;</p>
          <p class="flavor"> {{ scoops[scoop - 1] }} </p>
          <p @click="advanceFlavor(scoop - 1)" class="arrow-button">&#x25B6;</p>
          <img class="icecream" :src="getScoopLink(scoop - 1)">
        </div>

    </div>

    <div class="item3 small-center">
        <h3>Cone</h3>

        <div style="align-content: center;">
          <p @click="decreaseCone" class="arrow-button">&#x25C0;</p>
          <p class="cone-label"> {{ cone }} </p>
          <p @click="advanceCone" class="arrow-button">&#x25B6;</p>
          <img class="cone" :src="getConeLink()">
        </div>

    </div>

    <div class="item5 small-center">
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

  </div>

  <VueButton @mouseup="addToCart()" class="add-to-cart">
    {{addButton}}
    <img class="cart-icon" src="../../assets/img/shopping-cart.png" alt="Shopping cart icon.">
  </VueButton>

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
const TOPPINGS = ['Cookie Dough', 'Oreo', 'Sprinkles', 'Chocolate Sauce'];

export default {
  name: 'CYOMenu',
  emits: ['sendToCart'],
  components: {
    Background,
    VueButton,
  },
  data() {
    return {
      scoopCount: 2,
      scoops: [],
      cone: "",
      toppings: [],
      currentTopping: "Cookie Dough",
      toppingButton: "Add",
      addButton: "Add to Cart",
      inventory: undefined,
      flavors: [],
      toppings_stock: [],
      cones_stock: [],
    }
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

          for (let i = 0; i < FLAVORS.length; i++) {
            if (this.inventory.find(obj => { return obj.description === FLAVORS[i] && obj.quantity > 0}) !== undefined) {
              this.flavors.push(FLAVORS[i]);
            }
          }

          for (let i = 0; i < TOPPINGS.length; i++) {
            if (this.inventory.find(obj => { return obj.description === TOPPINGS[i] && obj.quantity > 0}) !== undefined) {
              this.toppings_stock.push(TOPPINGS[i]);
            }
          }

          for (let i = 0; i < CONES.length; i++) {
            if (this.inventory.find(obj => { return obj.description === CONES[i] && obj.quantity > 0}) !== undefined) {
              this.cones_stock.push(CONES[i]);
            }
          }

          this.scoops = [this.flavors[0], this.flavors[0], this.flavors[0]];
          this.currentTopping = this.toppings_stock[0];
          this.cone = this.cones_stock[0];
        });
  },
  methods: {
    inStock(item) {

      console.log(item);

      const cone = this.inventory.find(obj => { return obj.description === item.cone && obj.quantity > 0});
      if (cone === undefined) {
        console.log(cone);
        return false;
      } else {
        const index = this.inventory.indexOf(cone);
        this.inventory[index].quantity = this.inventory[index].quantity - 1;
      }

      for (let i = 0; i < item.scoops.length; i++) {
        const scoop = this.inventory.find(obj => { return obj.description === item.scoops[i] && obj.quantity > 0});
        if (scoop === undefined) {
          console.log(item.scoops[i]);
          return false;
        } else {
          const index = this.inventory.indexOf(scoop);
          this.inventory[index].quantity = this.inventory[index].quantity - 1;
        }
      }

      for (let i = 0; i < item.toppings.length; i++) {
        const topping = this.inventory.find(obj => { return obj.description === item.toppings[i] && obj.quantity > 0});
        if (topping === undefined) {
          console.log(item.toppings[i]);
          return false;
        } else {
          const index = this.inventory.indexOf(topping);
          this.inventory[index].quantity = this.inventory[index].quantity - 1;
        }
      }

      return true;
    },
    addTopping() {
      this.toppings.push(this.currentTopping);
      this.toppingButton = "Added!";
      this.addButton = "Add to Cart";
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
        case "Oreo":
          return oreo;
        case "Chocolate Sauce":
          return sauce;
        default:
          return sprinkles;
      }
    },
    decreaseTopping() {
      this.toppingButton = "Add";
      this.addButton = "Add to Cart";
      const currentIndex = this.toppings_stock.indexOf(this.currentTopping);
      if (currentIndex > 0) {
        this.currentTopping = this.toppings_stock[currentIndex - 1];
      } else {
        this.currentTopping = this.toppings_stock[this.toppings_stock.length - 1];
      }
    },
    advanceTopping() {
      this.toppingButton = "Add";
      this.addButton = "Add to Cart";
      const currentIndex = this.toppings_stock.indexOf(this.currentTopping);
      if (currentIndex < this.toppings_stock.length - 1) {
        this.currentTopping = this.toppings_stock[currentIndex + 1];
      } else {
        this.currentTopping = this.toppings_stock[0];
      }
    },
    decreaseCone() {
      this.addButton = "Add to Cart";
      const currentIndex = this.cones_stock.indexOf(this.cone);
      if (currentIndex > 0) {
        this.cone = this.cones_stock[currentIndex - 1];
      } else {
        this.cone = this.cones_stock[this.cones_stock.length - 1];
      }
    },
    advanceCone() {
      this.addButton = "Add to Cart";
      const currentIndex = this.cones_stock.indexOf(this.cone);
      if (currentIndex < this.cones_stock.length - 1) {
        this.cone = this.cones_stock[currentIndex + 1];
      } else {
        this.cone = this.cones_stock[0];
      }
    },
    decreaseFlavor(index) {
      this.addButton = "Add to Cart";
      const currentIndex = this.flavors.indexOf(this.scoops[index]);
      if (currentIndex > 0) {
        this.scoops[index] = this.flavors[currentIndex - 1];
      } else {
        this.scoops[index] = this.flavors[this.flavors.length - 1];
      }
    },
    advanceFlavor(index) {
      this.addButton = "Add to Cart";
      const currentIndex = this.flavors.indexOf(this.scoops[index]);
      if (currentIndex < this.flavors.length - 1) {
        this.scoops[index] = this.flavors[currentIndex + 1];
      } else {
        this.scoops[index] = this.flavors[0];
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

      let price = 0;

      for (let i = 0; i < this.scoopCount; i++) {
        //add price of this.scoops[i] to price
        let theCost = this.inventory.find(obj => { return obj.description === this.scoops[i]});
        if (theCost !== undefined) {
          price += theCost.costPerUnit;
        }
      }

      for (let i = 0; i < this.toppings.length; i++) {
        //add price of this.toppings[i] to price
        let theCost = this.inventory.find(obj => { return obj.description === this.toppings[i]});
        if (theCost !== undefined) {
          price += theCost.costPerUnit;
        }
      }

      //add price of this.cone to price
      let theCost = this.inventory.find(obj => { return obj.description === this.cone});
      if (theCost !== undefined) {
        price += theCost.costPerUnit;
      }

      return price;
    },
    addToCart() {
      if (this.toppings.length === 0) {
        alert("It's no fun to have a cone with no toppings! Add at least one to continue :)");
        return;
      }
      const item = {name: 'CYO cone', price: this.calculatePrice(), qty: 1, details: {
          cone: this.cone, scoops: this.scoops.slice(0, this.scoopCount), toppings: this.toppings
        }};

      if (this.inStock(item.details)) {
        this.$emit('sendToCart', item);
        this.addButton = "Added! Add again?";
      } else {
        alert("Unfortunately this item is now out of stock! Please try again later.");
      }
    },
    increaseScoops() {
      this.addButton = "Add to Cart";
      if (this.scoopCount < MAX_SCOOPS) {
        this.scoopCount++;
      }
    },
    decreaseScoops() {
      this.addButton = "Add to Cart";
      if (this.scoopCount > MIN_SCOOPS) {
        this.scoopCount--;
      }
    }
  },
}
</script>

<style scoped>

.item2 { grid-area: menu; }
.item3 { grid-area: main; }
.item5 { grid-area: footer; }

.grid-container {
  display: grid;
  grid-template-areas:
    'menu menu menu main main main'
    'menu menu menu footer footer footer';
  gap: 5px;
  padding: 5px;
  margin-bottom: 20px;
}

.grid-container > div {
  text-align: center;
  padding: 5px 0;
}

.scoops {
  height: 100%;
}

.add-topping {
  width: 45%;
  margin-bottom: 10px;
  margin-left: 50%;
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
  position: relative;
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
