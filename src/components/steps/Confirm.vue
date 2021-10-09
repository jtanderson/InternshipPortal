<template>
  <div
    class="
      bg-gray-200
      shadow-md
      border-2
      rounded
      px-8
      pt-6
      pb-8
      mb-4
      flex flex-col
      my-2
      m-auto
      w-3/4
    "
  >
    <div
      class="
        block
        uppercase
        tracking-wide
        text-grey-darker text-xs
        font-bold
        mb-2
        mt-6
        text-center
      "
    >
      <h2 class="text-2xl uppercase">Confirm</h2>
    </div>
    <div class="text-justify m-auto">
      <p>
        Would you like to put this internship listing on the Salisbury
        University Internship Web Portal?
      </p>
      <p id="italic-p" class="text-gray-400 text-sm italic">
        By confirming your listing you are allowing Salisbury University to
        share the information you provided to their student
      </p>
      <div class="flex justify-center">
        <button
          class="
            inline-flex
            text-white
            border-0
            py-2
            px-4
            focus:outline-none
            rounded
            text-md
            mb-4
            mt-4
          "
          v-on:click="submitListing"
        >
          Confirm Listing
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Confirm",
  methods: {
    submitListing() {
      fetch(`${process.env.SERVER_URL}/submit`);
    },
  },
};
</script>

<style scoped>
button {
  background-color: rgba(16, 185, 129, 1);
}
button:hover {
  background-color: rgb(43, 231, 168);
}
#italic-p {
  font-style: italic;
  color: rgba(107, 114, 128, 1);
}
</style>
