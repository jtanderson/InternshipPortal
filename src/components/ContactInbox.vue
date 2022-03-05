<template>
  <div class="flex flex-col w-full m-auto">
    <div class="mt-20">
      <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
          <div
            class="
              container
              mx-auto
              flex flex-wrap
              p-5
              flex-col
              md:flex-row
              items-center
              "
          >
            <table class="shadow-md
              overflow-hidden 
              sm:px-6 
              lg:px-8 
              sm:rounded-lg 
              min-w-full 
              divide-y 
              divide-gray-200
              ">
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
                    Message
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
                    Email
                  </th>
                  <th scope="col" class="relative px-6 py-3">
                    <span class="sr-only">Edit</span>
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200 ">
                <tr v-for="message in this.all_messages" :key="message.id">
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-left">
                      <div>
                        <div class="text-sm font-medium text-gray-900">
                          {{ message[1].name }}
                        </div>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-left text-sm text-gray-900">
                        <div class="overflow-hidden truncate w-32 text-left">
                            {{ message[1].message}}
                        </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-left"> 
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
                      
                      </span>
                    </div>
                  </td>
                  
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    <div class="flex items-left"> 
                      {{ message[1].email }}
                    </div> 
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
  name: "ContactInboxModule",
  setup() {
    const all_messages = ref([]);
    onMounted(async () => {
      let result = await fetch(
        `${process.env.SERVER_URL}/admin/get-messages/all`
      ).catch((error) => {
        console.log(error);
      });
      let messages = await result.json();
      
      all_messages.value = Object.entries(messages).filter((message) => {
            return message; 
      });
      
    });
    //function toMessagePage(contact_id) {
      //window.location.href = `/admin/contactinbox?id=${contact_id}`;
   // }
    return {
      all_messages,
      //toMessagePage,
    };
  },
};
</script>
