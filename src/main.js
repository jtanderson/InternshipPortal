import ContactPage from "./pages/ContactPage.vue";
import AdminPage from "./pages/admin/AdminPage.vue";
import HomePage from "./pages/HomePage.vue";
import LoginPage from "./pages/LoginPage.vue";
import InsertListingPage from "./pages/InsertListingPage.vue";
import AdminListingsPage from "./pages/admin/AdminListingsPage.vue";

import "tailwindcss/tailwind.css";

import Vue from "vue";

var app = new Vue({
  el: "#app",
  components: {
    homepage: HomePage,
    adminpage: AdminPage,
    adminlistings: AdminListingsPage,
    contactpage: ContactPage,
    loginpage: LoginPage,
    insertpage: InsertListingPage,
  },
  delimiters: ["[[", "]]"],
});
