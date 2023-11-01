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


    <p>Approximate arrival: {{ Math.round(minToArrival * 100) / 100 }} minute(s)</p>

    </div>


</template>

<script>
import Background from "@/components/Background.vue";

const TOTAL_TIME = .5; //in minutes
const UPDATE_RATE = .1; //in minutes

export default {
  name: 'Track Order',
  components: {
    Background,
  },
  data() {
    return {
      timePassed: 0,
    }
  },
  created() {
    let numOfSections = TOTAL_TIME / UPDATE_RATE;
    let sectionLength = (TOTAL_TIME / numOfSections /*in minutes*/) * 60 * 1000; //into milliseconds
    this.doTheWait(numOfSections, sectionLength)
        .then((resp) => {
          console.log(resp);
          this.$router.push({path: '/customer/arrived', query: {}});
        });
  },
  methods: {
    doTheWait(numOfSections, sectionLength) {
      return this.sleep(sectionLength)
          .then(async() => {
            this.timePassed += (sectionLength / 1000 / 60);
            if (numOfSections > 0) {
              return await this.doTheWait(numOfSections - 1, sectionLength);
            }
            return "We did it!";
          });
    },
    sleep(ms) {
      return new Promise(resolve => setTimeout(resolve, ms));
    },
  },
  computed: {
    barProgress() {
      const percent = Math.round(((TOTAL_TIME - this.minToArrival) / TOTAL_TIME) * 100);
      return `width: ${percent}%`;
    },
    minToArrival() {
      return TOTAL_TIME - this.timePassed;
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
