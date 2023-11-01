<template>
  <div id="standardLayout">
    <AppHeader />
    <HomepageContent />
    <AppFooter />
  </div>
</template>

<script>
import '../../assets/style.css';
import AppHeader from '@/components/Header.vue';
import AppFooter from '@/components/Footer.vue';
import HomepageContent from '@/components/page-content/HomepageContent.vue';


export default {
  name: 'Homepage',
  components: {
    AppHeader,
    AppFooter,
    HomepageContent
  },
  data() {
    return {
      //add data for the page
    }
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
