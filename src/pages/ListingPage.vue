<template>
  <div>
    <Navbar :isAdmin="false" />
    <IndividualPage />
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import IndividualPage from "../components/IndividualPage.vue";
export default {
  name: "listingpage",
  components: {
    Navbar,
    IndividualPage,
  },
};
</script>
