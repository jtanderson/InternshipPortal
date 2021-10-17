<template>
  <div>
    <div class="mb-12">
      <Navbar active="Listings" />
    </div>
    <div class="flex h-screen">
      <div class="rounded border-2 border-black w-full h-full">
        <h1 class="text-center text-2xl mb-4">Pending</h1>
        {{ pending_listings }}
      </div>
      <div class="rounded border-2 border-black w-full h-full">
        <h1 class="text-center text-2xl mb-4">Active</h1>
        <div class="ml-2">
          <p
            v-for="listing in active_listings"
            :key="listing.client_id"
            class="mb-4"
          >
            Client: {{ listing.client }} <br />
            Title: {{ listing.position_info.title }}<br />
            Minimum Qualifications:
            {{ listing.position_info.min_qualifications }} <br />
            Preferred Qualifications:
            {{ listing.position_info.pref_qualifications }}<br />
            Responsibility: {{ listing.position_info.responsibility }}
          </p>
        </div>
      </div>
      <div class="rounded border-2 border-black w-full h-full">
        <h1 class="text-center text-2xl mb-4">Inactive</h1>
        {{ inactive_listings }}
      </div>
      <div class="rounded border-2 border-black w-full h-full">
        <h1 class="text-center text-2xl mb-4">Rejected</h1>
        {{ rejected_listings }}
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
export default {
  name: "AdminListingsPage",
  components: {
    Navbar,
  },
  async mounted() {
    let result = await fetch(
      `${process.env.SERVER_URL}/admin/get-listings/${this.listing_type}`
    ).catch((error) => {
      console.log(error);
    });
    let listings = await result.json();
    Object.keys(listings).forEach((listing) => {
      this.active_listings.push(listings[listing]);
      console.log(listings[listing]);
    });
  },
  data() {
    return {
      listing_type: "active",
      pending_listings: [],
      active_listings: [],
      inactive_listings: [],
      rejected_listings: [],
    };
  },
};
</script>
