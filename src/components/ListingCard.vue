<template>
  <div class="w-full flex flex-row flex-wrap">
    <div
      v-for="listing in this.listings"
      :key="listing.listing_id"
      class="
        max-w-sm
        m-8
        overflow-hidden
        shadow-lg
        rounded-xl
        bg-gray-100
        cursor-pointer
      "
      v-on:click="toListingPage(listing.listing_id)"
    >
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">
          {{ listing.position_info.title }}
        </div>
        <p class="text-black font-semibold text-base">
          Client:
          <span class="text-gray-700 font-normal">{{ listing.client }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Minimum Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing.position_info.min_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Preferred Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing.position_info.pref_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Responsibilities:
          <span class="text-gray-700 font-normal">{{
            listing.position_info.responsibility
          }}</span>
        </p>
      </div>
      <div class="px-6 pt-4 pb-2">
        <span
          class="
            inline-block
            bg-gray-200
            rounded-full
            px-3
            py-1
            text-sm
            font-semibold
            text-gray-700
            mr-2
            mb-2
          "
          >status: {{ listing.status }}</span
        >
        <span
          class="
            inline-block
            bg-gray-200
            rounded-full
            px-3
            py-1
            text-sm
            font-semibold
            text-gray-700
            mr-2
            mb-2
          "
          >client_id: {{ listing.client_id }}</span
        >
        <span
          class="
            inline-block
            bg-gray-200
            rounded-full
            px-3
            py-1
            text-sm
            font-semibold
            text-gray-700
            mr-2
            mb-2
          "
          >listing_id: {{ listing.listing_id }}</span
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ListingCard",
  props: ["listings"],
  methods: {
    toListingPage(listing_id) {
      window.location.href = `/admin/listing/${listing_id}`;
    },
  },
};
</script>
