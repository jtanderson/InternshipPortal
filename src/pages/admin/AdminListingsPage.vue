<template>
  <div>
    <div class="mb-8">
      <Navbar active="Listings" />
      <Dropdown :changeFilter="updateFilter" />
    </div>
    <div>
      <ListingCard :listings="filtered_listings" />
    </div>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar.vue";
import ListingMapper from "../../components/ListingMapper.vue";
import ListingCard from "../../components/ListingCard.vue";
import Dropdown from "../../components/Dropdown.vue";
export default {
  name: "AdminListingsPage",
  components: {
    Navbar,
    ListingMapper,
    Dropdown,
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
      const listingObj = {
        client: listings[listing].client,
        listing: listings[listing].listing,
      };
      switch (listings[listing].listing.status) {
        case "active":
          this.active_listings.push(listingObj);
          break;
        case "inactive":
          this.inactive_listings.push(listingObj);
          break;
        case "pending":
          this.pending_listings.push(listingObj);
          break;
        case "rejected":
          this.rejected_listings.push(listingObj);
          break;
      }
    });
    this.all_listings.push(
      ...this.active_listings,
      ...this.inactive_listings,
      ...this.pending_listings,
      ...this.rejected_listings
    );
    this.filtered_listings = this.all_listings;
  },
  data() {
    return {
      listing_type: "all",
      filter: "",
      all_listings: [],
      active_listings: [],
      inactive_listings: [],
      pending_listings: [],
      rejected_listings: [],
      filtered_listings: [],
    };
  },
  methods: {
    updateFilter(newFilter) {
      this.filter = newFilter;
      this.filtered_listings = [];
      switch (this.filter) {
        case "active":
          this.filterListings("active");
          break;
        case "inactive":
          this.filterListings("inactive");
          break;
        case "pending":
          this.filterListings("pending");
          break;
        case "rejected":
          this.filterListings("rejected");
          break;
        case "all":
          this.filtered_listings = this.all_listings;
      }
    },
    filterListings(filterKeyword) {
      this.all_listings.filter((obj, index) => {
        console.log(obj);
        if (obj.listing.status == filterKeyword) {
          this.filtered_listings.push(obj);
        }
      });
    },
  },
};
</script>
