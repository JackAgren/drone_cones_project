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
                <p> Current Balance:
                    <span :class="balanceInfo.tagDisplayMode"
                      >{{ balanceInfo.sign}}{{ balanceInfo.absBalance }}</span>
                  </p>                    </div>
                <div class="balanceTag">
                  <p> Current Expenses:
                    <span :class="expensesInfo.tagDisplayMode"
                      >{{ expensesInfo.sign}}{{ expensesInfo.absExpenses }}</span>
                  </p>              
                </div>
              <div class="balanceTag">
                <p>
                  Current Earnings:
                  <span :class="earningsInfo.tagDisplayMode"
                    >{{ earningsInfo.sign}}{{ earningsInfo.absEarnings }}</span>
                </p>
              </div>
            </div>
          </div>

          <div id="rightHalf">
            <div id="salesHistoryTableArea" class="tableArea">
              <p id="contentHeader2">Earnings History</p>
              <table>
                <thead>
                  <tr>
                    <th style="width: 5%">Sale ID</th>
                    <th style="width: 5%">Amount</th>
                  </tr>
                </thead>
              </table>

              <div id="tableContent" :style="{ height: tableHeight + 'px' }">
                <table>
                  <tbody>
                    <tr
                      v-for="(row, index) in salesRows"
                      :key="index"
                      :class="[{ 'selected-row': selectedRowIndex === index }, index % 2 === 0 ? 'even-row' : 'odd-row']"
                      @click.stop="selectRow(index)"
                    >
                      <td style="width: 5%">{{ row.col1 }}</td>
                      <td
                        style="width: 5%"
                        :class="transactionColorings[index]"
                      >
                        {{ row.col2 }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div id="expensesHistoryTableArea" class="tableArea">
              <p id="contentHeader3">Expenses History</p>
              <table>
                <thead>
                  <tr>
                    <th style="width: 5%">Restock Item</th>
                    <th style="width: 5%">Amount</th>
                  </tr>
                </thead>
              </table>

              <div id="tableContent" :style="{ height: tableHeight2 + 'px' }">
                <table>
                  <tbody>
                    <tr
                      v-for="(row, index) in expenseRows"
                      :key="index"
                      :class="[{ 'selected-row': selectedRowIndex === index }, index % 2 === 0 ? 'even-row' : 'odd-row']"
                      @click.stop="selectRow(index)"
                    >
                      <td style="width: 5%">{{ row.col1 }}</td>
                      <td
                        style="width: 5%"
                        :class="transactionColorings2[index]"
                      >
                        {{ row.col2 }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- <div id="buttonArea">
              <VueButton id="generateReportButton"> Generate Report </VueButton>
            </div> -->
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
    balance: '',
    earnings: '',
    expenses: '',
    maxHeight: 440, // Max height in pixels
    selectedRowIndex: null, // Index of the selected row
    salesRows: [],
    expenseRows: [],
  }
},
methods: {
  goBack() {
      this.$router.push({path: '/dashboard', query: {focus: `admin`}})
    },
    
  fetchOrders() {
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

      fetch('http://localhost:8000/orders/order_search?order=ALL', {
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
          this.processOrdersData(data);
        })
        .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
        });
  },

  fetchRestocks() {
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

      fetch('http://localhost:8000/inventory/restock_report', {
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
          this.processRestockData(data);
        })
        .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
        });
  },

  fetchBalance() {
       const token = localStorage.getItem('token');
      if (!token) {
        console.error('No token found');
        return;
      }

      const authorizationHeaders = {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      };

      fetch('http://localhost:8000/orders/company_balance', {
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
          this.processBalanceData(data);
        })
        .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
        });
  },

  formatCurrency(value) {
    return `$${parseFloat(value).toFixed(2)}`;
  },

  processOrdersData(orderData) {
  this.salesRows = orderData.map(order => {
     // Calculate the total cost of all cones in the order.
     let totalCost = order.cones.reduce((sum, cone) => sum + cone.cost, 0);
    
    // Determine the prefix based on the cost being positive or negative.
    let prefix = totalCost >= 0 ? '+' : '-';

    return {
        col1: order.id, // Display the order ID.
        col2: prefix + this.formatCurrency(Math.abs(totalCost)) // Format the total cost with prefix.
      };
    });
  },

  processRestockData(restockData) {

  let prefix = '-';

  this.expenseRows = restockData.map(restock => {
    let itemName;
    if (!restock.item) {
      itemName = 'Unknown';
    } else {
      let match = restock.item.match(/\(([^)]+)\)/);
      itemName = match ? match[1] : 'Unknown'; // Use the NAME part if available, otherwise 'Unknown'
    }

    return {
        col1: itemName, // Use the extracted or default itemName for col1
        col2: prefix + this.formatCurrency(Math.abs(restock.cost)), // Format the total cost with prefix
      };
    });
},

  processBalanceData(data) {
  // Check if the data object has the necessary properties
  if (data.hasOwnProperty('balance') && data.hasOwnProperty('earnings')) {
    this.balance = this.formatCurrency(data.balance);
    this.earnings = this.formatCurrency(data.earnings);

    // If the 'expenses' property is present in the data, process it.
    if (data.hasOwnProperty('expenses')) {
      this.expenses = this.formatCurrency(data.expenses);
    } else {
      // Handle the case where 'expenses' data is missing or undefined.
      this.expenses = this.formatCurrency(0);
    }
  } else {
    console.error('Data object is missing required properties');
    this.balance = this.formatCurrency(0);
    this.earnings = this.formatCurrency(0);
    this.expenses = this.formatCurrency(0);
  }
},


  },
computed: {
    tableHeight() {
      const rowHeight = 40; // Height of one row in pixels.
      const totalRows = this.salesRows.length;
      const calculatedHeight = ((totalRows) * rowHeight);
      return Math.min(calculatedHeight, this.maxHeight); // Return the smaller of the two.
    },

    tableHeight2() {
      const rowHeight = 40; // Height of one row in pixels.
      const totalRows = this.expenseRows.length;
      const calculatedHeight = ((totalRows) * rowHeight);
      return Math.min(calculatedHeight, this.maxHeight); // Return the smaller of the two.
    },

    earningsInfo() {
      const earnings = parseFloat(this.earnings.replace(/[$,]/g, ''));
      const sign = earnings >= 0 ? '+' : '-';
      const tagDisplayMode = earnings >= 0 ? 'on' : 'off';
      const absEarnings = Math.abs(earnings).toLocaleString('en-US', {
      style: 'currency',
      currency: 'USD',
      });
      return { sign, tagDisplayMode, absEarnings };
    },

    expensesInfo() {
      const expenses = parseFloat(this.expenses.replace(/[$,]/g, ''));
      const sign = expenses >= 0 ? '-' : '+';
      const tagDisplayMode = expenses >= 0 ? 'off' : 'on';
      const absExpenses = expenses.toLocaleString('en-US', {
      style: 'currency',
      currency: 'USD',
      });
      return { sign, tagDisplayMode, absExpenses };
    },

    balanceInfo() {
      const balance = parseFloat(this.balance.replace(/[$,]/g, ''));
      const sign = balance >= 0 ? '+' : '-';
      const tagDisplayMode = balance >= 0 ? 'on' : 'off';
      const absBalance = Math.abs(balance).toLocaleString('en-US', {
      style: 'currency',
      currency: 'USD',
      });
      return { sign, tagDisplayMode, absBalance };
    },
    

    transactionColorings() {
      return this.salesRows.map(row => {
        return row.col2.startsWith('+') ? 'on' : 'off';
      });
   },

   transactionColorings2() {
      return this.expenseRows.map(row => {
        return row.col2.startsWith('+') ? 'on' : 'off';
      });
   },
  },

  mounted() {
    this.fetchBalance();
    this.fetchOrders();
    this.fetchRestocks();
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

#rightHalf {
  display: flex; 
  justify-content: space-around; 
  align-items: flex-start;
}

.balanceTag p {
  margin: 0;
  padding: 0;
  size: 40px;
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

#contentHeader2, #contentHeader3 {
  font-size: 20pt;
  pointer-events: none;
  user-select: none;
  text-align: center; /* Center the text horizontally */
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

.tableArea {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 50px;
  margin-right: 20px;
  position: relative;
  overflow-y: auto; 
  max-height: 750px;
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
