<template>
  <div>
    <Navbar :isAdmin="isAdmin" />
    <InboxSearchBar/>
    <ContactInboxModule/>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import ContactInboxModule from "../../components/ContactInbox.vue";
import InboxSearchBar from "../../components/InboxSearchBar.vue";
import { ref } from "vue";
export default {
  name: "AdminContactInboxView",
  components: {
    Navbar,
    InboxSearchBar, 
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