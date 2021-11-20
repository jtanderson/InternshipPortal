<template>
  <div class="flex">
    <button type="button" @click="star">
      <svg
        class="block h-8 w-8 fill-current"
        :class="{
          'text-yellow-300': isStarred,
          'text-gray-300': !isStarred,
        }"
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 20 20"
      >
        <path
          d="M10 15l-5.878 3.09 1.123-6.545L.489 6.91l6.572-.955L10 0l2.939 5.955 6.572.955-4.756 4.635 1.123 6.545z"
        />
      </svg>
    </button>
  </div>
</template>

<script>
import { ref, toRefs, onMounted, onUpdated } from "vue";
export default {
  name: "Star",
  props: {
    id: Number,
  },
  setup(props) {
    const isStarred = ref(false);
    const { id } = toRefs(props);

    onMounted(async () => {
      let result = await fetch(
        `${process.env.SERVER_URL}/admin/is-listing-starred/${id.value}`
      ).catch((error) => {
        console.log(error);
      });
      let r = await result.json();
      isStarred.value = r.star;
    });

    async function star() {
      await fetch(`${process.env.SERVER_URL}/admin/star-listing/${id.value}`, {
        method: "PUT",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
      }).then((res) => {
        if (res.status === 200) {
          isStarred.value = !isStarred.value;
        } else {
          alert("Failed to star listing");
        }
      });
    }

    return {
      isStarred,
      star,
    };
  },
};
</script>
