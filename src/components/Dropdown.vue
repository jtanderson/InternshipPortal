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
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
          class="
            fill-current
            h-4
            w-4
            transform
            transition-transform
            duration-200
            ease-in-out
          "
          :class="isOptionsExpanded ? 'rotate-180' : 'rotate-0'"
        >
          <path
            d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
          />
        </svg>
      </button>
      <transition
        enter-active-class="transform transition duration-500 ease-custom"
        enter-class="-translate-y-1/2 scale-y-0 opacity-0"
        enter-to-class="translate-y-0 scale-y-100 opacity-100"
        leave-active-class="transform transition duration-300 ease-custom"
        leave-class="translate-y-0 scale-y-100 opacity-100"
        leave-to-class="-translate-y-1/2 scale-y-0 opacity-0"
      >
        <ul
          class="absolute text-gray-700 pt-1 group-hover:block"
          v-show="!hideDropdown"
        >
          <li class="">
            <div
              class="
                rounded-t
                bg-gray-200
                hover:bg-gray-400
                py-4
                px-6
                block
                whitespace-no-wrap
                cursor-pointer
                text-center
              "
              v-on:click="clearFilters"
            >
              All
            </div>
            <div
              class="
                bg-gray-200
                hover:bg-gray-400
                py-4
                px-6
                block
                whitespace-no-wrap
                cursor-pointer
                text-center
              "
              v-on:click="filterActive"
            >
              Active
            </div>
          </li>
          <li class="">
            <div
              class="
                bg-gray-200
                hover:bg-gray-400
                py-4
                px-6
                block
                whitespace-no-wrap
                cursor-pointer
                text-center
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
                py-4
                px-6
                block
                whitespace-no-wrap
                cursor-pointer
                text-center
              "
              v-on:click="filterPending"
            >
              Pending
            </div>
          </li>
        </ul>
      </transition>
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
      isOptionsExpanded: false,
    };
  },
  props: ["changeFilter"],
  methods: {
    dropDown() {
      this.hideDropdown = !this.hideDropdown;
      this.isOptionsExpanded = !this.isOptionsExpanded;
    },
    filterActive() {
      this.changeFilter("active");
      this.activeFilter = "Active";
      this.hideDropdown = true;
      this.isOptionsExpanded = false;
    },
    filterInactive() {
      this.changeFilter("inactive");
      this.activeFilter = "Inactive";
      this.hideDropdown = true;
      this.isOptionsExpanded = false;
    },
    filterPending() {
      this.changeFilter("pending");
      this.activeFilter = "Pending";
      this.hideDropdown = true;
      this.isOptionsExpanded = false;
    },
    clearFilters() {
      this.changeFilter("all");
      this.activeFilter = "All";
      this.hideDropdown = true;
      this.isOptionsExpanded = false;
    },
  },
};
</script>

<style>
.ease-custom {
  transition-timing-function: cubic-bezier(0.61, -0.53, 0.43, 1.43);
}
</style>
