<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack" />
          <p id="contentHeader">Manage Menu</p>
        </div>

        <div id="tableArea">
          <table v-if="!isTableEmpty">
            <thead>
              <tr>
                <th style="width: 10%">Item ID</th>
                <th style="width: 15%">Item Name</th>
                <th style="width: 15%">Item Type</th>
                <th style="width: 15%">Sales Price</th>
                <th style="width: 10%">Stock Status</th>
              </tr>
            </thead>
          </table>

          <div v-else class="emptyTableMessage">
            No Menu Items exist. Add a menu item by clicking the Add button
            below.
          </div>

          <div id="tableContent" :style="{ height: tableHeight + 'px' }">
            <table>
              <tbody>
                <tr
                  v-for="(row, index) in rows"
                  :key="index"
                  :class="[{ 'selected-row': selectedRowIndex === index }, index % 2 === 0 ? 'even-row' : 'odd-row']"
                  @click.stop="selectRow(index)"
                >
                  <td style="width: 10%">{{ row.col1 }}</td>
                  <td style="width: 15%">{{ row.col2 }}</td>
                  <td style="width: 15%">{{ row.col3 }}</td>
                  <td style="width: 15%">{{ row.col4 }}</td>
                  <td style="width: 10%" :class="getStatus(row.col5)">
                    {{ row.col5 }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div id="buttonArea">
          <VueButton @click="gotoAddMenuItem"> Add </VueButton>
          <VueButton
            class="marginButton"
            :class="{ 'button-disabled': selectedRowIndex === null }"
            :disabled="selectedRowIndex === null"
            @click="gotoEditMenuItem"
          >
            Edit
          </VueButton>
          <VueButton
            class="marginButton"
            :class="{ 'button-disabled': selectedRowIndex === null }"
            :disabled="selectedRowIndex === null"
            @click="gotoRemoveMenuItem"
          >
            Remove
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
name: 'ManageMenu',
components: {
  AppHeader,
  AppFooter,
  Background,
  VueButton,
  VueBackButton,
},
data() {
  return {
    maxHeight: 500, // Max height in pixels
    selectedRowIndex: null, // Index of the selected row
    rows: []
  }
},
computed: {
    tableHeight() {
      const rowHeight = 40; // Height of one row in pixels
      const totalRows = this.rows.length;
      const calculatedHeight = ((totalRows) * rowHeight);
      return Math.min(calculatedHeight, this.maxHeight); // Return the smaller of the two
    },

    isTableEmpty() {
      return this.rows.length === 0;
    },
  },

  mounted() {
    this.fetchMenu();
    // Add global click event listener
    document.addEventListener('click', this.deselectRow);
  },
  beforeDestroy() {
    // Remove global click event listener
    document.removeEventListener('click', this.deselectRow);
  },
  methods: {
    selectRow(index) {
      this.selectedRowIndex = index;
    },
    deselectRow(event) {
    // Get the clicked element
    const clickedElement = event.target;

    // Check if the clicked element is the back button, scroll, or restock button
    const isSpecialElement = clickedElement.closest('#backButton') ||
                             clickedElement.closest('#tableContent') ||
                             clickedElement.closest('#buttonArea');

    // Only deselect the row if a special element was not clicked
    if (!isSpecialElement) {
      this.selectedRowIndex = null;
    }
  },
    getStatus(status) {
      return status === 'In Stock' ? 'on' : 'off';
    },
    goBack() {
      this.$router.push({path: '/dashboard', query: {focus: `admin`}})
    },
    gotoAddMenuItem() {
      this.$router.push({path: `/admin/manageMenu/add`});
    },
    gotoRemoveMenuItem() {
      const selectedItem = this.rows[this.selectedRowIndex];
      const itemName = selectedItem ? selectedItem.col2 : ''; // Assuming col2 is the item name
      this.$router.push({
        path: `/admin/manageMenu/remove/${itemName}`
      });
    },
    gotoEditMenuItem() {
      const selectedItem = this.rows[this.selectedRowIndex];
      const itemName = selectedItem ? selectedItem.col2 : ''; // Assuming col2 is the item name
      this.$router.push({
        path: `/admin/manageMenu/edit/${itemName}`
      });
    },






    fetchMenu() {

      // Correctly set the authorization header
      const token = localStorage.getItem('token');
      if (!token) {
        console.error('No token found');
        // Handle the case where the token is missing
        return;
      }

      const authorizationHeaders = {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      };
    // Use your preferred method to fetch data, here's a fetch API example
    fetch('http://localhost:8000/inventory/inventory_search?description=ALL', {
        method: 'GET',
        headers: authorizationHeaders
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        this.processInventoryData(data);
      })
      .catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
      });
    },

    formatCurrency(value) {
      return `$${parseFloat(value).toFixed(2)}`;
    },

    processInventoryData(inventoryData) {
    this.rows = inventoryData.map((item, index) => {
      return {
          col1: index + 1, // Assuming the Item ID is the index + 1
          col2: item.description,
          col3: item.category,
          col4: this.formatCurrency(item.salesPrice), // Format cost per unit
          col5: item.quantity > 0 ? 'In Stock' : 'Out of Stock',
        };
      });
    },
  }
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
  margin-left: 100px;
  margin-right: 100px;
  z-index: 1;
  height: 750px;
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
  width: 600px;
  right: -145px;
  top: 738px;
  transform: translate(-50%, -50%);
}

.marginButton {
  margin-left: 25px;
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

.emptyTableMessage {
  color: white;
  text-align: center;
  margin-top: 250px;
  font-size: 30px;
}
</style>
