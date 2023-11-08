<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack" />
          <p id="contentHeader">Restock</p>
        </div>

        <div id="actionContentArea">
          <div id="infoArea1">
            <p class="infoLabel">Item to restock: {{ itemName }}</p> <!-- Binding itemName -->
            <p class="infoLabel">Item Type: {{ itemType }}</p> <!-- Binding itemType -->
            <p class="infoLabel">Current Quantity: {{ currentQuantity }} Gallons</p> <!-- Binding currentQuantity -->
            <p class="infoLabel">Cost per Unit: {{ costPerUnit }}</p> <!-- Binding costPerUnit -->
          </div>

          <div id="inputArea1">
            <p>Quantity to Purchase</p>
            <input
              type="number"
              placeholder="Enter quantity to purchase"
              min="0"
              v-model="quantityToPurchase"
              @keypress="isNumber($event)"
            />
          </div>

          <div id="infoArea2">
              <div class="infoWrapper">
                <p class="infoLabel">Restock Cost:</p>
                <p class="infoValue">{{ restockCost }}</p>
              </div>
              <div class="infoWrapper">
                <p class="infoLabel">Tax:</p>
                <p class="infoValue">{{ tax }}</p>
              </div>
              <div class="infoWrapper">
                <p class="infoLabel">Total Cost:</p>
                <p class="infoValue">{{ totalCost }}</p>
            </div>
          </div>
        </div>

        <div id="buttonArea">
          <VueButton
            :class="{ 'button-disabled': !quantityToPurchase }"
            :disabled="!quantityToPurchase"
            @click="restockItem"
          >
            Restock
          </VueButton>
          
        </div>
      </div>
    </Background>
  </header>
</template>

<script>
import '../../../assets/style.css';
import AppHeader from '@/components/Header.vue';
import AppFooter from '@/components/Footer.vue';
import Background from '@/components/Background.vue'
import VueButton from '@/components/Button.vue'
import VueBackButton from '@/components/BackButton.vue'


export default {
name: 'ManageInventoryRestock',
components: {
  AppHeader,
  AppFooter,
  Background,
  VueButton,
  VueBackButton,
},
data() {
  return {
    quantityToPurchase: null,
    restockCost: 0,
    tax: 0,
    totalCost: 0,
    itemName: '',
    itemType: '',
    currentQuantity: 0,
    costPerUnit: 0,
  }
},

watch: {
  quantityToPurchase(newValue, oldValue) {
    if (newValue !== oldValue) {
      this.updateCosts();
    }
  }
},

methods: {
  isNumber(event) {
    var keyCode = (event.keyCode ? event.keyCode : event.which);
    if (keyCode < 48 || keyCode > 57) { // 48-57 are the key codes for numbers 0-9
      event.preventDefault();
    }
  },
    goBack() {
      this.$router.push({path: '/admin/manageInventory', query: {}})
    },

    fetchItem() {
      const itemName = this.$route.params.description;
      fetch(`http://localhost:8000/inventory/inventory_search?description=${itemName}`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          this.processItemData(data);
        })
        .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
        });
    },

    formatCurrency(value) {
      return `$${parseFloat(value).toFixed(2)}`;
    },

    processItemData(itemData) {
      if (!itemData || itemData.length === 0) return;
      const item = itemData[0]; // Assuming the first item is the one we need
      // Update the data properties with the item details
      this.itemName = item.description;
      this.itemType = item.category; // Assuming the type is available
      this.currentQuantity = item.quantity;
      this.costPerUnit = this.formatCurrency(item.costPerUnit);

      // Assuming quantityToPurchase is defined and updated elsewhere in your component
      const restockCost = this.quantityToPurchase * parseFloat(item.costPerUnit);
      const taxRate = 0.03; // 3% tax rate for Utah
      const tax = restockCost * taxRate;
      const totalCost = restockCost + tax;

      // Update the component's data properties
      this.restockCost = this.formatCurrency(restockCost);
      this.tax = this.formatCurrency(tax);
      this.totalCost = this.formatCurrency(totalCost);
  },

  updateCosts() {
      const restockCost = this.quantityToPurchase * parseFloat(this.costPerUnit.replace('$', ''));
      const taxRate = 0.03; // Update tax rate as needed
      const tax = restockCost * taxRate;
      const totalCost = restockCost + tax;

      this.restockCost = this.formatCurrency(restockCost);
      this.tax = this.formatCurrency(tax);
      this.totalCost = this.formatCurrency(totalCost);
    },
  
    restockItem() {
    const options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        description: this.itemName,
        quantity: this.quantityToPurchase,
        }),
      };

      fetch('http://localhost:8000/inventory/update_item', options)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Restock successful:', data);
        // Handle successful restock here (e.g., show a success message, update UI)
        this.$router.push({path: '/admin/manageInventory', query: {}})
      })
      .catch(error => {
        console.error('Restock failed:', error);
        // Handle errors here (e.g., show an error message)
      });
    },

  


},

  mounted() {
    this.fetchItem();
    // Add global click event listener
    document.addEventListener('click', this.deselectRow);
  },
  beforeDestroy() {
    // Remove global click event listener
    document.removeEventListener('click', this.deselectRow);
  },

}
</script>

<style scoped>
.tablePageContent {
  display: grid;
  grid-template-rows: 1fr;
}

#backButtonArea {
  display: flex;
}

#tableContentArea {
  position: relative;
  display: flex;
  flex-direction: column;
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 20px;
  color: white;
  font-family: sans-serif;
  font-weight: bold;
  grid-column: 2/3;
  padding-top: 20px;
  padding-left: 20px;
  padding-right: 20px;
  margin-top: 35px;
  margin-bottom: 35px;
  margin-left: auto;
  margin-right: auto;
  z-index: 1;
  height: 550px;
  width: 500px;
}

#contentHeader {
  transform: translate(19px, -2px);
  font-size: 30pt;
  pointer-events: none;
  user-select: none;
}

#buttonArea {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  grid-column: 2/3;
  width: 400px;
  right: -90px;
  top: 480px;
}

#tableArea {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 40px;
  margin-right: 40px;
  position: relative;
}

#tableContent {
  overflow-y: auto;
  height: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
  user-select: none;
}

th,
td {
  padding-top: 8px;
  padding-bottom: 8px;
  text-align: center;
}

th {
  border-bottom: 3px solid white;
  font-size: 18pt;
  position: sticky;
  top: 0;
  z-index: 1;
}

.even-row {
  background-color: #00000094;
}

.odd-row {
  background-color: #3535358f;
}

.selected-row {
  background-color: rgb(0, 174, 255);
}

#tableContent tbody tr:not(.selected-row):hover {
  background-color: rgba(173, 216, 230, 0.3);
  transition: background-color 0.1s ease-in-out;
}

#tableContent tbody tr {
  transition: background-color 0.1s ease-in-out;
}

.on {
  color: rgb(115, 221, 67);
}

.off {
  color: rgb(255, 57, 57);
}

.button-disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.infoLabel {
  margin: 0;
}

#actionContentArea {
  margin-left: 70px;
}

#inputArea1 {
  margin-top: 20px;
}

#inputArea1 p {
  margin-bottom: 9px;
}

#infoArea2 {
  margin-top: 20px;
}

.infoWrapper {
  display: grid;
  grid-template-columns: 120px min-content;
}

.infoLabel {
  margin: 0;
  grid-column: 1;
}

.infoValue {
  margin: 0;
  grid-column: 2;
  text-align: left; /* Left-aligned */
}

input[type="number"] {
  border: none; /* Removes the border */
  border-radius: 25px; /* Makes the input corners rounded */
  padding: 10px 20px; /* Padding to make it look like a capsule */
  width: auto; /* Auto width to fit content */
  min-width: 300px; /* Minimum width to fit placeholder text */
  background-color: rgb(29, 29, 29); /* Sets the background color to black */
  color: white; /* Sets the input text color to white */
  font-family: sans-serif;
  font-weight: bold;
  transition: background-color 0.15s ease-in-out;
  margin-left: 0px;
}

input[type="number"]::placeholder {
  color: rgb(209, 209, 209); /* Sets the placeholder text color to grey */
}

input[type="number"]:focus {
  outline: none; /* Removes the default focus outline */
  border: 2px solid rgb(0, 162, 255); /* Sets the border color to green */
}

input[type="number"]:hover {
  background-color: rgb(50, 50, 50); /* Slightly lighter background color */
}
</style>
