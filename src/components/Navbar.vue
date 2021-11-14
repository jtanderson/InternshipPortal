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
        <span class="ml-3 text-xl">Admin Dashboard</span>
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
    return {
      active,
      logout,
    };
  },
};
</script>
