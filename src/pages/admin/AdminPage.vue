<template>
  <div>
    <Navbar :isAdmin="isAdmin" />
    <AdminDashboard />
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import AdminDashboard from "../../components/AdminDashboard.vue";
import { ref } from "vue";
export default {
  name: "AdminPage",
  components: {
    Navbar,
    AdminDashboard,
  },
  setup() {
    const isAdmin = ref(true);
    return {
      isAdmin,
    };
  },
};
</script>
