<template>
  <div class="flex">
    <button type="button" v-on:click="star">
      <svg
        class="block h-8 w-8 fill-current"
        :class="starring ? 'text-gray-300' : 'text-yellow-300'"
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
export default {
  name: "Star",
  props: ["starred"],
  data() {
    return {
      starring: this.starred,
    };
  },
  methods: {
    star() {
      this.starring = !this.starring;
    },
  },
};
</script>
