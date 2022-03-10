<template>
  <div>
    <Navbar :isAdmin="isAdmin" />
    <MessageView/>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import MessageView from "../../components/MessageView.vue";
import { ref } from "vue";
export default {
  name: "AdminViewMessage",
  components: {
    Navbar,
    MessageView,
  },
  setup() {
      const isAdmin = ref(true);
    return {
      isAdmin,
    };
  },
};
</script>