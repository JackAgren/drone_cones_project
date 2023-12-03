<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack" />
          <p id="contentHeader">Earnings</p>
        </div>

        <div id="infoArea">
          <p>Earnings to Date: ${{ earnings }}</p>
        </div>
      </div>
    </Background>
  </header>
</template>

<script>
import Background from '@/components/Background.vue'
import VueBackButton from '@/components/BackButton.vue'

export default {
  name: 'DroneEarnings',
  components: {
    Background,
    VueBackButton,
  },
  data() {
    return {
      earnings: 0,
      userID: 0
    }
  },
  mounted() {
    this.fetchUserID();
  },
  methods: {
    goBack() {
      this.$router.push({ path: '/dashboard', query: { focus: 'drones' } })
    },




    fetchEarnings(userID) {
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

  // Use template literals to insert the email variable into the URL
  fetch(`http://localhost:8000/orders/drone_earnings?droneID=${userID}`, {
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
    this.earnings = this.formatCurrency(data.earnings);
    
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
  });
},

  fetchUserID() {
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
  console.log(email);
  // Check if email is not null or undefined
  if (!email) {
    console.error('No id found');
    // Handle the case where the email is missing
    return;
  }

  // Use template literals to insert the email variable into the URL
  fetch(`http://localhost:8000/user/get_users?email=${email}`, {
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
    console.log(data.user.id);
    var userID = data.user.id; // -1 to account for ID offset by DJango.
    this.fetchEarnings(userID);
  })
  .catch(error => {
    console.error('There has been a problem with your fetch operation:', error);
  });
},


    formatCurrency(value) {
      return `${parseFloat(value).toFixed(2)}`;
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

.in-stock {
  color: rgb(115, 221, 67);
}

.out-of-stock {
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

#infoArea {
  text-align: center;
  margin-top: 170px;
  font-size: 24px;
}

.infoWrapper {
  display: grid;
  grid-template-columns: 135px min-content;
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
