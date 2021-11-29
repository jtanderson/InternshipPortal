<template>
  <header class="text-gray-600 body-font shadow-xl">
    <div
      class="
        container
        mx-auto
        flex flex-wrap
        p-5
        flex-col
        md:flex-row
        items-center
      "
    >
      <div class="ml-0 mr-2">
        <!-- TODO: Need to fix this to use config path eventually -->
        <img src="../img/seagull.svg" height="30" width="30" />
      </div>
      <a
        class="
          flex
          title-font
          font-medium
          items-center
          text-gray-900
          mb-4
          md:mb-0
        "
        href="/admin"
      >
        <span class="ml-3 text-xl">SU Internship Web Portal</span>
      </a>
      <nav
        class="
          md:mr-auto md:ml-4 md:py-1 md:pl-4 md:border-l md:border-gray-400
          flex flex-wrap
          items-center
          text-base
          justify-center
        "
      >
        <a
          class="mr-5 py-1 px-3"
          href="/admin/listings"
          :class="
            active == 'Listings'
              ? 'bg-gray-100 rounded hover:bg-gray-200 focus:outline-none border-0 text-base'
              : 'hover:text-gray-900'
          "
          >Listings</a
        >
        <!-- <a
          class="mr-5"
          :class="
            active == 'Internships'
              ? 'bg-gray-100 rounded hover:bg-gray-200 focus:outline-none px-3 py-1 border-0 text-base'
              : 'hover:text-gray-900'
          "
          >Internships</a
        >
        <a
          class="mr-5"
          :class="
            active == 'Student'
              ? 'bg-gray-100 rounded hover:bg-gray-200 focus:outline-none px-3 py-1 border-0 text-base'
              : 'hover:text-gray-900'
          "
          >Student</a
        >
        <a
          class="mr-5"
          :class="
            active == 'Clients'
              ? 'bg-gray-100 rounded hover:bg-gray-200 focus:outline-none px-3 py-1 border-0 text-base'
              : 'hover:text-gray-900'
          "
          >Clients</a
        > -->
      </nav>
      <div>
        <svg
          class="w-6 h-6 mr-4 cursor-pointer"
          @click="toNotificationsPage"
          fill="#F3F4F6"
          stroke="#000000"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"
          ></path>
        </svg>
      </div>
      <button
        class="
          inline-flex
          items-center
          bg-gray-100
          border-0
          py-1
          px-3
          focus:outline-none
          hover:bg-gray-200
          rounded
          text-base
          mt-4
          md:mt-0
        "
        @click="logout"
      >
        Logout
        <svg
          fill="none"
          stroke="currentColor"
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          class="w-4 h-4 ml-1"
          viewBox="0 0 24 24"
        >
          <path d="M5 12h14M12 5l7 7-7 7"></path>
        </svg>
      </button>
    </div>
  </header>
</template>

<script>
import { ref } from "vue";
export default {
  name: "Navbar",
  props: ["active"],
  setup(props) {
    const active = ref(props.active);
    async function logout() {
      fetch(`${process.env.SERVER_URL}/logout`).then((res) => {
        if (res.status === 200) {
          console.log("Logout successful");
          window.location.href = "/";
        }
      });
    }
    function toNotificationsPage() {
      // TODO: Change this to notifications page once we build it
      window.location.href = "/";
    }
    return {
      active,
      toNotificationsPage,
      logout,
    };
  },
};
</script>
