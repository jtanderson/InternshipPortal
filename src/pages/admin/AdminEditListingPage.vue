<template>
  <div>
    <Navbar :isAdmin="isAdmin" />
    <EditListing />
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import EditListing from "../../components/EditListing.vue";
import { ref } from "vue";
export default {
  name: "AdminEditListingPage",
  components: {
    Navbar,
    EditListing,
  },
  setup() {
    const isAdmin = ref(true);
    return {
      isAdmin,
    };
  },
};
</script>
