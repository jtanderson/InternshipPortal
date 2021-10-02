<template>
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-5">
      <div class="flex flex-wrap w-full mb-8">
        <div class="w-full mb-6 lg:mb-0">
          <h1
            class="
              sm:text-4xl
              text-5xl
              font-medium
              title-font
              mb-2
              text-primary
            "
          >
            Statistics
          </h1>
          <div class="h-1 w-20 bg-primary rounded"></div>
        </div>
      </div>
      <div class="flex flex-col -m-4 text-center">
        <div class="p-4 sm:w-1/4 w-1/2">
          <div class="bg-primary rounded-lg p-2 xl:p-4">
            <h2 class="title-font font-medium sm:text-4xl text-3xl text-white">
              10
            </h2>
            <p class="leading-relaxed text-gray-100 font-bold">Live Listings</p>
          </div>
        </div>
        <div class="p-4 sm:w-1/4 w-1/2">
          <div class="bg-primary rounded-lg p-2 xl:p-4">
            <h2 class="title-font font-medium sm:text-4xl text-3xl text-white">
              5
            </h2>
            <p class="leading-relaxed text-gray-100 font-bold">
              Pending Listings
            </p>
          </div>
        </div>
        <div class="p-4 sm:w-1/4 w-1/2">
          <div class="bg-primary rounded-lg p-2 xl:p-4">
            <h2 class="title-font font-medium sm:text-4xl text-3xl text-white">
              2
            </h2>
            <p class="leading-relaxed text-gray-100 font-bold">
              Rejected Listings
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "AdminStats",
};
</script>
