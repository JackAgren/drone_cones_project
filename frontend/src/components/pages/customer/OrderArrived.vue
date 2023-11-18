<template>

  <Background/>

  <VueButton @click="moveToDashboard" class="dashboard-button">&#x25C0; &nbsp; Dashboard</VueButton>

  <div class="center">

    <div id="section1TextBlurbArea">
      <h2>Your Order Has Been Delivered!</h2>
    </div>

    <div id="droneIconArea">
      <img alt="Drone carrying a box of ice cream." id="droneIcon" src="@/assets/drone.png" />
    </div>

    <img class="person" alt="Person waving, holding an ice cream cone." src="../../../assets/img/Group%2037.png">


    <p>Thanks for choosing Drone Cones!</p>

  </div>


</template>

<script>
import Background from "@/components/Background.vue";
import VueButton from "@/components/Button.vue";
const SERVER_URL = "http://localhost:8000/";

export default {
  name: 'Order Arrived',
  components: {
    Background,
    VueButton
  },
  data() {
    return {
    }
  },
  created() {
    const orderID = this.$route.query.id;
    //TODO: mark order as delivered

    const body = {
      order: orderID
    }

    const token = localStorage.getItem('token');

    fetch(SERVER_URL + `orders/delivered`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`
      },
      body: JSON.stringify(body)
    })
        .then(res => {
          return res.json();
        })
        .then(resp => {
          console.log(resp);
        })
        .catch(err => {
          console.log(`An error occurred: ${err}`);
        });

  },
  methods: {
    moveToDashboard() {
      this.$router.push({path: '/dashboard', query: {}})
    },
  },
}
</script>

<style scoped>

.dashboard-button {
  position: fixed;
  top: 12%;
  left: 2%;
}

.person {
  height: 45%;
  margin-top: 8%;
  position: fixed;
  z-index: 1;
  top: 25%;
  left: 25%;
}

.center {
  margin: auto;
  width: 70%;
  height: 60%;
  position: fixed;
  z-index: 1;
  top: 20%;
  left: 15%;
  color: white;
  text-align: center;
}

h2 {
  padding-top: 10px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

p {
  font-size: 20pt;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  margin-top: 50%;
}

#droneIconArea {
  position: absolute;
  display: flex;
  grid-column: 2/3;
  width: auto;
  left: 75%;
  top: 30%;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

#droneIcon {
  width: 250px;
  height: auto;
  animation: droneHover 2s 2s ease-in-out infinite alternate;
}

@keyframes droneHover {
  from {
    transform: translateY(0px); /* Start off-screen to the left */
  }
  to {
    transform: translateY(-20px); /* Move off-screen to the right */
  }
}


</style>
