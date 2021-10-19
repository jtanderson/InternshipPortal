<template>
  <div>
    <div class="mb-12">
      <Navbar active="Listings" />
    </div>
    <div class="flex h-screen">
      <div class="rounded border-2 border-black w-full h-full">
        <h1 class="text-center text-2xl mb-4 font-bold mt-4">Pending</h1>
        <div class="ml-2">
          <ListingMapper :listings="pending_listings" />
        </div>
      </div>
      <div class="rounded border-2 border-black w-full h-full">
        <h1 class="text-center text-2xl mb-4 font-bold mt-4">Active</h1>
        <div class="ml-2">
          <ListingMapper :listings="active_listings" />
        </div>
      </div>
      <div class="rounded border-2 border-black w-full h-full">
        <h1 class="text-center text-2xl mb-4 font-bold mt-4">Inactive</h1>
        <div class="ml-2">
          <ListingMapper :listings="inactive_listings" />
        </div>
      </div>
      <div class="rounded border-2 border-black w-full h-full">
        <h1 class="text-center text-2xl mb-4 font-bold mt-4">Rejected</h1>
        <div class="ml-2">
          <ListingMapper :listings="rejected_listings" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import ListingMapper from "../../components/ListingMapper.vue";
export default {
  name: "AdminListingsPage",
  components: {
    Navbar,
    ListingMapper,
  },
  async mounted() {
    let result = await fetch(
      `${process.env.SERVER_URL}/admin/get-listings/${this.listing_type}`
    ).catch((error) => {
      console.log(error);
    });
    let listings = await result.json();
    Object.keys(listings).forEach((listing) => {
      switch (listings[listing].status) {
        case "active":
          this.active_listings.push(listings[listing]);
          break;
        case "inactive":
          this.inactive_listings.push(listings[listing]);
          break;
        case "pending":
          this.pending_listings.push(listings[listing]);
          break;
        case "rejected":
          this.rejected_listings.push(listings[listing]);
          break;
      }
    });
  },
  data() {
    return {
      listing_type: "all",
      active_listings: [],
      inactive_listings: [],
      pending_listings: [],
      rejected_listings: [],
    };
  },
};
</script>
