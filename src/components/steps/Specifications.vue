<!-- DO NOT FORMAT THIS FILE AS THE PLACEHOLDERS WILL NOT BE PROPERLY DISPLAYED IF THEY ARE NOT EXACTLY LIKE THEY ARE NOW -->
<template>
  <form>
    <div
      class="
        shadow-xl
        border-2
        rounded
        px-8
        pt-6
        pb-8
        mb-4
        flex flex-col
        my-2
        m-auto
        w-3/4
      "
    >
      <div class="-mx-3 md:flex mb-6">
        <div class="md:w-1/2 px-3 mb-6 md:mb-0">
          <label
            class="
              block
              uppercase
              tracking-wide
              text-grey-darker text-xs
              font-bold
              mb-2
              mt-6
            "
            for="grid-internship-position-title"
          >
            Position Title
          </label>
          <input
            class="
              appearance-none
              block
              w-full
              bg-grey-lighter
              text-grey-darker
              border border-grey-lighter
              rounded
              py-3
              px-4
              mb-3
            "
            required=""
            id="grid-company-name"
            type="text"
            placeholder="Software Developer Intern"
            v-model="positionTitle"
            v-on:change="titleChange"
          />
        </div>
        <div class="md:w-1/2 px-3">
          <label
            class="
              block
              uppercase
              tracking-wide
              text-grey-darker text-xs
              font-bold
              mb-2
            "
            for="grid-minimum-qualifications"
          >
            Minimum Qualifications
          </label>
          <textarea
            class="
              appearance-none
              block
              w-full
              bg-grey-lighter
              text-grey-darker
              border border-grey-lighter
              rounded
              py-3
              px-4
              resize-none
            "
            rows="6"
            required
            id="grid-minimum-qualifications"
            type="text"
            placeholder="- Bachelor's student majoring in Computer Science or a related field
- Programming experience in C, C++, Java, JavaScript or Python
            "
            v-model="minQualifications"
            v-on:change="minQualChange"
          />
        </div>
      </div>
      <div class="-mx-3 md:flex mb-6">
        <div class="md:w-full px-3">
          <label
            class="
              block
              uppercase
              tracking-wide
              text-grey-darker text-xs
              font-bold
              mb-2
            "
            for="grid-preferred-qualifications"
          >
            Preferred Qualifications
          </label>
          <textarea
            class="
              appearance-none
              block
              w-full
              bg-grey-lighter
              text-grey-darker
              border border-grey-lighter
              rounded
              py-3
              px-4
              resize-none
            "
            rows="6"
            required=""
            id="grid-preferred-qualifications"
            type="text"
            placeholder="- Advanced degree in Computer Science, Computer Engineering, Electrical Engineering or related field
- Proficient in a scripting language, C/C++ programming and software design skills
            "
            v-model="prefQualifications"
            v-on:change="prefQualChange"
          />
        </div>
      </div>
      <div class="-mx-3 md:flex mb-2">
        <div class="md:w-full px-3">
          <label
            class="
              block
              uppercase
              tracking-wide
              text-grey-darker text-xs
              font-bold
              mb-2
            "
            for="grid-position-responsibilities"
          >
            Position Responsibilities
          </label>
          <textarea
            class="
              appearance-none
              block
              w-full
              bg-grey-lighter
              text-grey-darker
              border border-grey-lighter
              rounded
              py-3
              px-4
              resize-none
            "
            rows="6"
            required=""
            id="grid-position-responsibilities"
            type="text"
            placeholder="- Fulfill tasks set out by supervisors from several departments
- Attend meetings and take minutes
- Perform research at a supervisor's request
            "
            v-model="positionResponsibilities"
            v-on:change="posResChange"
          />
        </div>
        <div class="md:w-full px-3">
          <label
            class="
              block
              uppercase
              tracking-wide
              text-grey-darker text-xs
              font-bold
              mb-2
              mt-6
            "
            for="grid-additional-information"
          >
            Additional Information
          </label>
          <textarea
            class="
              appearance-none
              block
              w-full
              bg-grey-lighter
              text-grey-darker
              border border-grey-lighter
              rounded
              py-3
              px-4
              mb-6
              resize-none
            "
            rows="4"
            required=""
            id="grid-additional-information"
            type="text"
            placeholder="Any additional information about internship"
            v-model="additionalInfo"
            v-on:change="addInfoChange"
          />
        </div>
      </div>
    </div>
  </form>
</template>

<script>
// TODO: Change input outline colors
export default {
  name: "Specifications",
  props: [
    "titleChanged",
    "minQualChanged",
    "prefQualChanged",
    "posResChanged",
    "addInfoChanged",
  ],
  data() {
    return {
      positionTitle: "",
      minQualifications: "",
      prefQualifications: "",
      positionResponsibilities: "",
      additionalInfo: "",
    };
  },
  methods: {
    titleChange() {
      this.titleChanged(this.positionTitle);
    },
    minQualChange() {
      this.minQualChanged(this.minQualifications);
    },
    prefQualChange() {
      this.prefQualChanged(this.prefQualifications);
    },
    posResChange() {
      this.posResChanged(this.positionResponsibilities);
    },
    addInfoChange() {
      this.addInfoChanged(this.additionalInfo);
    },
  },
};
</script>

<style>
select:invalid {
  color: rgba(156, 163, 175, 1);
}
</style>
