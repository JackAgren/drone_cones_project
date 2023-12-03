<template>

  <div class="center">

    <div class="button-box" @click="toRegistration">
      <img class="image-box" alt="Icon of a drone with a plus button." src="../../assets/img/Group%2038.png">
      <p class="caption">Drone Registration</p>
    </div>

    <!-- <div class="button-box" @click="toActivity">
      <img class="image-box" alt="Icon of binoculars." src="../../assets/img/binoculars.png">
      <p class="caption">Drone Activity</p>
    </div> -->

    <div class="button-box" @click="toEarnings">
      <img class="image-box" alt="Icon of a stack of cash." src="../../assets/img/money.png">
      <p class="caption">Earnings</p>
    </div>

  </div>

</template>

<script>


export default {
  name: 'DroneDashboard',
  methods: {
    toRegistration() {
      this.$router.push({path: '/drone/registration', query: {}})
    },
    toActivity() {
      this.$router.push({path: '/drone/activity', query: {}})
    },
    toEarnings() {
      this.$router.push({path: '/drone/earnings', query: {}})
    },
  },
}
</script>

<style scoped>

.center {
  margin: auto;
  width: 70%;
  height: 30%;
  position: fixed;
  z-index: 1;
  top: 40%;
  left: 25%;
  color: white;
  font-weight: bold;
  text-align: center;
}

.image-box {
  opacity: 100%;
  width: 50%;
  user-select: none;
}

.caption {
  margin-top: 10px;
  font-size: 18pt;
  user-select: none;
}

.button-box {
  background-color: rgba(17, 17, 17, .85);
  border-radius: 10px;
  width: 30%;
  height: 90%;
  display: inline-block;
  font-size: 18pt;
  padding: 20px;
  margin: 10px 10px 10px 10px;
  cursor: pointer;
  user-select: none;
}

.button-box:hover {
  background-color: rgba(17, 17, 17, .95);
}

</style>
