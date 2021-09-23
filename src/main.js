// // import "./styles/styles.css";

import LoginForm from "./components/LoginForm.vue";
import HomePage from "./components/HomePage.vue";
import ContactPage from "./components/ContactPage.vue";
import "tailwindcss/tailwind.css";

import Vue from "vue";

var app = new Vue({
  el: "#app",
  data: {
    message: "Hello Vue!",
  },
  components: {
    loginform: LoginForm,
    homepage: HomePage,
    contactpage: ContactPage,
  },
  delimiters: ["[[", "]]"],
});
