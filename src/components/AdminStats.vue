<template>
  <section
    class="
      bg-white
      border-2 border-gray-100
      h-1/2
      w-1/4
      body-font
      rounded-xl
      mt-2
      ml-2
      align-middle
      shadow-2xl
    "
  >
    <div class="container px-5 py-5">
      <div class="flex flex-wrap w-full mb-8">
        <div class="w-full mb-6 lg:mb-0">
          <h1
            class="
              sm:text-4xl
              text-5xl
              font-medium
              title-font
              text-center
              mb-2
              mt-4
              text-primary
            "
          >
            Listings
          </h1>
          <div class="h-1 w-36 bg-primary rounded m-auto mb-2"></div>
        </div>
      </div>
      <div class="flex flex-col mb-4 text-center">
        <a
          class="bg-primary rounded-lg p-2 m-2 cursor-pointer"
          href="/admin/pending-listings"
        >
          <p class="leading-relaxed text-gray-100 font-bold">
            Pending Listings
          </p>
        </a>
        <a
          class="bg-primary rounded-lg p-2 m-2 cursor-pointer"
          href="/admin/live-listings"
        >
          <p class="leading-relaxed text-gray-100 font-bold">Live Listings</p>
        </a>
        <a
          class="bg-primary rounded-lg p-2 m-2 cursor-pointer"
          href="/admin/rejected-listings"
        >
          <p class="leading-relaxed text-gray-100 font-bold">
            Rejected Listings
          </p>
        </a>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "AdminStats",
};
</script>
