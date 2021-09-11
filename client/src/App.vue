<template>
  <HomePageHeader />
</template>

<script>
import HomePageHeader from "./components/HomePageHeader.vue";

export default {
  name: "App",
  components: {
    HomePageHeader,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
