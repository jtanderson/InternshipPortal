<template>
  <div class="flex flex-wrap">
    <div
      v-for="listing in listings"
      class="sm:flex-sm md:flex-md lg:flex-lg last:flex-el flex-nm m-4 shadow-lg rounded-xl bg-gray-100 cursor-pointer"
      :key="listing[1].listing.id"
      @click="toListingPage(listing[1].listing.id)"
    >
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">
          {{ listing[1].listing.position }}
        </div>
        <p class="text-black font-semibold text-base">
          Client:
          <span class="text-gray-700 font-normal">{{ listing[1].client }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Minimum Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.min_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Preferred Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.pref_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Additional Info:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.additional_info
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Responsibilities:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.pos_responsibility
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Duration:
          <span class="text-gray-700 font-normal"
            >{{
              listing[1].listing.duration != null
                ? listing[1].listing.duration + " weeks"
                : ""
            }}
          </span>
        </p>
        <p class="text-black font-semibold text-base">
          Open Date:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.app_open
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Close Date:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.app_close
          }}</span>
        </p>
        <div class="text-black font-semibold text-base">
          Tags:
          <div v-if="listing[1].tags != null && listing[1].tags.length > 0">
            <div v-for="tag in listing[1].tags" :key="tag">
              <span class="text-gray-700 font-normal"> - {{ tag }} </span>
            </div>
          </div>
          <div v-else>
            <span class="text-gray-700 font-normal"> No Tags </span>
          </div>
        </div>
        <div class="text-black font-semibold text-base">
          SU Courses:
          <div
            v-if="listing[1].courses != null && listing[1].courses.length > 0"
          >
            <div v-for="course in listing[1].courses" :key="course">
              <span class="text-gray-700 font-normal"> - {{ course }} </span>
            </div>
          </div>
          <div v-else>
            <span class="text-gray-700 font-normal"> No Courses </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BrowseListingCard",
  props: ["listings"],
  setup() {
    async function toListingPage(listing_id) {
      await fetch(`${process.env.SERVER_URL}/modify-statitics/${listing_id}`, {
        method: "PUT",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: {"statistic":"views"},
      })
        .then((res) => {
          if (res.status === 200) {
            // Need refactor, better way of routing
            window.location.href = "/admin";
          } else if (res.status === 403) {
            res.json().then((r) => {
              alert(r.err_msg);
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
        window.location.href = `/admin/listing/${listing_id}`;
    }
    return {
      toListingPage,
    };
  },
};
</script>
