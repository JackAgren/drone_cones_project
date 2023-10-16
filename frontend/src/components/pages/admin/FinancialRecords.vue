<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack" />
          <p id="contentHeader">Financial Records</p>
        </div>

        <div id="splitContentArea">
          <div id="leftHalf">
            <div id="balanceArea">
              <p id="contentHeader2">Balance</p>
              <div class="balanceTag">
                <p>Current Balance: $1,00,000.00</p>
              </div>
              <div class="balanceTag">
                <p>Starting Current Month Balance: $100,000.00</p>
              </div>
              <div class="balanceTag">
                <p>
                  Current Month Earnings:
                  <span :class="earningsInfo.tagDisplayMode" id="earningsTag"
                    >{{ earningsInfo.sign



                    }}{{ earningsInfo.absEarnings }}</span
                  >
                </p>
              </div>
            </div>
          </div>

          <div id="rightHalf">
            <div id="tableArea">
              <p id="contentHeader2">Transaction History</p>
              <table>
                <thead>
                  <tr>
                    <th style="width: 10%">Transaction ID</th>
                    <th style="width: 15%">Transaction Type</th>
                    <th style="width: 15%">Description</th>
                    <th style="width: 10%">Amount</th>
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
                      <td
                        style="width: 10%"
                        :class="transactionColorings[index]"
                      >
                        {{ row.col4 }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div id="buttonArea">
              <VueButton id="generateReportButton"> Generate Report </VueButton>
            </div>
          </div>
        </div>
      </div>
    </Background>
  </header>
</template>

<script>
import '../../../assets/style.css';
import AppHeader from '@/components/Header.vue';
import AppFooter from '@/components/Footer.vue';
import Background from '@/components/Background.vue';
import VueButton from '@/components/Button.vue';
import VueBackButton from '@/components/BackButton.vue';


export default {
name: 'FinancialRecords',
components: {
  AppHeader,
  AppFooter,
  Background,
  VueButton,
  VueBackButton,
},
data() {
  return {
    earnings: '900,000.00',
    maxHeight: 440, // Max height in pixels
    selectedRowIndex: null, // Index of the selected row
    rows: [
        { col1: '1512', col2: 'Order', col3: 'OrderID: 5153', col4: '+$10.42'},
        { col1: '1511', col2: 'Order', col3: 'OrderID: 1234', col4: '+$15.42'},
        { col1: '1510', col2: 'Order', col3: 'OrderID: 8642', col4: '+$5.11'},
        { col1: '1509', col2: 'Order', col3: 'OrderID: 5152', col4: '+$1.99'},
        { col1: '1508', col2: 'Lease Payment', col3: 'Lease payment to Drone Owner - 12', col4: '-$50.00'},
        { col1: '1507', col2: 'Lease Payment', col3: 'Lease payment to Drone Owner - 57', col4: '-$25.00'},
        { col1: '1506', col2: 'Menu Restock', col3: 'Vanilla Ice Cream refill', col4: '-$15.67'},
        { col1: '1505', col2: 'Order', col3: 'OrderID: 5555', col4: '+$20.11'},
        { col1: '1504', col2: 'Order', col3: 'OrderID: 6666', col4: '+$13.37'},
        { col1: '1503', col2: 'Order', col3: 'OrderID: 2561', col4: '+$1.00'},
        { col1: '1502', col2: 'Order', col3: 'OrderID: 5523', col4: '+$15.28'},
        { col1: '1501', col2: 'Lease Payment', col3: 'Lease payment to Drone Owner - 42', col4: '-$50.00'},
        { col1: '1500', col2: 'Menu Restock', col3: 'Chocolate Ice Cream refill', col4: '-$50.99'},
        { col1: '1499', col2: 'Menu Restock', col3: 'Waffle Cone refill', col4: '-$10.00'},
        { col1: '1498', col2: 'Lease Payment', col3: 'Lease payment to Drone Owner - 11', col4: '-$10.00'},
        { col1: '1497', col2: 'Order', col3: 'OrderID: 5153', col4: '+$10.42'},

      ]
  }
},
methods: {
  goBack() {
      this.$router.push({path: '/dashboard', query: {}})
    },
  },
computed: {
    tableHeight() {
      const rowHeight = 40; // Height of one row in pixels
      const totalRows = this.rows.length;
      const calculatedHeight = ((totalRows) * rowHeight);
      return Math.min(calculatedHeight, this.maxHeight); // Return the smaller of the two
    },
    earningsInfo() {
      const earnings = parseFloat(this.earnings.replace(/[$,]/g, ''));
      const sign = earnings >= 0 ? '+' : '-';
      const tagDisplayMode = earnings >= 0 ? 'positive' : 'negative';
      const absEarnings = Math.abs(earnings).toLocaleString('en-US', {
      style: 'currency',
      currency: 'USD',
      });
      return { sign, tagDisplayMode, absEarnings };
    },
    transactionColorings() {
      return this.rows.map(row => {
        return row.col4.startsWith('+') ? 'positive' : 'negative';
      });
   },
  },
}
</script>

<style scoped>
#splitContentArea {
  display: grid;
  grid-template-columns: auto 1fr;
}

#leftHalf {
  margin-left: 20px;
}

.balanceTag p {
  margin: 0;
  padding: 0;
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
  z-index: 2;
  height: 750px;
}

#contentHeader {
  transform: translate(19px, -2px);
  font-size: 30pt;
  pointer-events: none;
  user-select: none;
}

#contentHeader2 {
  font-size: 20pt;
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

#generateReportButton {
  width: 220px;
}

#tableArea {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 40px;
  margin-right: 20px;
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
