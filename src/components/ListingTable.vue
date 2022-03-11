<template>
  <div class="flex flex-col w-3/4 m-auto h-screen">
    <div class="mt-20">
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
                    class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                  >
                    Company
                  </th>
                  <th
                    scope="col"
                    class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                  >
                    Title
                  </th>
                  <th
                    scope="col"
                    class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                  >
                    Tags
                  </th>
                  <th
                    scope="col"
                    class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                  >
                    SU Courses
                  </th>
                  <th scope="col" class="relative px-6 py-3">
                    <span class="sr-only">Edit</span>
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200 cursor-pointer">
                <tr
                  v-for="listing in listings"
                  :key="listing.id"
                  class="hover:bg-gray-50"
                  @click="viewListing(listing[1].listing.id)"
                >
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
                    <div
                      v-if="
                        listing[1].tags != null && listing[1].tags.length > 0
                      "
                    >
                      <div v-for="tag in listing[1].tags" :key="tag">
                        <span
                          class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-200 text-gray-600"
                        >
                          {{ tag }}
                        </span>
                      </div>
                    </div>
                    <div v-else>
                      <span
                        class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-200 text-red-600"
                      >
                        No Tags
                      </span>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div
                      v-if="
                        listing[1].courses != null &&
                        listing[1].courses.length > 0
                      "
                    >
                      <div v-for="course in listing[1].courses" :key="course">
                        <span
                          class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-200 text-gray-600"
                        >
                          {{ course }}
                        </span>
                      </div>
                    </div>
                    <div v-else>
                      <span
                        class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-200 text-red-600"
                      >
                        No Courses
                      </span>
                    </div>
                  </td>
                  <td
                    class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
                  />
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
export default {
  name: "ListingTable",
  props: ["listings"],
  setup() {
    function viewListing(id) {
      window.location.href = `/view-listing/${id}`;
    }
    return {
      viewListing,
    };
  },
};
</script>
