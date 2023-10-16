<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack"/>
          <p id="contentHeader">Edit</p>
        </div>

        <div id="actionContentArea">
          <div id="infoArea1">
            <p class="infoLabel">Item to edit: Peanuts</p>
            <p class="infoLabel">Current Sales Price: $0.50</p>
          </div>

          <div id="inputArea1">
            <p>New Sales Price</p>
            <div class="input-wrapper">
              <!-- Wrapper div -->
              <span class="dollar-sign">$</span>
              <!-- Dollar sign -->
              <input
                type="text"
                placeholder="Enter new sales price"
                min="0"
                v-model="newSalesPrice"
                @keypress="isPositiveDecimal($event)"
              />
            </div>
          </div>
        </div>

        <div id="buttonArea">
          <VueButton
            :class="{ 'button-disabled': !newSalesPrice }"
            :disabled="!newSalesPrice"
          >
            Apply
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
name: 'ManageMenuEdit',
components: {
  AppHeader,
  AppFooter,
  Background,
  VueButton,
  VueBackButton,
},
data() {
  return {
    newSalesPrice: null, // New data property
  }
},

methods: {
  isPositiveDecimal(event) {
    const charCode = (event.which) ? event.which : event.keyCode;
    const value = event.target.value;

    // Allow only one decimal point (46) and numbers (48-57)
    if (charCode === 46 && value.indexOf('.') !== -1) {
      event.preventDefault();
      return;
    }

    if (charCode !== 46 && (charCode < 48 || charCode > 57)) {
      event.preventDefault();
    }

    // Restrict to two decimal places
    if (charCode === 46 || (charCode >= 48 && charCode <= 57)) {
      const parts = value.split('.');
      if (parts.length > 1 && parts[1].length >= 2) {
        event.preventDefault();
      }
    }
  },
  goBack() {
      this.$router.push({path: '/admin/manageMenu', query: {}})
    },
},

computed: {
  tableHeight() {
      const rowHeight = 40; // Height of one row in pixels
      const totalRows = this.rows.length;
      const calculatedHeight = ((totalRows) * rowHeight);
      return Math.min(calculatedHeight, this.maxHeight); // Return the smaller of the two
    },
  },

  mounted() {
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

input[type="text"] {
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
  padding-left: 25px;
}

.input-wrapper {
  display: flex;
  align-items: center;
  transform: translateX(-16px);
}

.dollar-sign {
  margin-right: 5px;
  color: white;
  font-family: sans-serif;
  font-weight: bold;
  transform: translateX(24px);
}

input[type="text"]::placeholder {
  color: rgb(209, 209, 209); /* Sets the placeholder text color to grey */
}

input[type="text"]:focus {
  outline: none; /* Removes the default focus outline */
  border: 2px solid rgb(0, 162, 255); /* Sets the border color to green */
}

input[type="text"]:hover {
  background-color: rgb(50, 50, 50); /* Slightly lighter background color */
}
</style>
