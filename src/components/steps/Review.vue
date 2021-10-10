<template>
  <form>
    <div
      class="
        bg-gray-200
        shadow-md
        border-2
        rounded
        px-8
        pt-6
        pb-8
        mb-4
        flex flex-col
        my-2
        m-auto
        w-1/2
      "
    >
      <div class="text-center mb-12 mt-4">
        <div class="text-3xl">{{ title }}</div>
      </div>
      <div class="text-justify mb-12">
        <div class="text-lg p-2">
          <span class="font-bold"> Company Name: </span>{{ this.name }}
        </div>
        <div class="text-lg p-2">
          <span class="font-bold"> Company Address: </span>{{ this.address }}
        </div>
        <div class="text-lg p-2">
          <span class="font-bold"> Company City: </span>{{ this.city }}
        </div>
        <div class="text-lg p-2">
          <span class="font-bold"> Company State: </span>{{ this.state }}
        </div>
        <div class="text-lg p-2">
          <span class="font-bold"> Company Zip Code: </span>{{ this.zip }}
        </div>
        <div class="text-lg p-2">
          <span class="font-bold"> Position Title: </span
          >{{ this.positionTitle }}
        </div>
        <div class="text-lg p-2">
          <span class="font-bold"> Minimum Qualifications: </span
          >{{ this.minQual }}
        </div>
        <div class="text-lg p-2">
          <span class="font-bold"> Prefered Qualifications: </span
          >{{ this.prefQual }}
        </div>
        <div class="text-lg p-2">
          <span class="font-bold"> Position Responsibilities: </span
          >{{ this.posResp }}
        </div>
        <div class="text-lg p-2">
          <span class="font-bold"> Additional Information: </span
          >{{ this.addInfo }}
        </div>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  name: "Review",
  props: [
    "name",
    "address",
    "city",
    "state",
    "zip",
    "positionTitle",
    "minQual",
    "prefQual",
    "posResp",
    "addInfo",
  ],
  data() {
    return {
      title: "Software Developer Intern",
      company_name: "Amazon",
    };
  },
};
</script>
