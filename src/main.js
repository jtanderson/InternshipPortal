import ContactPage from "./pages/ContactPage.vue";
import AdminPage from "./pages/AdminPage.vue";
import HomePage from "./pages/HomePage.vue";
import LoginPage from "./pages/LoginPage.vue";
import InsertPage from "./pages/InsertPage.vue";

import "tailwindcss/tailwind.css";

import Vue from "vue";

var app = new Vue({
  el: "#app",
  components: {
    homepage: HomePage,
    adminpage: AdminPage,
    contactpage: ContactPage,
    loginpage: LoginPage,
    insertpage: InsertPage,
  },
  delimiters: ["[[", "]]"],
});
