<template></template>

<script>
export default {
  name: "InsertPage",
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
