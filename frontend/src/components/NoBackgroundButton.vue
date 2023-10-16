<template>
    <button class="vueButton" @click="onClick">
      <slot></slot>
    </button>
</template>

<script>
import '@/assets/style.css';

export default {
  name: 'VueButton',

  methods: {
    onClick() {
      this.$emit('click');
    }
  }
};
</script>

<style scoped>
  .vueButton {
    justify-content: center;
    border-radius: 50px;
    padding: 10px 20px;
    font-family: sans-serif;
    font-size: 14pt;
    font-weight: bold;
    cursor: pointer;
    color: rgb(212, 212, 212);
    border: none;
    outline: none;
    background: none;
    transition: color 0.3s;
  }

  .vueButton:hover {
    color:  rgb(255, 255, 255);;
  }
</style>