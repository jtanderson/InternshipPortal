<template>
  <Navbar :isAdmin="false" active="Browse" />
  <Searchbar />
</template>

<script>
import Searchbar from "../components/Searchbar.vue";
import Navbar from "../components/Navbar.vue";
export default {
  name: "BrowsePage",
  components: {
    Searchbar,
    Navbar,
  },
  setup() {},
};
</script>
