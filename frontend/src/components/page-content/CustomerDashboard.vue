<template>

  <div class="center">
    <div class="order-box" @click="toOrder">
      <img class="image-box" alt="Icon of ice cream menu." src="../../assets/img/menu.png">
      <p class="caption">Place an Order</p>
    </div>
    <div class="history-box" @click="toHistory">
      <p>View Order History</p>
    </div>
  </div>

</template>

<script>


export default {
  name: 'CustomerDashboard',
  methods: {
    toOrder() {
      this.$router.push({path: '/customer/menu', query: {}})
    },
    toHistory() {
      this.$router.push({path: '/customer/history', query: {}})
    },
  },
}
</script>

<style scoped>

.center {
  margin: auto;
  width: 60%;
  height: 60%;
  position: fixed;
  z-index: 1;
  top: 20%;
  left: 30%;
  color: white;
  font-weight: bold;
  text-align: center;
}

.image-box {
  opacity: 100%;
  height: 90%;
  user-select: none;
}

.caption {
  margin-top: 10px;
  user-select: none;
}

.order-box {
  background-color: rgba(119, 207, 26, .85);
  border-radius: 10px;
  height: 80%;
  font-size: 25pt;
  padding: 50px 0;
  cursor: pointer;
}

.order-box:hover {
  background-color: rgba(119, 207, 26, .95);
}

.history-box {
  background-color: rgba(17, 17, 17, .85);
  border-radius: 10px;
  height: 20%;
  font-size: 18pt;
  padding: 20px 0;
  cursor: pointer;
  user-select: none;
}

.history-box:hover {
  background-color: rgba(17, 17, 17, .95);
}

</style>
