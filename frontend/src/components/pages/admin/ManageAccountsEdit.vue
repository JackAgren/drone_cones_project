<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack" />
          <p id="contentHeader">Edit Account Status</p>
        </div>

        <div id="actionContentArea">
          <div id="infoArea1">
            <p class="infoLabel">Current User ID: {{ userID }}</p>
            <p class="infoLabel">email: {{ userEmail }}</p>
          </div>

          <div class="inputArea">
            <p>Account Type</p>
            <div class="input-wrapper3">
              <img id="downIcon" src="@/assets/downTriangle.png" />
              <select
                v-model="accountType"
                :class="{ 'placeholder-color': !accountType }"
                class="dropdown"
              >
                <option disabled value="">Select account type</option>
                <option>Customer</option>
                <option>Drone Owner</option>
                <option>Admin</option>
              </select>
            </div>
          </div>

          <div class="inputArea">
            <!-- <p>Account Status</p>
            <div class="input-wrapper3">
              <img id="downIcon" src="@/assets/downTriangle.png" />
              <select
                v-model="accountStatus"
                :class="{ 'placeholder-color': !accountStatus }"
                class="dropdown"
              >
                <option disabled value="">Select account status</option>
                <option>Active</option>
                <option>Banned</option>
              </select>
            </div> -->
          </div>
        </div>

        <div id="buttonArea">
          <VueButton
            :class="{ 'button-disabled': !accountType }"
            :disabled="!accountType"
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
name: 'ManageAccountsEdit',
components: {
  AppHeader,
  AppFooter,
  Background,
  VueButton,
  VueBackButton,
},
data() {
  return {
    userID: '',
    userEmail: '',
    accountType: '',
    accountStatus: '',
   };
},

methods: {


  goBack() {
      this.$router.push({path: '/admin/manageAccounts', query: {}})
    },



    fetchUser() {
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
  // Get userID from the URL parameters
  const userID = this.$route.params.description;

  fetch(`http://localhost:8000/user/get_users?id=${userID}`,{
        method: 'GET',
        headers: authorizationHeaders
      })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(user => {
      // Directly process the received user data
      this.processUserData(user);
    })
    .catch(error => {
      console.error('There has been a problem with your fetch operation:', error);
    });
},

processUserData(userData) {
  this.userID = userData.user.id;
  this.userEmail = userData.user.email;
},


    modifyUser() {
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

    const options = {
      method: 'POST',
      headers: authorizationHeaders,
      body: JSON.stringify({
        description: this.itemName,
        }),
      };

      fetch('http://localhost:8000/inventory/edit_user', options)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Remove successful:', data);
        this.$router.push({path: '/admin/manageMenu', query: {}})
      })
      .catch(error => {
        console.error('Remove failed:', error);
      });
    },





},

mounted() {
    this.fetchUser();
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
  height: 600px;
  width: 550px;
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
  top: 530px;
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

.inputArea {
  margin-top: 20px;
}

.inputArea p {
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

.input-wrapper2 {
  display: flex;
  align-items: center;
}

.input-wrapper3 {
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

.dropdown {
  border: none;
  border-radius: 25px;
  padding: 10px 20px;
  width: auto;
  min-width: 300px;
  background-color: rgb(29, 29, 29);
  color: white;
  font-family: sans-serif;
  font-weight: bold;
  transition: background-color 0.15s ease-in-out;
  appearance: none; /* Removes default arrow in some browsers */
  transition: background-color 0.15s ease-in-out;
}

.dropdown:hover {
  background-color: rgb(50, 50, 50); /* Slightly lighter background color */
}

.placeholder-color {
  color: rgba(209, 209, 209, 0.5); /* Your placeholder color */
}

#downIcon {
  height: 12px;
  width: auto;
  transform: translate(283px, 2px);
  z-index: 1;
  pointer-events: none;
}
</style>
