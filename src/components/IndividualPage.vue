<template>
  <div
    class="shadow-xl border-2 rounded px-8 pt-6 pb-8 mb-4 flex flex-col my-2 m-auto w-1/2 mt-12"
  >
    <div class="text-center mb-12 mt-4">
      <div class="text-3xl font-extrabold">{{ position }}</div>
    </div>
    <div class="text-justify mb-12">
      <div class="text-lg p-2">
        <span class="font-bold"> Minimum Qualifications: </span
        >{{ min_qualifications }}
      </div>
      <div class="text-lg p-2">
        <span class="font-bold"> Prefered Qualifications: </span
        >{{ pref_qualifications }}
      </div>
      <div class="text-lg p-2">
        <span class="font-bold"> Position Responsibilities: </span
        >{{ pos_responsibility }}
      </div>
      <div v-if="additional_info">
        <div class="text-lg p-2">
          <span class="font-bold"> Additional Information: </span
          >{{ additional_info }}
        </div>
      </div>
      <div class="text-lg p-2">
        <span class="font-bold"> Duration: </span>{{ duration }} weeks
      </div>
      <div class="text-lg p-2">
        <span class="font-bold"> Application Open Date: </span>{{ app_open }}
      </div>
      <div class="text-lg p-2">
        <span class="font-bold"> Application Close Date: </span>{{ app_close }}
      </div>
    </div>
    <div v-if="app_link != null" class="mx-auto">
      <a :href="app_link" @click="incrementApplications">
        <button
          class="bg-primary hover:bg-primaryOffset text-white font-bold py-2 px-4 rounded w-full"
        >
          Apply
        </button>
      </a>
    </div>
    <div v-if="app_link == null" class="mx-auto">
      <button
        class="bg-primary hover:bg-primaryOffset text-white font-bold py-2 px-4 rounded w-full cursor-not-allowed"
        disabled
      >
        No Application Link
      </button>
    </div>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
export default {
  name: "IndividualPage",
  setup() {
    const listing = ref({});
    const id = ref("");
    const position = ref("");
    const min_qualifications = ref("");
    const pref_qualifications = ref("");
    const pos_responsibility = ref("");
    const additional_info = ref("");
    const duration = ref("");
    const app_open = ref("");
    const app_close = ref("");
    const app_link = ref("");
    onMounted(async () => {
      let uri = window.location.search.substring(1);
      let params = new URLSearchParams(uri);
      let lid = params.get("id");
      let result = await fetch(
        `${process.env.SERVER_URL}/get-listing/${lid}`
      ).catch((error) => {
        console.log(error);
      });
      let l = await result.json();
      console.log(l);
      id.value = l.listing.id;
      position.value = l.listing.position;
      min_qualifications.value = l.listing.min_qualifications;
      pref_qualifications.value = l.listing.pref_qualifications;
      pos_responsibility.value = l.listing.pos_responsibility;
      additional_info.value = l.listing.additional_info;
      duration.value = l.listing.duration;
      app_open.value = l.listing.app_open;
      app_close.value = l.listing.app_close;
      app_link.value = l.listing.app_link;
      console.log("link", l.listing.app_link);
    });

    async function incrementApplications() {
      const toSend = {
        statistic: "applications",
      };
      await fetch(`${process.env.SERVER_URL}/modify-statistics/${id.value}`, {
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
            console.log("SUCCESS");
            window.location.href = `/listing?id=${listing_id}`;
          } else if (res.status === 404) {
            console.log("FAILED");
          } else {
            console.log("ERROR");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }
    return {
      id,
      position,
      min_qualifications,
      pref_qualifications,
      pos_responsibility,
      additional_info,
      duration,
      app_open,
      app_close,
      app_link,
      incrementApplications,
    };
  },
};
</script>
