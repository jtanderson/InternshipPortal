<template>
  <Navbar :isAdmin="isAdmin" active="Browse" />
  <Searchbar />
</template>

<script>
import { ref } from "vue";
import Searchbar from "../components/Searchbar.vue";
import Navbar from "../components/Navbar.vue";
export default {
  name: "BrowsePage",
  components: {
    Searchbar,
    Navbar,
  },
  setup() {
    const isAdmin = ref(false);
    return {
      isAdmin,
    };
  },
};
</script>
