<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="flex flex-col w-3/4 m-auto h-screen">
    <h1 class="text-3xl">New Pending Listings</h1>
    <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
      <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
        <div
          class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg"
        >
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th
                  scope="col"
                  class="
                    px-6
                    py-3
                    text-left text-xs
                    font-medium
                    text-gray-500
                    uppercase
                    tracking-wider
                  "
                >
                  Name
                </th>
                <th
                  scope="col"
                  class="
                    px-6
                    py-3
                    text-left text-xs
                    font-medium
                    text-gray-500
                    uppercase
                    tracking-wider
                  "
                >
                  Title
                </th>
                <th
                  scope="col"
                  class="
                    px-6
                    py-3
                    text-left text-xs
                    font-medium
                    text-gray-500
                    uppercase
                    tracking-wider
                  "
                >
                  Status
                </th>
                <th
                  scope="col"
                  class="
                    px-6
                    py-3
                    text-left text-xs
                    font-medium
                    text-gray-500
                    uppercase
                    tracking-wider
                  "
                >
                  Role
                </th>
                <th scope="col" class="relative px-6 py-3">
                  <span class="sr-only">Edit</span>
                </th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr
                v-for="listing in this.all_listings"
                :key="listing.listing.id"
              >
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div>
                      <div class="text-sm font-medium text-gray-900">
                        {{ listing.client }}
                      </div>
                      <div class="text-sm text-gray-500">
                        {{ listing.client }}
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">{{ listing.client }}</div>
                  <div class="text-sm text-gray-500">
                    {{ listing.client }}
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span
                    class="
                      px-2
                      inline-flex
                      text-xs
                      leading-5
                      font-semibold
                      rounded-full
                      bg-green-100
                      text-green-800
                    "
                  >
                    Active
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  {{ listing.client }}
                </td>
                <td
                  class="
                    px-6
                    py-4
                    whitespace-nowrap
                    text-right text-sm
                    font-medium
                  "
                >
                  <a href="#" class="text-indigo-600 hover:text-indigo-900"
                    >Edit</a
                  >
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "PendingListingModule",
  setup() {
    const all_listings = ref([]);
    onMounted(async () => {
      let local_listings = [];
      let result = await fetch(
        `${process.env.SERVER_URL}/admin/get-listings/all`
      ).catch((error) => {
        console.log(error);
      });
      let listings = await result.json();
      Object.keys(listings).forEach((listing) => {
        const listingObj = {
          client: listings[listing].client,
          listing: listings[listing].listing,
        };
        if (listings[listing].listing.status == "pending") {
          local_listings.push(listings[listing].listing);
        }
        //   switch (listings[listing].listing.status) {
        //     case "active":
        //       this.active_listings.push(listingObj);
        //       break;
        //     case "inactive":
        //       this.inactive_listings.push(listingObj);
        //       break;
        //     case "pending":
        //       this.pending_listings.push(listingObj);
        //       break;
        //     case "rejected":
        //       this.rejected_listings.push(listingObj);
        //       break;
        //   }
      });
      all_listings.value = local_listings;
      // this.all_listings.push(
      //   ...this.active_listings,
      //   ...this.inactive_listings,
      //   ...this.pending_listings,
      //   ...this.rejected_listings
      // );
      // this.filtered_listings = this.all_listings;
    });
    return {
      all_listings,
    };
  },
};
</script>