<template>
  <div>
    <Navbar :isAdmin="isAdmin" />
    <PendingListingModule/>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import PendingListingModule from "../../components/PendingListingModule.vue";
import { ref } from "vue";
export default {
  name: "AdminNotificationPage",
  components: {
    Navbar,
    PendingListingModule,
  },
  setup() {
    const isAdmin = ref(true);
    return {
      isAdmin,
    };
  },
};
</script>