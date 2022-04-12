<template>
  <div class="flex flex-wrap mx-auto my-auto">
    <div
      v-for="listing in listings"
      class="sm:flex-sm md:flex-md lg:flex-lg last:flex-el flex-nm m-4 shadow-xl rounded-xl bg-white cursor-pointer"
      :key="listing[1].listing.id"
      @click="toListingPage(listing[1].listing.id)"
    >
      <div class="px-6 py-4">
        <div class="text-red-700 font-bold text-xl mb-2">
          {{ listing[1].listing.position }}
        </div>
        <p v-if="listing[1].listing.client != null" class="text-gray-900 font-semibold text-base">
          Client:
          <span class="text-gray-700 font-normal">{{ listing[1].client }}</span>
        </p>
        <p class="text-gray-900 font-semibold text-base">
          Minimum Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.min_qualifications
          }}</span>
        </p>
        <p v-if="listing[1].listing.pref_qualifications != null" class="text-gray-900 font-semibold text-base">
          Preferred Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.pref_qualifications
          }}</span>
        </p>
        <p v-if="listing[1].listing.additional_info != null" class="text-gray-900 font-semibold text-base">
          
          Additional Info:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.additional_info
          }}</span>
          
        </p>
        <p v-if="listing[1].listing.pos_responsibility != null" class="text-gray-900 font-semibold text-base">
          Responsibilities:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.pos_responsibility
          }}</span>
        </p>
        <p v-if="listing[1].listing.duration != null" class="text-gray-900 font-semibold text-base">
          Duration:
          <span class="text-gray-700 font-normal"
            >{{
              listing[1].listing.duration != null
                ? listing[1].listing.duration + " weeks"
                : ""
            }}
          </span>
        </p>
        <p class="text-gray-900 font-semibold text-base">
          Open Date:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.app_open
          }}</span>
        </p>
        <p class="text-gray-900 font-semibold text-base">
          Close Date:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.app_close
          }}</span>
        </p>
        <div class="text-gray-900 font-semibold text-base">
          Tags:
          <div v-if="listing[1].tags != null && listing[1].tags.length > 0">
            <div v-for="tag in listing[1].tags" :key="tag">
              <span
              class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-200 text-gray-600"
              >
                {{ tag }}
              </span>
            </div>
          </div>
          <div v-else>
            <span class="text-gray-700 font-normal"> No Tags </span>
          </div>
        </div>
        <div class="text-gray-900 font-semibold text-base">
          SU Courses:
          <div
            v-if="listing[1].courses != null && listing[1].courses.length > 0"
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
            <span class="text-gray-700 font-normal"> No Courses </span>
          </div>
        </div>
      </div>
    </div>
    <Modal
                  v-if="show_modal"
                  :ModalTitleProp="modal_title"
                  :ModalMessageProp="modal_message"
    />
  </div>
</template>

<script>
import { ref } from "vue";
import Modal from "./Modal.vue";
export default {
  name: "BrowseListingCard",
  props: ["listings"],
  components: {
    Modal,
  },
  setup() {
    const modal_title = ref("");
    const modal_message = ref("");
    const show_modal = ref(false);
    const toSend = {
        statistic: 'views'
    };
    async function toListingPage(listing_id) {
      await fetch(`${process.env.SERVER_URL}/modify-statitics/${listing_id}`, {
        method: "PUT",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(toSend),
      })
        .then((res) => {
          if (res.status === 200) {
            show_modal.value = true;
            modal_title.value = "Submit Success!";
            modal_message.value = "Listing views incremented successfully";
            
          }else if (res.status === 404) {
            show_modal.value = true;
            modal_title.value = "Submit Failed!";
            modal_message.value = "Listing views not incremented successfully";
          } else {
            show_modal.value = true;
            modal_title.value = "Error!";
            modal_message.value =
            "An error occurred  while submitting. Please try again.";
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }
    return {
      show_modal,
      modal_title,
      modal_message,
      toListingPage,
    };
  },
};
</script>
