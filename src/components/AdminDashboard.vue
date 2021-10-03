<template>
  <div class="h-screen flex">
    <AdminStats />
    <AdminCard />
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
