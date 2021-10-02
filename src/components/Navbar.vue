<template>
  <nav class="flex items-center justify-between flex-wrap p-4 bg-primary">
    <div class="w-full block flex-grow lg:flex lg:items-center lg:w-auto">
      <div class="lg:flex-grow">
        <h2 class="mt-2 mb-2 text-white text-center text-2xl font-bold">
          Admin Dashboard
        </h2>
      </div>
      <div>
        <button
          class="
            inline-block
            text-sm
            px-4
            py-2
            leading-none
            border
            rounded
            text-white
            border-white
            hover:border-transparent
            hover:text-primary
            hover:bg-white
            mt-4
            lg:mt-0
          "
          v-on:click="logout"
        >
          Logout
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
  methods: {
    logout() {
      // Logout admin, end session
      console.log("Logout requested");
    },
  },
};
</script>
