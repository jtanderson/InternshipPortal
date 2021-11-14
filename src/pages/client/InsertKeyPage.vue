<template>
  <div class="flex h-screen justify-center items-center">
    <div class="col-span-6 sm:col-span-3 lg:col-span-2">
      <label class="block font-medium text-2xl font-sans mb-2"
        >Secret Key</label
      >
      <div class="flex">
        <input
          type="text"
          autofocus
          autocomplete="off"
          placeholder="*********"
          class="
            bg-gray-200
            mt-4
            px-4
            py-3
            mr-4
            block
            w-full
            outline-none
            border-none
            shadow-xl
            sm:text-sm
            rounded-lg
          "
        />
        <button
          @click="submitKey"
          type="submit"
          class="
            text-white
            bg-primary
            mt-4
            px-4
            py-3
            block
            w-1/3
            outline-none
            border-none
            shadow-xl
            sm:text-sm
            rounded-lg
          "
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M14 5l7 7m0 0l-7 7m7-7H3"
            ></path>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InsertKeyPage",
  setup() {
    function submitKey() {
      window.location.href = "/insert-listing";
    }
    return {
      submitKey,
    };
  },
};
</script>
