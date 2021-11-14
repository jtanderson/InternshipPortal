<template>
  <div class="flex flex-wrap overflow-hidden">
    <div
      v-for="listing in this.listings"
      :key="listing.listing.id"
      class="
        sm:flex-sm
        md:flex-md
        lg:flex-lg
        flex-nm
        m-4
        shadow-lg
        rounded-xl
        bg-gray-100
      "
    >
      <!--v-on:click="toListingPage(listing.listing.id)"  -->
      <div class="relative">
        <div class="absolute top-0 right-0 p-4">
          <Star :id="listing.listing.id" :starred="listing.listing.starred" />
        </div>
      </div>
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">
          {{ listing.client }}
        </div>
        <p class="text-black font-semibold text-base">
          Client:
          <span class="text-gray-700 font-normal">{{ listing.client }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Minimum Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing.listing.min_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Preferred Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing.listing.pref_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Additional Info:
          <span class="text-gray-700 font-normal">{{
            listing.listing.additional_info
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Responsibilities:
          <span class="text-gray-700 font-normal">{{
            listing.listing.pos_responsibility
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
            listing.listing.status == 'active'
              ? 'bg-green-300'
              : listing.listing.status == 'rejected'
              ? 'bg-red-300'
              : listing.listing.status == 'pending'
              ? 'bg-yellow-300'
              : listing.listing.status == 'inactive'
              ? 'bg-yellow-500'
              : 'bg-gray-200'
          "
          >status: {{ listing.listing.status }}</span
        >
        <!-- Remove below once done with development -->
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
          >client_id: {{ listing.listing.client_id }}</span
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
          >listing_id: {{ listing.listing.id }}</span
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
  },
};
</script>
