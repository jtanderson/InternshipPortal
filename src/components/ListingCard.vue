<template>
  <div class="flex flex-row flex-wrap">
    <div
      v-for="listing in this.listings"
      :key="listing.listing_id"
      class="
        w-3/4
        sm:w-full
        md:w-3/4
        lg:w-1/3
        xl:w-1/3
        2xl:w-1/5
        m-8
        overflow-hidden
        shadow-lg
        rounded-xl
        bg-gray-100
      "
    >
      <!--v-on:click="toListingPage(listing.listing_id)"  -->
      <div class="relative">
        <div class="absolute top-0 right-0 p-4">
          <Star :starred="starListing" />
        </div>
      </div>
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
            rounded-full
            px-3
            py-1
            text-sm
            font-semibold
            text-gray-700
            mr-2
            mb-2
          "
          :class="
            listing.status == 'active'
              ? 'bg-green-300'
              : listing.status == 'rejected'
              ? 'bg-red-300'
              : listing.status == 'pending'
              ? 'bg-yellow-300'
              : listing.status == 'inactive'
              ? 'bg-yellow-500'
              : 'bg-gray-200'
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
import Star from "./Star.vue";
export default {
  name: "ListingCard",
  props: ["listings"],
  components: {
    Star,
  },
  data() {
    return {
      starred: false,
    };
  },
  methods: {
    toListingPage(listing_id) {
      window.location.href = `/admin/listing/${listing_id}`;
    },
    starListing() {},
  },
};
</script>
