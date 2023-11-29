<template>

  <div class="center">

    <div>
      <div class="button-box" @click="toFinancialRecords">
        <img class="image-box" alt="Dollar sign." src="../../assets/img/dollar.png">
        <p class="caption">Financial Records</p>
      </div>

      <!-- <div class="button-box" @click="toManageLeases">
        <img class="image-box" alt="Money being passed." src="../../assets/img/money-hand.png">
        <p class="caption">Manage Lease Payments</p>
      </div> -->

      <div class="button-box" @click="toManageInventory">
        <img class="image-box" alt="Boxes and a clip board." src="../../assets/img/inventory.png">
        <p class="caption">Restock</p>
      </div>
    </div>

    <div>
      <div class="button-box" @click="toManageAccounts">
        <img class="image-box" alt="Icon of users." src="../../assets/img/users.png">
        <p class="caption">Manage Accounts</p>
      </div>

      <div class="button-box" @click="toManageMenu">
        <img class="image-box" alt="Icon of ice cream menu." src="../../assets/img/menu.png">
        <p class="caption">Manage Menu</p>
      </div>
    </div>

  </div>

</template>

<script>
export default {
  name: 'AdminDashboard',
  methods: {
    toFinancialRecords() {
      this.$router.push({path: '/admin/financialRecords', query: {}});
    },
    toManageLeases() {
      this.$router.push({path: '/admin/manageLeasePayments', query: {}});
    },
    toManageInventory() {
      this.$router.push({path: '/admin/manageInventory', query: {}});
    },
    toManageAccounts() {
      this.$router.push({path: '/admin/manageAccounts', query: {}});
    },
    toManageMenu() {
      this.$router.push({path: '/admin/manageMenu', query: {}});
    },
  },
}
</script>

<style scoped>

.center {
  margin: auto;
  width: 60%;
  height: 30%;
  position: fixed;
  z-index: 1;
  top: 20%;
  left: 325px;
  color: white;
  font-weight: bold;
  text-align: center;
}

.image-box {
  opacity: 100%;
  width: 50%;
}

.caption {
  margin-top: 10px;
  font-size: 13pt;
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
}

.button-box:hover {
  background-color: rgba(17, 17, 17, .95);
}

</style>
