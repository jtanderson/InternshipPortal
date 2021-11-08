<template>
  <div
    class="
      shadow-xl
      border-2
      rounded
      px-8
      pt-6
      pb-8
      mb-4
      flex flex-col
      my-2
      m-auto
      w-1/2
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
      <h2 class="text-2xl uppercase mb-4">Confirm</h2>
    </div>
    <div class="text-justify m-auto">
      <p>
        Would you like to request this internship listing be put on the
        Salisbury University Internship Web Portal?
      </p>
      <p id="italic-p" class="text-gray-400 text-sm italic mt-2">
        By confirming this listing, you are allowing Salisbury University to
        share the information provided to the students in the Math & Computer
        Science department. This listing will be sent to an administrator for
        review and if granted, posted to the portal.
      </p>
      <p class="text-sm mt-2">
        Contact
        <span class="text-black font-bold">gxfranchi@salisbury.edu</span> if you
        have any questions or concerns regarding your listing.
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
          v-on:click="confirmListing"
        >
          Confirm
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Confirm",
  props: ["submitListing"],
  methods: {
    confirmListing() {
      this.submitListing();
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
