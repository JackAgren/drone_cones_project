<template>
    <button class="wideButton" @click="onClick">
      <slot></slot>
    </button>
</template>

<script>
import '@/assets/style.css';

export default {
  name: 'wideButton',

  methods: {
    onClick() {
      this.$emit('click');
    }
  }
};
</script>

<style scoped>
  .wideButton {
    width: 240px;
    justify-content: center;
    border-radius: 50px;
    padding: 10px 20px;
    font-family: sans-serif;
    font-size: 14pt;
    font-weight: bold;
    cursor: pointer;
    background-color: rgb(115, 221, 67);
    color: white;
    border: none;
    outline: none;
    transition: background-color 0.3s;
  }

  .wideButton:hover {
    background-color:  rgb(64, 126, 36);;
  }
</style>