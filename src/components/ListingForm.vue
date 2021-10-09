<template>
  <div>
    <div class="p-5 mb-24">
      <div class="mx-4 p-4">
        <div class="flex items-center">
          <div class="flex items-center text-white relative">
            <div
              class="
                rounded-full
                transition
                duration-500
                ease-in-out
                h-12
                w-12
                py-3
                border-2 border-red-600
                bg-red-600
              "
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="100%"
                height="100%"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-bookmark"
              >
                <path
                  d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"
                ></path>
              </svg>
            </div>
            <div
              class="
                absolute
                top-0
                -ml-10
                text-center
                mt-16
                w-32
                text-xs
                font-medium
                uppercase
                text-red-600
              "
            >
              General
            </div>
          </div>
          <div
            class="
              flex-auto
              border-t-2
              transition
              duration-500
              ease-in-out
              border-gray-300
            "
          ></div>
          <div class="flex items-center text-gray-500 relative">
            <div
              class="
                rounded-full
                transition
                duration-500
                ease-in-out
                h-12
                w-12
                py-3
                border-2 border-gray-300
              "
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="100%"
                height="100%"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-list"
              >
                <line x1="8" y1="6" x2="21" y2="6"></line>
                <line x1="8" y1="12" x2="21" y2="12"></line>
                <line x1="8" y1="18" x2="21" y2="18"></line>
                <line x1="3" y1="6" x2="3.01" y2="6"></line>
                <line x1="3" y1="12" x2="3.01" y2="12"></line>
                <line x1="3" y1="18" x2="3.01" y2="18"></line>
              </svg>
            </div>
            <div
              class="
                absolute
                top-0
                -ml-10
                text-center
                mt-16
                w-32
                text-xs
                font-medium
                uppercase
                text-gray-500
              "
            >
              Specifications
            </div>
          </div>
          <div
            class="
              flex-auto
              border-t-2
              transition
              duration-500
              ease-in-out
              border-gray-300
            "
          ></div>
          <div class="flex items-center text-gray-500 relative">
            <div
              class="
                rounded-full
                transition
                duration-500
                ease-in-out
                h-12
                w-12
                py-3
                border-2 border-gray-300
              "
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="100%"
                height="100%"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-globe"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path
                  d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"
                ></path>
              </svg>
            </div>
            <div
              class="
                absolute
                top-0
                -ml-10
                text-center
                mt-16
                w-32
                text-xs
                font-medium
                uppercase
                text-gray-500
              "
            >
              Review
            </div>
          </div>
          <div
            class="
              flex-auto
              border-t-2
              transition
              duration-500
              ease-in-out
              border-gray-300
            "
          ></div>
          <div class="flex items-center text-gray-500 relative">
            <div
              class="
                rounded-full
                transition
                duration-500
                ease-in-out
                h-12
                w-12
                py-3
                border-2 border-gray-300
              "
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="100%"
                height="100%"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="feather feather-database"
              >
                <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
                <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
                <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
              </svg>
            </div>
            <div
              class="
                absolute
                top-0
                -ml-10
                text-center
                mt-16
                w-32
                text-xs
                font-medium
                uppercase
                text-gray-500
              "
            >
              Confirm
            </div>
          </div>
        </div>
      </div>
    </div>
    <General :class="isGeneralHidden ? 'hidden' : ''" />
    <Specifications :class="isSpecificationsHidden ? 'hidden' : ''" />
    <Review :class="isReviewHidden ? 'hidden' : ''" />
    <Confirm :class="isConfirmHidden ? 'hidden' : ''" />
    <div class="flex justify-center align-center mt-4 mb-4">
      <div
        class="flex justify-center align-center mt-4 mb-4"
        v-if="stepIndex > 0"
      >
        <button class="text-center" v-on:click="previousSection">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="36"
            height="36"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="feather feather-arrow-left"
          >
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
          </svg>
        </button>
      </div>
      <div
        class="flex justify-center align-center mt-4 mb-4"
        v-if="stepIndex < 3"
      >
        <button class="text-center" v-on:click="nextSection">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="36"
            height="36"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="feather feather-arrow-right"
          >
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import General from "./steps/General.vue";
import Specifications from "./steps/Specifications.vue";
import Review from "./steps/Review.vue";
import Confirm from "./steps/Confirm.vue";
export default {
  name: "ListingForm",
  components: {
    General,
    Specifications,
    Review,
    Confirm,
  },
  data() {
    return {
      isGeneralHidden: false,
      isSpecificationsHidden: true,
      isReviewHidden: true,
      isConfirmHidden: true,
      stepIndex: 0,
    };
  },
  methods: {
    // TODO: Refactor this code
    nextSection() {
      // If General to Specifications
      if (
        this.isGeneralHidden == false &&
        this.isSpecificationsHidden == true
      ) {
        this.isGeneralHidden = true;
        this.isSpecificationsHidden = false;
        this.stepIndex = 1;
      }
      // If Specifications to Review
      else if (
        this.isSpecificationsHidden == false &&
        this.isReviewHidden == true
      ) {
        this.isSpecificationsHidden = true;
        this.isReviewHidden = false;
        this.stepIndex = 2;
      }
      // If Review to Confirm
      else if (this.isReviewHidden == false && this.isConfirmHidden == true) {
        this.isReviewHidden = true;
        this.isConfirmHidden = false;
        this.stepIndex = 3;
      }
    },

    previousSection() {
      // If Specifications to General
      if (
        this.isGeneralHidden == true &&
        this.isSpecificationsHidden == false
      ) {
        this.isGeneralHidden = false;
        this.isSpecificationsHidden = true;
        this.stepIndex = 0;
      }
      // If Review to Specifications
      else if (
        this.isSpecificationsHidden == true &&
        this.isReviewHidden == false
      ) {
        this.isSpecificationsHidden = false;
        this.isReviewHidden = true;
        this.stepIndex = 1;
      }
      // If Confirm to Review
      else if (this.isReviewHidden == true && this.isConfirmHidden == false) {
        this.isReviewHidden = false;
        this.isConfirmHidden = true;
        this.stepIndex = 2;
      }
    },
  },
};
</script>
