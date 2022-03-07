<template>
  <div class="pt-10">
    <div class="relative inline-block text-left">
      <div>
        <button
          type="button"
          class="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none"
          id="menu-button"
          aria-expanded="true"
          aria-haspopup="true"
          @click="dropDown"
        >
          {{ activeSort }}
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
        class="origin-top-right absolute left-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
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
            @click="filterTitleAsc"
            >Title, A-Z</a
          >
          <a
            href="#"
            class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-100"
            role="menuitem"
            tabindex="-1"
            id="menu-item-1"
            @click="filterTitleDesc"
            >Title, Z-A</a
          >
          <a
            href="#"
            class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-100"
            role="menuitem"
            tabindex="-1"
            id="menu-item-2"
            @click="filterCompanyAsc"
            >Company, A-Z</a
          >
          <a
            href="#"
            class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-100"
            role="menuitem"
            tabindex="-1"
            id="menu-item-3"
            @click="filterCompanyDesc"
            >Company, Z-A</a
          >
          <a
            href="#"
            class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-100"
            role="menuitem"
            tabindex="-1"
            id="menu-item-4"
            @click="filterWageDesc"
            >Wage, High-Low</a
          >
          <a
            href="#"
            class="text-gray-700 block px-4 py-2 text-sm hover:bg-gray-100"
            role="menuitem"
            tabindex="-1"
            id="menu-item-5"
            @click="filterWageAsc"
            >Wage, Low-High</a
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, toRefs } from "vue";
export default {
  name: "BrowseSortDropdown",
  props: {
    changeFilter: Function,
  },
  setup(props) {
    const { changeFilter } = toRefs(props);
    const hideDropdown = ref(true);
    const activeSort = ref("Title, A-Z");
    const isOptionsExpanded = ref(false);
    function dropDown() {
      hideDropdown.value = !hideDropdown.value;
      isOptionsExpanded.value = !isOptionsExpanded.value;
    }
    function filterTitleAsc() {
      changeFilter.value("title-asc");
      activeSort.value = "Title, A-Z";
      hideDropdown.value = true;
      isOptionsExpanded.value = false;
    }
    function filterTitleDesc() {
      changeFilter.value("title-desc");
      activeSort.value = "Title, Z-A";
      hideDropdown.value = true;
      isOptionsExpanded.value = true;
    }
    function filterCompanyAsc() {
      changeFilter.value("company-asc");
      activeSort.value = "Company, A-Z";
      hideDropdown.value = true;
      isOptionsExpanded.value = false;
    }
    function filterCompanyDesc() {
      changeFilter.value("company-desc");
      activeSort.value = "Company, Z-A";
      hideDropdown.value = true;
      isOptionsExpanded.value = true;
    }
    function filterWageDesc() {
      changeFilter.value("wage-desc");
      activeSort.value = "Wage, High-Low";
      hideDropdown.value = true;
      isOptionsExpanded.value = true;
    }
    function filterWageAsc() {
      changeFilter.value("wage-asc");
      activeSort.value = "Wage, Low-High";
      hideDropdown.value = true;
      isOptionsExpanded.value = true;
    }
    return {
      hideDropdown,
      activeSort,
      isOptionsExpanded,
      dropDown,
      filterTitleAsc,
      filterTitleDesc,
      filterCompanyAsc,
      filterCompanyDesc,
      filterWageDesc,
      filterWageAsc,
    };
  },
};
</script>

<style>
.ease-custom {
  transition-timing-function: cubic-bezier(0.61, -0.53, 0.43, 1.43);
}
</style>
