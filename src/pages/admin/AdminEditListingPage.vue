<template>
  <div>
    <Navbar />
    <EditListing />
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import EditListing from "../../components/EditListing.vue";
export default {
  name: "AdminEditListingPage",
  components: {
    Navbar,
    EditListing,
  },
};
</script>
