<template>
  <div class="sm:items-center sm:flex sm:justify-between mx-48 mt-12">
    <form action="" class="flex mt-2 sm:mt-0">
      <div>
        <InboxFilterDropdown :changeFilter="updateFilter" />
      </div>

      <div class="ml-4">
        <!--InboxSortDropdown :changeFilter="sortMessages" /-->
      </div>
    </form>
  </div>
  <div class="mt-10 flex justify-center items-center">
    <div class="pt-2 relative mx-auto text-gray-600">
      <input
        class="border-2 border-gray-300 bg-white h-10 w-72 px-5 pr-16 rounded-lg text-sm focus:outline-none"
        type="text"
        name="search"
        :placeholder="`Search by ${filterValue}`"
        v-model="searchTerm"
        @input="filterMessages"
      />
      <button type="submit" class="absolute right-0 top-0 mt-5 mr-4">
        <svg
          class="text-gray-600 h-4 w-4 fill-current"
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          version="1.1"
          id="Capa_1"
          x="0px"
          y="0px"
          viewBox="0 0 56.966 56.966"
          style="enable-background: new 0 0 56.966 56.966"
          xml:space="preserve"
          width="512px"
          height="512px"
        >
          <path
            d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import InboxFilterDropdown from "./InboxFilterDropdown.vue"
export default {
  name: "InboxSearchBar",
  components: {
    InboxFilterDropdown
  },
  setup() {
    const all_messages = ref([]);
    const filtered_messages = ref([]);
    const searchTerm = ref("");
    const filterValue = ref("name");
    const sortValue = ref("name-asc");

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

    function updateFilter(filter) {
      filterValue.value = filter;
    }

    function filterMessages() {
      if (searchTerm.value == "") {
        filtered_messages.value = all_messages.value;
      } else {
        switch (filterValue.value) {
          case "name":
            filtered_messages.value = all_messages.value.filter((message) => {
              if (
                message[1].name
                  .toLowerCase()
                  .includes(searchTerm.value.toLowerCase())
              ) {
                return message;
              }
            });
            break;
          case "email":
            filtered_messages.value = all_messages.value.filter((message) => {
              if (
                message[1].email
                  .toLowerCase()
                  .includes(searchTerm.value.toLowerCase())
              ) {
                return message;
              }
            });
            break;
          case "message":
            filtered_messages.value = all_messages.value.filter((message) => {
              if (
                message[1].message
                  .toLowerCase()
                  .includes(searchTerm.value.toLowerCase())
              ) {
                return message;
              }
            });
            break;
        }
      }
    }

    function sortMessages(sort) {
      sortValue.value = sort;
      switch (sortValue.value) {
        case "name-asc":
          filtered_messages.value = filtered_messages.value.sort((a, b) => {
            if (
              a[1].message.toLowerCase()[0] <
              b[1].message.toLowerCase()[0]
            )
              return -1;
            if (
              a[1].message.toLowerCase()[0] >
              b[1].message.toLowerCase()[0]
            )
              return 1;
            return 0;
          });
          break;
        case "name-desc":
          filtered_messages.value = filtered_messages.value.sort((a, b) => {
            if (
              a[1].name.toLowerCase()[0] >
              b[1].name.toLowerCase()[0]
            )
              return -1;
            if (
              a[1].name.toLowerCase()[0] <
              b[1].name.toLowerCase()[0]
            )
              return 1;
            return 0;
          });
          break;
        case "email-asc":
          filtered_messages.value = filtered_messages.value.sort((a, b) => {
            if (a[1].email.toLowerCase()[0] < b[1].email.toLowerCase()[0])
              return -1;
            if (a[1].email.toLowerCase()[0] > b[1].email.toLowerCase()[0])
              return 1;
            return 0;
          });
          break;
        case "email-desc":
          filtered_messages.value = filtered_messages.value.sort((a, b) => {
            if (a[1].email.toLowerCase()[0] > b[1].email.toLowerCase()[0])
              return -1;
            if (a[1].email.toLowerCase()[0] < b[1].email.toLowerCase()[0])
              return 1;
            return 0;
          });
          break;
      }
    }

    return {
      filterMessages,
      sortMessages,
      updateFilter,
      all_messages,
      filtered_messages,
      searchTerm,
      filterValue,
      sortValue,
    };
  },
};
</script>