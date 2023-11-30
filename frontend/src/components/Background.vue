<template>
  <div id="standardLayout">
    <AppHeader />
    <header class="tablePageContent">
      <div id="pageContent">
        <div id="cloudsArea">
          <img id="clouds1" src="@/assets/clouds1.png" />
          <img id="clouds2" src="@/assets/clouds2.png" />
          <img id="clouds3" src="@/assets/clouds3.png" />
          <img id="clouds4" src="@/assets/clouds1.png" />
        </div>

        <!-- INPUT OPTIONAL HTML HERE -->
        <slot></slot>
      </div>
    </header>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from '@/components/Header.vue';
import AppFooter from '@/components/Footer.vue';

export default {
  name: 'Background',
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {

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

.tablePageContent {
  display: grid;
  grid-template-rows: 1fr;
}

#pageContent {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr auto;
  width: 100%;
  background-image: url("@/assets/sky.png");
  background-size: 100% 100%;
  background-repeat: repeat-x;
  overflow: hidden;
}

#cloudsArea {
  position: absolute;
  display: flex;
  height: auto;
  grid-column: 1/4;
}

#clouds1 {
  position: absolute;
  top: 150px;
  animation: cloudAnimation1 60s linear infinite;
  animation-delay: -10s;
  padding-left: 40px;
  user-select: none;
  pointer-events: none;
}

#clouds2 {
  animation: cloudAnimation2 60s linear infinite;
  animation-delay: -25s;
  user-select: none;
  pointer-events: none;
}

#clouds3 {
  position: absolute;
  top: 240px;
  animation: cloudAnimation3 80s linear infinite;
  animation-delay: -25s;
  user-select: none;
  pointer-events: none;
}

#clouds4 {
  animation: cloudAnimation3 60s linear infinite;
  animation-delay: -40s;
  user-select: none;
  pointer-events: none;
}

@keyframes cloudAnimation1 {
  from {
    transform: translateX(-100%); /* Start off-screen to the left */
  }
  to {
    transform: translateX(300%); /* Move off-screen to the right */
  }
}

@keyframes cloudAnimation2 {
  from {
    transform: translateX(-100%); /* Start off-screen to the left */
  }
  to {
    transform: translateX(500%); /* Move off-screen to the right */
  }
}

@keyframes cloudAnimation3 {
  from {
    transform: translateX(-500%); /* Start off-screen to the left */
  }
  to {
    transform: translateX(300%); /* Move off-screen to the right */
  }
}

@keyframes cloudAnimation4 {
  from {
    transform: translateX(-500%); /* Start off-screen to the left */
  }
  to {
    transform: translateX(500%); /* Move off-screen to the right */
  }
}

.button-disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
