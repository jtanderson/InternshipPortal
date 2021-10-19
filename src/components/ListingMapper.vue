<template>
  <div>
    <p v-for="listing in this.listings" :key="listing.client_id" class="mb-4">
      Client: {{ listing.client }} <br />
      Title: {{ listing.position_info.title }}<br />
      Minimum Qualifications:
      {{ listing.position_info.min_qualifications }} <br />
      Preferred Qualifications:
      {{ listing.position_info.pref_qualifications }}<br />
      Responsibility: {{ listing.position_info.responsibility }}
    </p>
  </div>
</template>

<script>
export default {
  name: "ListingMapper",
  props: ["listings"],
};
</script>
