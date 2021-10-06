<template>
  <ListingForm />
</template>

<script>
import ListingForm from "../components/ListingForm.vue";
export default {
  name: "InsertListingPage",
  components: {
    ListingForm,
  },
  data: {
    email: "",
    reg: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/,
  },
  methods: {
    isEmailValid() {
      return this.email == ""
        ? ""
        : this.reg.test(this.email)
        ? "has-success"
        : "has-error";
    },
  },
};
</script>
