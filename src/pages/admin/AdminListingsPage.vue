<template>
  <div>
    <div class="mb-12">
      <Navbar active="Listings" />
    </div>
    <div class="flex">
      <ListingCard :listings="all_listings" />
    </div>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import ListingMapper from "../../components/ListingMapper.vue";
import ListingCard from "../../components/ListingCard.vue";
export default {
  name: "AdminListingsPage",
  components: {
    Navbar,
    ListingMapper,
    ListingCard,
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
    this.all_listings.push(
      ...this.active_listings,
      ...this.inactive_listings,
      ...this.pending_listings,
      ...this.rejected_listings
    );
  },
  data() {
    return {
      listing_type: "all",
      all_listings: [],
      active_listings: [],
      inactive_listings: [],
      pending_listings: [],
      rejected_listings: [],
    };
  },
};
</script>
