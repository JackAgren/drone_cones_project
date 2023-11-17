<template>
  <header class="tablePageContent">
    <Background>
      <div id="tableContentArea">
        <div id="backButtonArea">
          <VueBackButton id="backButton" @click="goBack" />
          <p id="contentHeader">Register</p>
        </div>

        <div id="actionContentArea">
          <div class="inputArea">
            <p>Email</p>
            <div class="input-wrapper2">
              <input
                type="email"
                placeholder="Enter your email"
                v-model="email"
              />
            </div>
            <p v-if="invalidEmail" style="color: red">Email is not valid.</p>
          </div>

          <div class="inputArea">
            <p>Password</p>
            <div class="input-wrapper2">
              <input
                type="password"
                placeholder="Enter password"
                v-model="password"
              />
            </div>
          </div>

          <div class="inputArea">
            <p>Confirm Password</p>
            <div class="input-wrapper2">
              <input
                type="password"
                placeholder="Re-enter password"
                v-model="confirmPassword"
              />
            </div>
            <p v-if="showPasswordMismatchMessage" style="color: red">
              The passwords do not match.
            </p>
          </div>

          <div class="inputArea">
            <p>Address</p>
            <div class="input-wrapper2">
              <input
                type="text"
                placeholder="Enter your address"
                v-model="address"
              />
            </div>
          </div>

          <div class="inputArea">
            <p>City</p>
            <div class="input-wrapper2">
              <input type="text" placeholder="Enter your city" v-model="city" />
            </div>
          </div>

          <div class="inputArea">
            <p>State</p>
            <div class="input-wrapper2">
              <input
                type="text"
                placeholder="Enter your state"
                v-model="state"
              />
            </div>
          </div>

          <div class="inputArea">
            <p>Zip Code</p>
            <div class="input-wrapper2">
              <input
                type="text"
                placeholder="Enter your zip code"
                v-model="zip"
              />
            </div>
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
        </div>

        <div id="buttonArea">
          <div v-if="isProcessing" class="processing-text">
            Processing . . .
          </div>
          <VueButton
            v-else
            :class="{ 'button-disabled': !isFormComplete }"
            :disabled="!isFormComplete"
            @click="addUser"
          >
            Register
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
name: 'RegistrationCustomer',
components: {
  AppHeader,
  AppFooter,
  Background,
  VueButton,
  VueBackButton,
},
data() {
  return {
      accountType: '',
      email: '',
      password: '',
      confirmPassword: '',
      address: '',
      city: '',
      state: '',
      zip: '',
      is_staff: '',
      is_superuser: '',
      showPasswordMismatchMessage: '',
      isProcessing: '',
      invalidEmail: '',
  };
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

  isValidEmail() {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(this.email.toLowerCase());
  },

  goBack() {
    this.$router.push({path: '/', query: {}})
  },


  addUser() {

    if (!this.isValidEmail()) {
    this.invalidEmail = true;
   }else{
    this.invalidEmail = false;
   }


    if (this.password !== this.confirmPassword) {
      this.showPasswordMismatchMessage = true;
    }else{
      this.showPasswordMismatchMessage = false;
    }

    this.isProcessing = true;

    if(this.invalidEmail || this.showPasswordMismatchMessage)
    {
      this.isProcessing = false;
      return;
    }

    if (this.accountType === 'Admin') {
    this.is_superuser = true;
    this.is_staff = false;
  } else if (this.accountType === 'Drone Owner') {
    this.is_superuser = false;
    this.is_staff = true;
  } else {
    this.is_superuser = false;
    this.is_staff = false;
  }

 // Construct the data object to send
 const userData = {
    email: this.email,
    password: this.password,
    confirmPassword: this.confirmPassword,
    address: this.address,
    city: this.city,
    state: this.state,
    zip: this.zip,
    accountType: this.accountType,
    is_staff: this.is_staff,
    is_superuser: this.is_superuser
  };

  const options = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(userData)
  };

    fetch('http://localhost:8000/user/create_account', options)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      console.log('Registration successful:', data);

      if (data.token) {
        localStorage.setItem('token', data.token);
        localStorage.setItem('userEmail', this.email);
      }

      this.$router.push({path: '/dashboard', query: {}})
    })
    .catch(error => {
      console.error('Registration failed:', error);
    })
    .finally(() => {
      this.isProcessing = false;
    });
  },

},

computed: {
  isFormComplete() {
        return this.email && this.password && this.confirmPassword &&
           this.accountType !== '' && this.address &&
           this.city && this.state && this.zip;
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
  height: 1000px;
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
  top: 920px;
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

input {
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

input::placeholder {
  color: rgb(209, 209, 209); /* Sets the placeholder text color to grey */
}

input:focus {
  outline: none; /* Removes the default focus outline */
  border: 2px solid rgb(0, 162, 255); /* Sets the border color to green */
}

input:hover {
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
  appearance: none;
}

.dropdown:hover {
  background-color: rgb(50, 50, 50);
}

.placeholder-color {
  color: rgba(209, 209, 209, 0.5);
}

#downIcon {
  height: 12px;
  width: auto;
  transform: translate(283px, 2px);
  z-index: 1;
  pointer-events: none;
}

.processing-text {
  color: white;
  text-align: center;
  font-size: 24px;
  transform: translateX(-170px);
  user-select: none;
}
</style>
