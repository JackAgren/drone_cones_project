<template>
  <div class="greetings">
    <h1 class="green">This is a different page now</h1>
  </div>
</template>

<script>
export default {
  name: 'SecondSampleComponent',
  data() {
    return {
      //add data for the page
    }
  },
}
</script>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}
</style>
