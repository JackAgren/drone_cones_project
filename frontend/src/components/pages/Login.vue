<template>
    <div id ="standardLayout">
        <LoginContent/>  
    </div>
</template>

<script>
import '../../assets/style.css';
import AppHeader from '@/components/Header.vue';
import AppFooter from '@/components/Footer.vue';
import LoginContent from '@/components/page-content/LoginContent.vue';

export default {
  name: 'Login',
  components: {
    AppHeader,
    AppFooter,
    LoginContent
  },
  data() {
    return {
      //add data for the page
    }
  },
  methods: {
  gotoDashboard() {
      this.$router.push({path: '/dashboard', query: {}})
    },
  },
}
</script>

<style scoped>
#standardLayout {
    display: grid;
    grid-template-rows: auto 1fr auto;
    height: 100vh;
}
</style>
