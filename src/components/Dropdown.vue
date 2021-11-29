<template>
  <div class="p-10 pb-20 mb-20">
    <div class="relative inline-block text-left">
      <div>
        <button
          type="button"
          class="
            inline-flex
            justify-center
            w-full
            rounded-md
            border border-gray-300
            shadow-sm
            px-4
            py-2
            bg-white
            text-sm
            font-medium
            text-gray-700
            hover:bg-gray-50
            focus:outline-none
          "
          id="menu-button"
          aria-expanded="true"
          aria-haspopup="true"
          @click="dropDown"
        >
          {{ activeFilter }}
          <svg
            class="-mr-1 ml-2 h-5 w-5"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            />
          </svg>
        </button>
      </div>
      <div
        class="
          origin-top-right
          absolute
          left-0
          mt-2
          w-56
          rounded-md
          shadow-lg
          bg-white
          ring-1 ring-black ring-opacity-5
          focus:outline-none
        "
        v-show="!hideDropdown"
        role="menu"
        aria-orientation="vertical"
        aria-labelledby="menu-button"
        tabindex="-1"
      >
        <div class="py-1" role="none">
          <a
            href="#"
            class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-100"
            role="menuitem"
            tabindex="-1"
            id="menu-item-0"
            @click="clearFilters"
            >All</a
          >
          <a
            href="#"
            class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-100"
            role="menuitem"
            tabindex="-1"
            id="menu-item-1"
            @click="filterActive"
            >Active</a
          >
          <a
            href="#"
            class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-100"
            role="menuitem"
            tabindex="-1"
            id="menu-item-2"
            @click="filterInactive"
            >Inactive</a
          >
          <a
            href="#"
            class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-100"
            role="menuitem"
            tabindex="-1"
            id="menu-item-3"
            @click="filterPending"
            >Pending</a
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, toRefs } from "vue";
export default {
  name: "Dropdown",
  props: {
    changeFilter: Function,
  },
  setup(props) {
    const { changeFilter } = toRefs(props);
    const hideDropdown = ref(true);
    const activeFilter = ref("Filter");
    const isOptionsExpanded = ref(false);
    function dropDown() {
      hideDropdown.value = !hideDropdown.value;
      isOptionsExpanded.value = !isOptionsExpanded.value;
    }
    function filterActive() {
      changeFilter.value("active");
      activeFilter.value = "Active";
      hideDropdown.value = true;
      isOptionsExpanded.value = false;
    }
    function filterInactive() {
      changeFilter.value("inactive");
      activeFilter.value = "Inactive";
      hideDropdown.value = true;
      isOptionsExpanded.value = true;
    }
    function filterPending() {
      changeFilter.value("pending");
      activeFilter.value = "Pending";
      hideDropdown.value = true;
      isOptionsExpanded.value = false;
    }
    function clearFilters() {
      changeFilter.value("all");
      activeFilter.value = "All";
      hideDropdown.value = true;
      isOptionsExpanded.value = true;
    }
    return {
      hideDropdown,
      activeFilter,
      isOptionsExpanded,
      dropDown,
      filterActive,
      filterInactive,
      filterPending,
      clearFilters,
    };
  },
};
</script>

<style>
.ease-custom {
  transition-timing-function: cubic-bezier(0.61, -0.53, 0.43, 1.43);
}
</style>
