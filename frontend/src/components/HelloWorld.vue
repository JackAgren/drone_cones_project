<template>
  <img alt="Vue logo" class="logo" src="../assets/logo.svg" width="125" height="125" />
  <div class="greetings">
    <h1 class="green">Hello here is some Vue!</h1>
    <h3>{{ message }}</h3>
    <button
        class="btn btn-secondary"
        @click="moveToNewPage">
      Move to another page!</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorldComponent',
  data() {
    return {
      message: 'Here is a message',
    }
  },
  methods: {
    moveToNewPage() {
      console.log("Goodbye!");
      this.$router.push({path: '/second-page', query: {parameter: "cool!"}})
    },
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

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}
</style>
