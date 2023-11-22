<template>
  <div class="header">
    <img id="headerLogo" src="@/assets/headerLogo.png" />
    <div id="loginButtonArea" @click="toggleDropdown">
      <p class="headerText" id="usernameTag"
         @click="isLoggedIn ? null : gotoLogin()">
        {{ isLoggedIn ? username : 'Login' }}
      </p>
      <img
        v-if="isLoggedIn"
        id="downIcon"
        :class="{ 'flipped': showDropdown }"
        src="@/assets/downTriangle.png"
      />
      <transition name="expand">
        <div v-if="showDropdown" class="dropdown">
          <div class="headerText dropdownText" @click.stop="logout">Logout</div>
          <img id="logoutIcon" src="@/assets/logout.png" />
        </div>
      </transition>
    </div>
  </div>
</template>


<script>
export default {
  name: 'AppHeader',
  data() {
    return {
      isLoggedIn: false,
      username: '',
      showDropdown: false
    };
  },
  methods: {
    toggleDropdown() {
      if (this.isLoggedIn) {
        this.showDropdown = !this.showDropdown;
      }
    },
    logout() {
      this.isLoggedIn = false;
      this.showDropdown = false;
      if(localStorage.getItem('userEmail') === 'Guest') {
        this.guestLogout();
        localStorage.removeItem('token');
        localStorage.removeItem('userEmail');
      
        this.$router.push({path: '/'})
      }
      else
      {
        // Remove token and userEmail from localStorage
        localStorage.removeItem('token');
        localStorage.removeItem('userEmail');
      
        this.$router.push({path: '/'})
      }
    },

    guestLogout() {
      // Correctly set the authorization header
      const token = localStorage.getItem('token');
      if (!token) {
        console.error('No token found');
        // Handle the case where the token is missing
        return;
      }


      const options = {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json','Authorization': `Token ${token}` },
        // body: JSON.stringify(loginData),
      };

      fetch('http://localhost:8000/user/delete_guest',options)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => {
          if (data.token) {
            this.isLoggedIn = false;
            this.showDropdown = false;
            }
        })
        .catch(error => {
          console.error('Login failed:', error);
          this.loginError = 'Invalid email or password. Please try again.';
          this.isLoggingIn = false; // Reset the login state on failure
        });
    },

    gotoLogin() {
      this.$router.push({path: '/login', query: {}})
    },
  },

  mounted() {
  const token = localStorage.getItem('token');
  if (token) {
    this.isLoggedIn = true;
    // Retrieve the stored email and update the username
    const storedEmail = localStorage.getItem('userEmail');
    if (storedEmail) {
      this.username = storedEmail;
    }
  }
},
};
</script>

<style scoped>
.header {
  display: flex;
  height: 70px;
  background-color: #0f131d;
  color: white;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  position: relative;
}

#loginButtonArea {
  display: flex;
  position: relative;
  align-items: center;
  cursor: pointer;
}

#headerLogo {
  width: 200px;
  height: auto;
}

#downIcon {
  height: 12px;
  width: auto;
  margin-left: 5px;
}

.expand-enter-active,
.expand-leave-active {
  transition: max-height 0.3s ease;
}

.expand-enter-from,
.expand-leave-to {
  max-height: 0;
}

.expand-enter-to,
.expand-leave-from {
  max-height: 50px;
}

.dropdown {
  display: grid;
  grid-template-columns: auto auto;
  position: absolute;
  top: calc(100% + 10px);
  right: -20px;
  left: auto;
  width: calc(
    150px
  ); /* Assuming that the parent container has 20px of padding on each side */
  background-color: #0f131dbb;
  color: white;
  text-align: center;
  z-index: 1000;
  overflow: hidden; /* Required to properly animate max-height */
  padding: 12px;
}

#logoutIcon {
  height: auto;
  width: 20px;
  transform: translate(10px, 6px);
}

.headerText {
  font-weight: bold;
  font-size: 15pt;
  cursor: pointer;
  user-select: none;
}

.dropdownText {
  transform: translate(5px, -2px);
  user-select: none;
}

#usernameTag {
  transform: translate(-5px, 5px);
}

.flipped {
  transform: scaleY(-1);
}
</style>
