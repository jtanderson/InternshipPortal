<template>
  <div class="flex flex-wrap overflow-hidden">
    <div
      v-for="listing in listings"
      class="
        sm:flex-sm
        md:flex-md
        lg:flex-lg
        last:flex-el
        flex-nm
        m-4
        shadow-lg
        rounded-xl
        bg-gray-100
      "
      :key="listing[0]"
    >
      <div class="relative">
        <div class="absolute top-0 right-0 p-4">
          <Star :id="listing[1].listing.id" />
        </div>
      </div>
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">
          {{ listing[1].listing.position }}
        </div>
        <p class="text-black font-semibold text-base">
          Client:
          <span class="text-gray-700 font-normal">{{ listing[1].client }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Minimum Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.min_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Preferred Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.pref_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Additional Info:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.additional_info
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Responsibilities:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.pos_responsibility
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Duration:
          <span class="text-gray-700 font-normal"
            >{{
              listing[1].listing.duration != null
                ? listing[1].listing.duration + " weeks"
                : ""
            }}
          </span>
        </p>
        <p class="text-black font-semibold text-base">
          Open Date:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.app_open
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Close Date:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.app_close
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
            listing[1].listing.status == 'active'
              ? 'bg-green-300'
              : listing[1].listing.status == 'rejected'
              ? 'bg-red-300'
              : listing[1].listing.status == 'pending'
              ? 'bg-yellow-300'
              : listing[1].listing.status == 'inactive'
              ? 'bg-blue-300'
              : 'bg-gray-200'
          "
          >status: {{ listing[1].listing.status }}</span
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
          >client_id: {{ listing[1].listing.client_id }}</span
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
          >listing_id: {{ listing[1].listing.id }}</span
        >
        <!-- <v-icon
          name="edit"
          @click="editListing(listing[1].listing..id)"
          class="float-right cursor-pointer"
          scale="1.4"
        ></v-icon> -->
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
  setup() {
    function toListingPage(listing_id) {
      window.location.href = `/admin/listing/${listing_id}`;
    }
    function editListing(listing_id) {
      window.location.href = `/admin/edit/listing?id=${listing_id}`;
    }
    return {
      toListingPage,
      editListing,
    };
  },
};
</script>
