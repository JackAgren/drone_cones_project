<template>
  <footer class="footer">
    <p>Copyright &copy; 2023</p>
  </footer>
</template>

<script>
import '@/assets/style.css';

export default {
  name: 'AppFooter'
};
</script>

<style scoped>
  .footer {
    background-color: #0F141D;
    color: white;
    text-align: center;
    bottom: 0;
    width: 100%;
    padding: 0;
    margin:0;
    pointer-events: none;
    user-select: none;
  }
</style>