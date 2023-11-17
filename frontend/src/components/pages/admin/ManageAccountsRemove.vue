<template>
  <div id="standardLayout">
    <AppHeader />
    <header class="tablePageContent">
      <div id="pageContent">
        <div id="cloudsArea">
          <img id="clouds1" src="@/assets/clouds1.png" />
          <img id="clouds2" src="@/assets/clouds2.png" />
          <img id="clouds3" src="@/assets/clouds3.png" />
          <img id="clouds4" src="@/assets/clouds1.png" />
        </div>

        <div id="tableContentArea">
          <div id="backButtonArea">
            <VueBackButton id="backButton" @click="goBack" />
            <p id="contentHeader">Remove</p>
          </div>

          <div id="actionContentArea">
            <div id="infoArea1">
              <p class="infoLabel">
                Confirm removal of following user account: {{ userEmail }}
              </p>
            </div>
          </div>

          <div id="buttonArea">
            <VueButton @click="removeUser">Remove</VueButton>
          </div>
        </div>
      </div>
    </header>
    <AppFooter />
  </div>
</template>

<script>
import '../../../assets/style.css';
import AppHeader from '@/components/Header.vue';
import AppFooter from '@/components/Footer.vue';
import VueButton from '../../Button.vue'
import VueBackButton from '../../BackButton.vue'


export default {
name: 'ManageMenuRemove',
components: {
  AppHeader,
  AppFooter,
  VueButton,
  VueBackButton,
},
data() {
  return {
    newSalesPrice: null,
    userEmail: '',
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

  removeUser() {

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
      method: 'DELETE',
      headers: authorizationHeaders,
      body: JSON.stringify({
        email: this.userEmail,
        }),
      };

      fetch('http://localhost:8000/user/delete_account', options)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Remove successful:', data);
        this.$router.push({path: '/admin/manageAccounts', query: {}})
      })
      .catch(error => {
        console.error('Remove failed:', error);
      });
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
    this.fetchUser();
  },

}
</script>

<style scoped>
#standardLayout {
  display: grid;
  grid-template-rows: auto 1fr auto;
  height: 100vh;
}

.tablePageContent {
  display: grid;
  grid-template-rows: 1fr;
}

#pageContent {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr auto;
  width: 100%;
  background-image: url("@/assets/sky.png");
  background-size: 100% 100%;
  background-repeat: repeat-x;
  overflow: hidden;
}

#cloudsArea {
  position: absolute;
  display: flex;
  height: auto;
  grid-column: 1/4;
}

#clouds1 {
  position: absolute;
  top: 150px;
  animation: cloudAnimation1 60s linear infinite;
  animation-delay: -10s;
  padding-left: 40px;
}

#clouds2 {
  animation: cloudAnimation2 60s linear infinite;
  animation-delay: -25s;
}

#clouds3 {
  position: absolute;
  top: 240px;
  animation: cloudAnimation3 80s linear infinite;
  animation-delay: -25s;
}

#clouds4 {
  animation: cloudAnimation3 60s linear infinite;
  animation-delay: -40s;
}

@keyframes cloudAnimation1 {
  from {
    transform: translateX(-100%); /* Start off-screen to the left */
  }
  to {
    transform: translateX(300%); /* Move off-screen to the right */
  }
}

@keyframes cloudAnimation2 {
  from {
    transform: translateX(-100%); /* Start off-screen to the left */
  }
  to {
    transform: translateX(500%); /* Move off-screen to the right */
  }
}

@keyframes cloudAnimation3 {
  from {
    transform: translateX(-500%); /* Start off-screen to the left */
  }
  to {
    transform: translateX(300%); /* Move off-screen to the right */
  }
}

@keyframes cloudAnimation4 {
  from {
    transform: translateX(-500%); /* Start off-screen to the left */
  }
  to {
    transform: translateX(500%); /* Move off-screen to the right */
  }
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
  margin-top: 100px;
  margin-bottom: 100px;
  margin-left: auto;
  margin-right: auto;
  z-index: 1;
  height: 300px;
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
  top: 225px;
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
