<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack" />
          <p id="contentHeader">Drone Registration</p>
        </div>

        <div id="tableArea">
          <table>
            <thead>
              <tr>
                <th style="width: 10%">Drone ID</th>
                <th style="width: 15%">Name</th>
                <th style="width: 15%">Size</th>
                <th style="width: 10%">Status</th>
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
                  <td style="width: 10%">{{ row.col1 }}</td>
                  <td style="width: 15%">{{ row.col2 }}</td>
                  <td style="width: 15%">{{ row.col3 }}</td>

                  <template v-if="row.col4 === 'Active'">
                    <td style="width: 10%;color:#7FFF00">{{ row.col4 }}</td>
                  </template>
                  <template v-else="row.col4 === 'Inactive'">
                    <td style="width: 10%;color:#FF4A3F">{{ row.col4 }}</td>
                  </template>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div id="buttonArea1">
          <VueButton>
            Activate
          </VueButton>
        </div>
        <div id="buttonArea2" @click="register_new">
          <WideButton>
            Register new drone
          </WideButton>
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
import WideButton from '@/components/WideButton.vue'


export default {
name: 'DroneRegistration',
components: {
  AppHeader,
  AppFooter,
  Background,
  VueButton,
  VueBackButton,
  WideButton
},
data() {
  return {
    maxHeight: 500, // Max height in pixels
    selectedRowIndex: null, // Index of the selected row
    rows: [
        { col1: '1', col2: 'DJI Avata', col3: 'Large', col4: 'Active'},
        { col1: '2', col2: 'Sky Rider', col3: 'Medium', col4: 'Active'},
        { col1: '3', col2: 'Ruko U11', col3: 'Small', col4: 'Inactive'},
        { col1: '4', col2: 'Falcon', col3: 'Large', col4: 'Active'},
        { col1: '5', col2: 'Falcon', col3: 'Small', col4: 'Active'},
        { col1: '6', col2: 'DJI Avata', col3: 'Large', col4: 'Active'},
        { col1: '7', col2: 'Sky Rider', col3: 'Large', col4: 'Active'},
        { col1: '8', col2: 'Ruko U11', col3: 'Small', col4: 'Active'},
        { col1: '9', col2: 'Falcon', col3: 'Large', col4: 'Active'},
        { col1: '10', col2: 'Potensic T25', col3: 'Small', col4: 'Active'},
        { col1: '11', col2: 'DJI Avata 2', col3: 'Small', col4: 'Active'},
        { col1: '12', col2: 'Sky Rider', col3: 'Medium', col4: 'Inactive'},
        { col1: '13', col2: 'Potensic T25', col3: 'Small', col4: 'Inactive'},
        { col1: '14', col2: 'Falcon', col3: 'Large', col4: 'Active'},
        { col1: '15', col2: 'Ruko U13', col3: 'Large', col4: 'Inactive'},
      ]
  }
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
  methods: {
    selectRow(index) {
      this.selectedRowIndex = index;
    },
    register_new() {
      this.$router.push({path: '/drone/registration/new', query: {}})
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
      return status === 'Active' ? 'active' : 'banned';
    },

    goBack() {
      this.$router.push({path: '/dashboard', query: {focus: 'drones'}})
    },

    gotoManageAccountsEdit() {
      this.$router.push({path: '../admin/manageAccounts/edit', query: {}})
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

#buttonArea1 {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  grid-column: 2/3;
  width: 400px;
  left: 50px;
  top: 710px;
}

#buttonArea2 {
  white-space: nowrap;
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  grid-column: 2/3;
  width: 400px;
  right: 80px;
  top: 710px;
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
