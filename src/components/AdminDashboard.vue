<template>
  <div class="h-screen flex">
    <div class="align-middle m-auto font-bold">
      Admin Dashboard Content Goes Here
    </div>
  </div>
</template>

<script>
import AdminStats from "./AdminStats.vue";
import AdminCard from "./AdminCard.vue";
export default {
  name: "AdminDashboard",
  components: {
    AdminStats,
    AdminCard,
  },
};
</script>
