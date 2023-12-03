<template>

  <table>
    <tr v-for="row in featured" style="height: 50%;">

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
          {name: "S'mores", price: 0, image: featured0, css: 'featured-image f0', details: {
              cone: "Waffle", scoops: ["Vanilla", "Chocolate"], toppings: ["S'mores", "Chocolate Sauce"]
            }, inStock: false},
          {name: 'Berry Blast', price: 0, image: featured1, css: 'featured-image f1', details: {
              cone: "Waffle", scoops: ["Strawberry", "Strawberry"], toppings: ["Mixed Berries", "Sprinkles"]
            }, inStock: false},
        ],
        [
          {name: 'Strawberry Cheesecake', price: 0, image: featured2, css: 'featured-image f2', details: {
              cone: "Waffle", scoops: ["Cheesecake", "Cheesecake"], toppings: ["Strawberries"]
            }, inStock: false},
          {name: 'Peanut Butter', price: 0, image: featured3, css: 'featured-image f3', details: {
              cone: "Waffle", scoops: ["Peanut Butter", "Peanut Butter"], toppings: ["Oreo", "Chocolate Sauce"]
            }, inStock: false},
        ],
      ],
      inventory: undefined,
    }
  },
  methods: {
    checkStockForOrder(item) {

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
    addToCart(cone) {
      const item = {name: cone.name, price: cone.price, qty: 1, details: cone.details}

      if (this.inStock(item.details)) {
        console.log(item);
        this.$emit('sendToCart', item);

        alert("Added to cart!");
      } else {
        alert("Unfortunately this item is now out of stock! Please try again later.");
      }
    },
    inStock(item) {

      if (this.inventory.find(obj => { return obj.description === item.cone  && obj.quantity > 0}) === undefined) {
        return false;
      }

      for (let i = 0; i < item.scoops.length; i++) {
        if (this.inventory.find(obj => { return obj.description === item.scoops[i] && obj.quantity > 0}) === undefined) {
          console.log(item.scoops[i]);
          return false;
        }
      }

      for (let i = 0; i < item.toppings.length; i++) {
        if (this.inventory.find(obj => { return obj.description === item.toppings[i] && obj.quantity > 0}) === undefined) {
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


            for (let j = 0; j < this.featured[i].length; j++) {
              let thisFeatured = this.featured[i][j].details;
              let price = 0;

              for (let k = 0; k < thisFeatured.scoops.length; k++) {
                let theCost = this.inventory.find(obj => { return obj.description === thisFeatured.scoops[k]});
                if (theCost !== undefined) {
                  price += theCost.costPerUnit;
                }
              }

              for (let k = 0; k < thisFeatured.toppings.length; k++) {
                let theCost = this.inventory.find(obj => { return obj.description === thisFeatured.toppings[k]});
                if (theCost !== undefined) {
                  price += theCost.costPerUnit;
                }
              }

              let theCost = this.inventory.find(obj => { return obj.description === thisFeatured.cone});
              if (theCost !== undefined) {
                price += theCost.costPerUnit;
              }

              this.featured[i][j].price = price;
            }
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
  width: 60%;
}

.f3 {
  width: 65%;
}

.featured-image {
  display: block;
  margin: auto;
}

h3 {
  font-size: 11pt;
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
  height: 100%;
  outline: hotpink solid;
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
