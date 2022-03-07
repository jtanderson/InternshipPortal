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
                    Role
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
                    <div v-for="tag in listing[1].tags" :key="tag">
                      <div v-if="tag == 'data structures and algorithms'">
                        <span
                          class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-yellow-200 text-yellow-600"
                        >
                          {{ tag }}
                        </span>
                      </div>
                      <div v-else-if="tag == 'database'">
                        <span
                          class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-200 text-blue-600"
                        >
                          {{ tag }}
                        </span>
                      </div>
                      <div v-else-if="tag == 'web development'">
                        <span
                          class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-200 text-red-600"
                        >
                          {{ tag }}
                        </span>
                      </div>
                      <div v-else-if="tag == 'mobile development'">
                        <span
                          class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-green-200 text-green-600"
                        >
                          {{ tag }}
                        </span>
                      </div>
                      <div v-else-if="tag == 'machine learning'">
                        <span
                          class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-purple-200 text-purple-600"
                        >
                          {{ tag }}
                        </span>
                      </div>
                      <div v-else>
                        <span
                          class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-200 text-gray-600"
                        >
                          {{ tag }}
                        </span>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    Internship
                  </td>
                  <td
                    class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
                  >
                    <button class="text-indigo-600 hover:text-indigo-900">
                      View
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
export default {
  name: "ListingTable",
  props: ["listings"],
};
</script>
