<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack" />
          <p id="contentHeader">Pending Drone Operator Lease Payments</p>
        </div>

        <div id="tableArea">
          <table>
            <thead>
              <tr>
                <th style="width: 10%">Drone ID</th>
                <th style="width: 15%">Drone Owner ID</th>
                <th style="width: 15%">Drone Size Class</th>
                <th style="width: 10%">Earnings Due</th>
              </tr>
            </thead>
          </table>

          <div id="tableContent" :style="{ height: tableHeight + 'px' }">
            <table>
              <tbody>
                <tr
                  v-for="(row, index) in rows"
                  :key="index"
                  :class="[{ 'selected-row': selectedRowIndex === index }, index % 2 === 0 ? 'even-row' : 'odd-row']"
                  @click.stop="selectRow(index)"
                >
                  <td style="width: 10%">{{}}</td>
                  <td style="width: 15%">{{ ownerID }}</td>
                  <td style="width: 15%">{{ size }}</td>
                  <td style="width: 10%">{{}}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <div id="buttonArea">
          <VueButton
            :class="{ 'button-disabled': isPayButtonDisabled }"
            :disabled="isPayButtonDisabled"
            @click="gotoPayLease"
          >
            Pay Lease
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
name: 'ManageLeasePayments',
components: {
  AppHeader,
  AppFooter,
  Background,
  VueButton,
  VueBackButton,
},
data() {
  return {
    ownerID:0,
    size:'',
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
  isPayButtonDisabled() {
    if (this.selectedRowIndex === null) {
      return true;
    }
      return this.rows[this.selectedRowIndex].col4 !== 'Unpaid';
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
      return status === 'Paid' ? 'on' : 'off';
    },
    goBack() {
      this.$router.push({path: '/dashboard', query: {focus: `admin`}})
    },
    gotoPayLease() {
      this.$router.push({path: '/admin/manageLeasePayments/paylease', query: {}})
    },

    fetchDrones() {
      fetch('http://localhost:8000/drone_operator/get_all_owned_drones')
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          this.processDroneData(data);
        })
        .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
        });
    },





    processDroneData(itemData) {
      if (!itemData || itemData.length === 0) return;
      const item = itemData[0]; // Assuming the first item is the one we need
      // Update the data properties with the item details
      this.ownerID = item.ownerID;
      this.size = item.size; // Assuming the type is available

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
  width: 400px;
  right: -150px;
  top: 738px;
  transform: translate(-50%, -50%);
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
</style>
