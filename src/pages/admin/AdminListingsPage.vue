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
import { ref, onMounted, onUpdated } from "vue";
import Navbar from "../../components/Navbar.vue";
import ListingCard from "../../components/ListingCard.vue";
import Dropdown from "../../components/Dropdown.vue";
export default {
  name: "AdminListingsPage",
  components: {
    Navbar,
    Dropdown,
    ListingCard,
  },
  setup() {
    const listing_type = ref("all");
    const filter = ref("");
    const all_listings = ref([]);
    const active_listings = ref([]);
    const inactive_listings = ref([]);
    const pending_listings = ref([]);
    const rejected_listings = ref([]);
    const filtered_listings = ref([]);

    onMounted(async () => {
      let result = await fetch(
        `${process.env.SERVER_URL}/admin/get-listings/${listing_type.value}`
      ).catch((error) => {
        console.log(error);
      });
      let listings = await result.json();
      all_listings.value = Object.entries(listings);
      active_listings.value = filterListings("active");
      inactive_listings.value = filterListings("inactive");
      pending_listings.value = filterListings("pending");
      rejected_listings.value = filterListings("rejected");
      filtered_listings.value = Object.entries(listings);
    });

    onUpdated(async () => {
      let result = await fetch(
        `${process.env.SERVER_URL}/admin/get-listings/${listing_type.value}`
      ).catch((error) => {
        console.log(error);
      });
      let listings = await result.json();
      all_listings.value = Object.entries(listings);
      active_listings.value = filterListings("active");
      inactive_listings.value = filterListings("inactive");
      pending_listings.value = filterListings("pending");
      rejected_listings.value = filterListings("rejected");
      filtered_listings.value = Object.entries(listings);
    });

    function filterListings(filterKeyword) {
      return all_listings.value.filter((listing) => {
        if (listing[1].listing.status === filterKeyword) {
          return listing;
        }
      });
    }

    function updateFilter(newFilter) {
      filter.value = newFilter;
      filtered_listings.value = [];
      switch (filter.value) {
        case "active":
          filtered_listings.value = filterListings("active");
          break;
        case "inactive":
          filtered_listings.value = filterListings("inactive");
          break;
        case "pending":
          filtered_listings.value = filterListings("pending");
          break;
        case "rejected":
          filtered_listings.value = filterListings("rejected");
          break;
        case "all":
          filtered_listings.value = all_listings.value;
          break;
      }
    }
    return {
      filter,
      all_listings,
      active_listings,
      inactive_listings,
      pending_listings,
      rejected_listings,
      filtered_listings,
      filterListings,
      updateFilter,
    };
  },
};
</script>
