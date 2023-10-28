<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack"/>
          <p id="contentHeader">Manage Menu</p>
        </div>

        <div id="tableArea">
          <table>
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
    rows: [
        { col1: '1', col2: 'Vanilla Ice Cream', col3: 'Ice Cream', col4: '$1.00/Scoop', col5: 'In Stock' },
        { col1: '2', col2: 'Chocolate Ice Cream', col3: 'Ice Cream', col4: '$1.50/Scoop', col5: 'In Stock' },
        { col1: '3', col2: 'Mint Ice Cream', col3: 'Ice Cream', col4: '$1.25/Scoop', col5: 'Out of Stock' },
        { col1: '4', col2: 'Strawberry Ice Cream', col3: 'Ice Cream', col4: '$2.00/Scoop', col5: 'In Stock' },
        { col1: '5', col2: 'Waffle Cone', col3: 'Container', col4: '$0.50/Cone', col5: 'In Stock' },
        { col1: '6', col2: 'Sugar Cone', col3: 'Container', col4: '$0.75/Cone', col5: 'In Stock' },
        { col1: '7', col2: 'Bowl', col3: 'Container', col4: '$1.00/Bowl', col5: 'Out of Stock' },
        { col1: '8', col2: 'Rainbow Sprinkles', col3: 'Topping', col4: '$0.10/Item', col5: 'In Stock' },
        { col1: '9', col2: 'Chocolate Sprinkles', col3: 'Topping', col4: '$0.10/Item', col5: 'In Stock' },
        { col1: '10', col2: 'Peanuts', col3: 'Topping', col4: '$0.20/Item', col5: 'Out of Stock' },
        { col1: '11', col2: 'Watermelon Ice Cream', col3: 'Ice Cream', col4: '$41.00/Scoop', col5: 'In Stock' },
        { col1: '12', col2: 'Orange Ice Cream', col3: 'Ice Cream', col4: '$15.00/Scoop', col5: 'Out of Stock' },
        { col1: '13', col2: 'Rocky Road Ice Cream', col3: 'Ice Cream', col4: '$11.00/Scoop', col5: 'In Stock' },
        { col1: '14', col2: 'Oreo Ice Cream', col3: 'Ice Cream', col4: '$15.00/Scoop', col5: 'In Stock' },
        { col1: '15', col2: 'Mystery Ice Cream', col3: 'Ice Cream', col4: '$12.00/Scoop', col5: 'In Stock' },

        // Add more rows as needed
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
      this.$router.push({path: '/admin/manageMenu/add', query: {}})
    },
    gotoRemoveMenuItem() {
      this.$router.push({path: '/admin/manageMenu/remove', query: {}})
    },
    gotoEditMenuItem() {
      this.$router.push({path: '/admin/manageMenu/edit', query: {}})
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
</style>
