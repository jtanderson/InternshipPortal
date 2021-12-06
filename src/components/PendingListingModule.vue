<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="flex flex-col w-5/6 m-auto">
    <div class="mt-20">
      <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
          <div
            class="
              shadow
              overflow-hiddensm:px-6 lg:px-8
              border-b border-gray-200
              sm:rounded-lg
            "
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
                    Company
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
                <tr v-for="listing in this.all_listings" :key="listing.id">
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-center">
                      <div>
                        <div class="text-sm font-medium text-gray-900">
                          {{ listing[1].client }}
                        </div>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="text-sm text-gray-900">
                      {{ listing[1].listing.position }}
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
                        bg-yellow-200
                        text-yellow-600
                      "
                    >
                      {{ listing[1].listing.status }}
                    </span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    Internship
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
                    <button
                      @click="toEditListingPage(listing[1].listing.id)"
                      class="text-indigo-600 hover:text-indigo-900"
                    >
                      Edit
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
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
    // TODO: Weird indexing here due to the way I get the response, need to fix this eventually
    onMounted(async () => {
      let result = await fetch(
        `${process.env.SERVER_URL}/admin/get-listings/all`
      ).catch((error) => {
        console.log(error);
      });
      let listings = await result.json();
      // console.log(listings);
      // Object.entries(listings).forEach((listing) => {
      //   console.log(listing);
      // });
      all_listings.value = Object.entries(listings).filter((listing) => {
        if (listing[1].listing.status === "pending") {
          return listing;
        }
      });
      // console.log(all_listings.value);
    });
    function toEditListingPage(listing_id) {
      window.location.href = `/admin/edit/listing?id=${listing_id}`;
    }
    return {
      all_listings,
      toEditListingPage,
    };
  },
};
</script>