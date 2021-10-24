<template>
  <div class="p-20 mb-32">
    <div class="group inline-block relative">
      <button
        class="
          bg-gray-200
          hover:bg-gray-400
          text-gray-700
          font-semibold
          py-2
          px-4
          rounded
          inline-flex
          items-center
        "
        v-on:click="dropDown"
      >
        <span class="mr-1">{{ activeFilter }}</span>
        <svg
          class="fill-current h-4 w-4"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
        >
          <path
            d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
          />
        </svg>
      </button>
      <ul
        class="absolute text-gray-700 pt-1 group-hover:block"
        :class="hideDropdown ? 'hidden' : ''"
      >
        <li class="">
          <div
            class="
              rounded-t
              bg-gray-200
              hover:bg-gray-400
              py-2
              px-4
              block
              whitespace-no-wrap
              cursor-pointer
            "
            v-on:click="clearFilters"
          >
            All
          </div>
          <div
            class="
              rounded-t
              bg-gray-200
              hover:bg-gray-400
              py-2
              px-4
              block
              whitespace-no-wrap
              cursor-pointer
            "
            v-on:click="filterActive"
          >
            Active
          </div>
        </li>
        <li class="">
          <div
            class="
              rounded
              bg-gray-200
              hover:bg-gray-400
              py-2
              px-4
              block
              whitespace-no-wrap
              cursor-pointer
            "
            v-on:click="filterInactive"
          >
            Inactive
          </div>
        </li>
        <li class="">
          <div
            class="
              rounded-b
              bg-gray-200
              hover:bg-gray-400
              py-2
              px-4
              block
              whitespace-no-wrap
              cursor-pointer
            "
            v-on:click="filterPending"
          >
            Pending
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "Dropdown",
  data() {
    return {
      hideDropdown: true,
      activeFilter: "Filter",
    };
  },
  props: ["changeFilter"],
  methods: {
    dropDown() {
      this.hideDropdown = !this.hideDropdown;
    },
    filterActive() {
      this.changeFilter("active");
      this.activeFilter = "Active";
      this.hideDropdown = true;
    },
    filterInactive() {
      this.changeFilter("inactive");
      this.activeFilter = "Inactive";
      this.hideDropdown = true;
    },
    filterPending() {
      this.changeFilter("pending");
      this.activeFilter = "Pending";
      this.hideDropdown = true;
    },
    clearFilters() {
      this.changeFilter("all");
      this.activeFilter = "All";
      this.hideDropdown = true;
    },
  },
};
</script>
