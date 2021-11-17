<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div class="bg-primary">
    <div class="max-w-7xl mx-auto py-3 px-3 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between flex-wrap">
        <div class="w-0 flex-1 flex items-center">
          <span class="flex p-2 rounded-lg bg-primaryOffset">
            <SpeakerphoneIcon class="h-6 w-6 text-white" aria-hidden="true" />
          </span>
          <p class="ml-3 font-medium text-white truncate">
            <span class="md:hidden"> We have new listings posted! </span>
            <span class="hidden md:inline">
              Big news! We're excited to announce new admin recommended
              listings.
            </span>
          </p>
        </div>
        <div
          class="order-3 mt-2 flex-shrink-0 w-full sm:order-2 sm:mt-0 sm:w-auto"
        >
          <a
            href="/browse?filter=admin_recommended"
            class="
              flex
              items-center
              justify-center
              px-4
              py-2
              border border-transparent
              rounded-md
              shadow-sm
              text-sm
              font-medium
              text-primary
              bg-white
              hover:bg-red-50
            "
          >
            <!-- This needs to route to /browse with admin recommended feature on and most recent -->
            See Listings
          </a>
        </div>
        <div class="order-2 flex-shrink-0 sm:order-3 sm:ml-3">
          <button
            type="button"
            class="
              -mr-1
              flex
              p-2
              rounded-md
              hover:bg-primaryOffset
              focus:outline-none focus:ring-2 focus:ring-white
              sm:-mr-2
            "
            @click="closeCallback()"
          >
            <span class="sr-only">Dismiss</span>
            <XIcon class="h-6 w-6 text-white" aria-hidden="true" />
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { SpeakerphoneIcon, XIcon } from "@heroicons/vue/outline";

export default {
  name: "Banner",
  props: { closeCallback: Function },
  components: {
    SpeakerphoneIcon,
    XIcon,
  },
};
</script>