<template>
  <div>
    <Navbar :isAdmin="isAdmin" />
    <ContactInboxModule/>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import ContactInboxModule from "../../components/ContactInbox.vue";
import { ref } from "vue";
export default {
  name: "AdminContactInboxView",
  components: {
    Navbar,
    ContactInboxModule,
  },
  setup() {
    const isAdmin = ref(true);
    return {
      isAdmin,
    };
  },
};
</script>