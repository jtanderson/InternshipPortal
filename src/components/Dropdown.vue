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
        @click="dropDown"
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
          v-if="!hideDropdown"
        >
          <li>
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
              @click="clearFilters"
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
              @click="filterActive"
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
              @click="filterInactive"
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
              @click="filterPending"
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
import { ref } from "vue";
export default {
  name: "Dropdown",
  props: ["changeFilter"],
  setup() {
    const hideDropdown = ref(true);
    const activeFilter = ref("Filter");
    const isOptionsExpanded = ref(false);
    function dropDown() {
      hideDropdown.value = !hideDropdown.value;
      isOptionsExpanded.value = !isOptionsExpanded.value;
    }
    function filterActive() {
      this.changeFilter("active");
      activeFilter.value = "Active";
      hideDropdown.value = true;
      isOptionsExpanded.value = false;
    }
    function filterInactive() {
      this.changeFilter("inactive");
      activeFilter.value = "Inactive";
      hideDropdown.value = true;
      isOptionsExpanded.value = true;
    }
    function filterPending() {
      this.changeFilter("pending");
      activeFilter.value = "Pending";
      hideDropdown.value = true;
      isOptionsExpanded.value = false;
    }
    function clearFilters() {
      this.changeFilter("all");
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
