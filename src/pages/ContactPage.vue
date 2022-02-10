<template>
  <div>
    <Navbar :isAdmin="isAdmin" active="Contact" />
    <ContactForm />
  </div>
</template>

<script>
import { ref } from "vue";
import ContactForm from "../components/ContactForm.vue";
import Navbar from "../components/Navbar.vue";
export default {
  name: "ContactPage",
  components: {
    ContactForm,
    Navbar,
  },
  setup() {
    const isAdmin = ref(false);
    return {
      isAdmin,
    };
  },
};
</script>
