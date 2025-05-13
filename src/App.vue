<template>
  <!-- <LifecycleHooks1 /> -->
  <LifecycleHooks2 />
  <LifecycleHooks3 />
  <!-- <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <!-- <div class="container mx-auto px-4 py-8">
    <router-view />
  </div> -->
</template>

<script> // setup
// import HelloWorld from './components/HelloWorld.vue'
import { onMounted } from 'vue';
onMounted(() => {
  console.log('应用已加载');
});
export default {
  name: 'App',
  components: {
    // HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  /* margin-top: 60px; */
}
body {
  font-family: 'Inter', sans-serif;
}
</style>
