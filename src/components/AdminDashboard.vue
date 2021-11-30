<template>
  <div class="bg-gray-100">
    <PendingListingModule />
  </div>
</template>

<script>
import PendingListingModule from "./PendingListingModule.vue";
export default {
  name: "AdminDashboard",
  components: {
    PendingListingModule,
  },
};
</script>
