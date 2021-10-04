<template>
  <div>
    <Navbar />
    <AdminDashboard />
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import AdminDashboard from "../components/AdminDashboard.vue";
export default {
  name: "AdminPage",
  components: {
    Navbar,
    AdminDashboard,
  },
};
</script>