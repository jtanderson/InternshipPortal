<template>
  <div id="listing-form">
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
            class="flex-auto border-t-2 transition duration-500 ease-in-out"
            :class="generalToSpecifications"
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
                border-2
              "
              :class="generalToSpecifications"
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
              "
              :class="specificationsText"
            >
              Specifications
            </div>
          </div>
          <div
            class="flex-auto border-t-2 transition duration-500 ease-in-out"
            :class="specificationsToReview"
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
                border-2
              "
              :class="specificationsToReview"
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
              "
              :class="reviewText"
            >
              Review
            </div>
          </div>
          <div
            class="flex-auto border-t-2 transition duration-500 ease-in-out"
            :class="reviewToConfirm"
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
                border-2
              "
              :class="reviewToConfirm"
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
              "
              :class="confirmText"
            >
              Confirm
            </div>
          </div>
        </div>
      </div>
    </div>
    <General
      :nameChanged="updateName"
      :addressChanged="updateAddress"
      :cityChanged="updateCity"
      :stateChanged="updateState"
      :zipChanged="updateZip"
      :class="isGeneralHidden ? 'hidden' : ''"
    />
    <Specifications
      :titleChanged="updatePositionTitle"
      :minQualChanged="updateMinQualifications"
      :prefQualChanged="updatePrefQualifications"
      :posResChanged="updatePositionResponsibilities"
      :addInfoChanged="updateAdditionalInfo"
      :class="isSpecificationsHidden ? 'hidden' : ''"
    />
    <Review
      :name="companyName"
      :address="companyAddress"
      :city="companyCity"
      :state="companyState"
      :zip="companyZip"
      :positionTitle="positionTitle"
      :minQual="minQualifications"
      :prefQual="prefQualifications"
      :posResp="positionResponsibilities"
      :addInfo="additionalInfo"
      :class="isReviewHidden ? 'hidden' : ''"
    />
    <Confirm
      :submitListing="submitListing"
      :class="isConfirmHidden ? 'hidden' : ''"
    />
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
      generalToSpecifications: "border-gray-300",
      specificationsText: "text-gray-500",
      specificationsToReview: "border-gray-300",
      reviewText: "text-gray-500",
      reviewToConfirm: "border-gray-300",
      confirmText: "text-gray-500",
      companyName: "",
      companyAddress: "",
      companyCity: "",
      companyState: "",
      companyZip: "",
      positionTitle: "",
      minQualifications: "",
      prefQualifications: "",
      positionResponsibilities: "",
      additionalInfo: "",
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
        this.generalToSpecifications = "border-red-600 bg-red-600 text-white";
        this.specificationsText = "text-red-600";
      }
      // If Specifications to Review
      else if (
        this.isSpecificationsHidden == false &&
        this.isReviewHidden == true
      ) {
        this.isSpecificationsHidden = true;
        this.isReviewHidden = false;
        this.stepIndex = 2;
        this.specificationsToReview = "border-red-600 bg-red-600 text-white";
        this.reviewText = "text-red-600";
      }
      // If Review to Confirm
      else if (this.isReviewHidden == false && this.isConfirmHidden == true) {
        this.isReviewHidden = true;
        this.isConfirmHidden = false;
        this.stepIndex = 3;
        this.reviewToConfirm = "border-red-600 bg-red-600 text-white";
        this.confirmText = "text-red-600";
      }
      this.scrollToTop();
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
        this.generalToSpecifications = "border-gray-300";
        this.specificationsText = "text-gray-500";
      }
      // If Review to Specifications
      else if (
        this.isSpecificationsHidden == true &&
        this.isReviewHidden == false
      ) {
        this.isSpecificationsHidden = false;
        this.isReviewHidden = true;
        this.stepIndex = 1;
        this.specificationsToReview = "border-gray-300";
        this.reviewText = "text-gray-500";
      }
      // If Confirm to Review
      else if (this.isReviewHidden == true && this.isConfirmHidden == false) {
        this.isReviewHidden = false;
        this.isConfirmHidden = true;
        this.stepIndex = 2;
        this.reviewToConfirm = "border-gray-300";
        this.confirmText = "text-gray-500";
      }
      this.scrollToTop();
    },

    scrollToTop() {
      window.scrollTo(0, 0);
    },

    updateName(newName) {
      this.companyName = newName;
      console.log(this.companyName);
    },
    updateAddress(newAddress) {
      this.companyAddress = newAddress;
      console.log(this.companyAddress);
    },
    updateCity(newCity) {
      this.companyCity = newCity;
      console.log(this.companyCity);
    },
    updateState(newState) {
      this.companyState = newState;
      console.log(this.companyState);
    },
    updateZip(newZip) {
      this.companyZip = newZip;
      console.log(this.companyZip);
    },
    updatePositionTitle(newTitle) {
      this.positionTitle = newTitle;
      console.log(this.positionTitle);
    },
    updateMinQualifications(newMinQual) {
      this.minQualifications = newMinQual;
      console.log(this.minQualifications);
    },
    updatePrefQualifications(newPrefQual) {
      this.prefQualifications = newPrefQual;
      console.log(this.prefQualifications);
    },
    updatePositionResponsibilities(newPosResp) {
      this.positionResponsibilities = newPosResp;
      console.log(this.positionResponsibilities);
    },
    updateAdditionalInfo(newAddInfo) {
      this.additionalInfo = newAddInfo;
      console.log(this.additionalInfo);
    },

    submitListing() {
      const body = {
        company_name: this.companyName,
        company_address: this.companyAddress,
        company_city: this.companyCity,
        company_state: this.companyState,
        company_zip: this.companyZip,
        position_title: this.positionTitle,
        pos_responsibility: this.positionResponsibilities,
        min_qualifications: this.minQualifications,
        pref_qualifications: this.prefQualifications,
        additional_info: this.additionalInfo,
      };
      console.log(body);
      console.log(JSON.stringify(body));
      fetch(`${process.env.SERVER_URL}/listing-submit`, {
        method: "POST",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body),
      }).then((res) => {
        if (res.status === 200) {
          // Make modal and then on modal exit, redirect to homepage
          window.location.href = "/";
        } else {
          // Make modal for failure
          alert("Failed");
        }
      });
    },
  },
};
</script>

<style>
#listing-form {
  scroll-behavior: smooth;
}
</style>
