<template>
  <Navbar :isAdmin="isAdmin" active="Browse" />
  <Searchbar />
  <ListingTable />
</template>

<script>
import { ref } from "vue";
import ListingTable from "../components/ListingTable.vue";
import Searchbar from "../components/Searchbar.vue";
import Navbar from "../components/Navbar.vue";
export default {
  name: "BrowsePage",
  components: {
    ListingTable,
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
