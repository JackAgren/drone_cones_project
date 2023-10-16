<template>
  <button class="vueBackButton">
    <img id="arrow" src="../assets/arrow.png" />
  </button>
</template>

<script>
import '@/assets/style.css';

export default {
  name: 'VueBackButton',
};
</script>

<style scoped>
.vueBackButton {
  justify-content: center;
  border-radius: 50%;
  height: 50px;
  width: 50px;
  font-family: sans-serif;
  font-size: 14pt;
  font-weight: bold;
  cursor: pointer;
  background-color: rgb(0, 0, 0);
  color: white;
  border: none;
  outline: none;
  transition: background-color 0.3s;
}

#arrow {
  height: 23px;
  width: auto;
}

.vueBackButton:hover {
  background-color: rgb(0, 162, 255);
}
</style>
