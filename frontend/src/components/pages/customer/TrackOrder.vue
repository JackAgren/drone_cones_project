<template>

  <Background/>

  <div class="center">

    <div id="section1TextBlurbArea">
      <h2>Your Order Is on the Way!</h2>
    </div>

    <div id="droneIconArea">
      <img id="droneIcon" src="@/assets/drone.png" />
    </div>

    <div class="progress" role="progressbar" aria-label="Basic example" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">
      <div class="progress-bar" :style='barProgress'></div>
    </div>


    <p>Approximate arrival: {{ minToArrival }} minutes</p>

    </div>


</template>

<script>
import Background from "@/components/Background.vue";

export default {
  name: 'Track Order',
  components: {
    Background,
  },
  data() {
    return {
      minToArrival: 2,
      totalTime: 10,
    }
  },
  computed: {
    barProgress() {
      const percent = Math.round(((this.totalTime - this.minToArrival) / this.totalTime) * 100);
      return `width: ${percent}%`;
    },
  },
}
</script>

<style scoped>

.progress {
  height: 20px;
  margin-top: 30%;
  box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  border-radius: 10px;
}

.progress-bar {
  background-color: #77CF1A;
  border-radius: 10px;
}

.center {
  margin: auto;
  width: 70%;
  height: 60%;
  position: fixed;
  z-index: 1;
  top: 20%;
  left: 15%;
  color: white;
  text-align: center;
}

h2 {
  padding-top: 10px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

p {
  font-size: 20pt;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
  margin-top: 5%;
}

#droneIconArea {
  position: absolute;
  display: flex;
  grid-column: 2/3;
  width: auto;
  left: 50%;
  top: 45%;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

#droneIcon {
  width: 450px;
  height: auto;
  animation: droneHover 2s 2s ease-in-out infinite alternate;
}

@keyframes droneHover {
  from {
    transform: translateY(0px); /* Start off-screen to the left */
  }
  to {
    transform: translateY(-20px); /* Move off-screen to the right */
  }
}


</style>
