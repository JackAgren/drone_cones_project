<template>
  <header class="homepageContent">
    <div id="homepageContentSection1">
      <div id="cloudsArea">
        <img id="clouds1" src="@/assets/clouds1.png" />
        <img id="clouds2" src="@/assets/clouds2.png" />
        <img id="clouds3" src="@/assets/clouds3.png" />
        <img id="clouds4" src="@/assets/clouds1.png" />
      </div>

      <div id="section1TextBlurbArea">
        <p>Get a cold creamy cone by drone!</p>
      </div>

      <div id="section1LogoArea">
        <img id="section1Logo" src="@/assets/logo.png" />
      </div>

      <div id="section1ButtonArea">
        <router-link :to="{ path: '/login' }">
        <VueButton id="section1LoginButton"> Login </VueButton>
        </router-link>
        <router-link :to="{ path: '/register' }">
        <VueButton id="section1LoginButton"> Register </VueButton>
      </router-link>
      </div>

      <div id="droneIconArea">
        <img id="droneIcon" src="@/assets/drone.png" />
      </div>
    </div>

    <div id="homepageContentSection2">
      <div class="section2Subsection">
        <img class="subsectionIcon" src="../../assets/money.png" />
        <p>
          Get paid while we let your drone <br />
          do all the work!
        </p>
        <a href="">Lease a drone →></a>
      </div>

      <div class="section2Subsection">
        <img class="subsectionIcon" src="../../assets/admin.png" />
        <p>Get great employment opportunities with the Drone Cone crew!</p>
        <a href="">Apply for admin →</a>
      </div>

      <div class="section2Subsection">
        <img class="subsectionIcon" src="../../assets/check.png" id="checkmark" />
        <p>
          Register for a free customer account to make orders faster and receive
          perks!
        </p>
        <a href="">Register →</a>
      </div>
    </div>
  </header>
</template>

<script>
import '@/assets/style.css';
import VueButton from '../Button.vue'

export default {
  name: 'HomepageContent',
  components:{
    VueButton
  },
  methods: {
  gotoLogin() {
      this.$router.push({path: '/login', query: {}})
    },
  gotoRegister() {
    this.$router.push({path: '/register', query: {}})
  },
  },
};
</script>

<style scoped>
.homepageContent {
  display: grid;
  grid-template-rows: 500px 1.5fr;
}

#homepageContentSection1 {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr auto;
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
}

#clouds2 {
  animation: cloudAnimation2 60s linear infinite;
  animation-delay: -25s;
}

#clouds3 {
  position: absolute;
  top: 240px;
  animation: cloudAnimation3 80s linear infinite;
  animation-delay: -25s;
}

#clouds4 {
  animation: cloudAnimation3 60s linear infinite;
  animation-delay: -40s;
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

#section1TextBlurbArea {
  left: 50%;
  top: 170px;
  transform: translate(-50%, -50%);
  position: absolute;
  grid-column: 2/3;
  font-family: sans-serif;
  font-weight: bold;
  color: white;
  font-size: 20pt;
  justify-content: center;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

#section1LogoArea {
  position: absolute;
  display: flex;
  grid-column: 2/3;
  width: auto;
  left: 50%;
  top: 70px;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

#droneIconArea {
  position: absolute;
  display: flex;
  grid-column: 2/3;
  width: auto;
  left: 50%;
  top: 400px;
  transform: translate(-50%, -50%);
  pointer-events: none;
}

#section1Logo {
  width: 650px;
  height: auto;
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

#section1ButtonArea {
  position: absolute;
  display: flex;
  justify-content: space-between;
  align-items: center;
  grid-column: 2/3;
  width: 400px;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

#homepageContentSection2 {
  background-color: #0f141d;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  padding-left: 220px;
  padding-right: 220px;
  color: white;
  font-size: 14pt;
  font-weight: bold;
}

.section2Subsection {
  margin-top: 80px;
  margin-bottom: 80px;
  display: flex;
  flex-direction: column;
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  padding-left: 70px;
  padding-right: 70px;
  text-align: center;
}

.subsectionIcon {
  height: 130px;
  width: auto;
  margin-bottom: 50px;
}

#checkmark {
  padding: 10px;
}
</style>
