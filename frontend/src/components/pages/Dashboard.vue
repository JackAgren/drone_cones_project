<template>
  <Background />

  <div class="sidenav">
    <p>Account</p>
    <p id="customer" @click="changeSelection">Customer</p>
    <p id="drones" @click="changeSelection">Drones</p>
    <p id="admin" @click="changeSelection">Admin Tools</p>
  </div>

  <CustomerDashboard v-if="currentSelection==='customer'"/>
  <DroneDashboard v-else-if="currentSelection==='drones'"/>
  <AdminDashboard v-else-if="currentSelection==='admin'"/>
</template>

<script>
import Background from '../Background.vue';
import AppHeader from '@/components/Header.vue';
import AppFooter from '@/components/Footer.vue';
import CustomerDashboard from "@/components/page-content/CustomerDashboard.vue";
import DroneDashboard from "@/components/page-content/DroneDashboard.vue";
import AdminDashboard from "@/components/page-content/AdminDashboard.vue";

export default {
  name: 'Dashboard',
  components: {
    DroneDashboard,
    CustomerDashboard,
    AdminDashboard,
    Background,
    AppHeader,
    AppFooter
  },
  data() {
    return {
      currentSelection: 'customer',
    }
  },
  methods: {
    changeSelection(event) {
      this.currentSelection = event.target.id;
    },
  },
  created() {
    if (this.$route.query.focus) {
      this.currentSelection = this.$route.query.focus;
    }
  },
}
</script>

<style scoped>
.sidenav {
  height: 100%;
  width: 175px;
  position: fixed;
  z-index: 1;
  top: 70px;
  left: 0;
  background-color: #111;
  opacity: 90%;
  overflow-x: hidden;
  padding-top: 20px;
}

.sidenav p {
  padding: 0 8px 6px 16px;
  text-decoration: none;
  font-size: 20px;
  color: #b7b7b7;
  display: block;
}

.sidenav p:hover {
  color: #f1f1f1;
}

@media screen and (max-height: 450px) {
  .sidenav {
    padding-top: 15px;
  }
  .sidenav p {
    font-size: 18px;
  }
}
</style>
