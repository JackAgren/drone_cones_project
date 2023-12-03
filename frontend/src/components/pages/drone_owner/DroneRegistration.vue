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
                <th style="width: 15%">Size</th>
                <!-- <th style="width: 10%">Status</th> -->
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

                  <!-- <template v-if="row.col3 === 'Active'">
                    <td style="width: 10%;color:#7FFF00">{{ row.col3 }}</td>
                  </template>
                  <template v-else="row.col3 === 'Inactive'">
                    <td style="width: 10%;color:#FF4A3F">{{ row.col3 }}</td>
                  </template> -->
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <!-- <div id="buttonArea1">
          <VueButton>
            Activate
          </VueButton>
        </div> -->
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
  },

  mounted() {
    this.fetchDrones();
    // Add global click event listener
    document.addEventListener('click', this.deselectRow);
  },
  beforeDestroy() {
    // Remove global click event listener
    document.removeEventListener('click', this.deselectRow);
  },
  methods: {
   
    register_new() {
      this.$router.push({path: '/drone/registration/new', query: {}})
    },
    
    goBack() {
      this.$router.push({path: '/dashboard', query: {focus: 'drones'}})
    },


  fetchDrones() {
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

  const email = localStorage.getItem('userEmail');

  // Check if email is not null or undefined
  if (!email) {
    console.error('No email found');
    // Handle the case where the email is missing
    return;
  }

  // Use template literals to insert the email variable into the URL
  fetch(`http://localhost:8000/drone_operator/get_all_owned_drones?ownerID=${email}`, {
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
    this.processDroneData(data);
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
  });
},



processDroneData(droneData) {

this.rows = droneData.map((item, index) => {
return {
    col1: item.id,
    col2: item.size,
    col3: item.status,
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
