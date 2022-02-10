import ContactPage from "./pages/ContactPage.vue";
import AdminPage from "./pages/admin/AdminPage.vue";
import HomePage from "./pages/HomePage.vue";
import LoginPage from "./pages/LoginPage.vue";
import InsertListingPage from "./pages/InsertListingPage.vue";
import AdminListingsPage from "./pages/admin/AdminListingsPage.vue";
import AdminEditListingPage from "./pages/admin/AdminEditListingPage.vue";
import ResetPasswordAuthPage from "./pages/ResetPasswordAuthPage.vue";
import ResetPasswordPage from "./pages/ResetPasswordPage.vue";
import BrowsePage from "./pages/BrowsePage.vue";

import "tailwindcss/tailwind.css";
import { createApp } from "vue";

const app = createApp({});
app.component("homepage", HomePage);
app.component("adminpage", AdminPage);
app.component("loginpage", LoginPage);
app.component("contactpage", ContactPage);
app.component("insertpage", InsertListingPage);
app.component("adminlistings", AdminListingsPage);
app.component("admineditlistingpage", AdminEditListingPage);
app.component("resetpasswordauthpage", ResetPasswordAuthPage);
app.component("resetpasswordpage", ResetPasswordPage);
app.component("browsepage", BrowsePage);

app.config.compilerOptions.delimiters = ["[[", "]]"];

app.mount("#app");
