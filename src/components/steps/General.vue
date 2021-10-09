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
            for="grid-company-name"
          >
            Company Name
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
            placeholder="Amazon"
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
            for="grid-address"
          >
            Company HQ Address
          </label>
          <!-- Make this autocomplete properly -->
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
            "
            required
            id="grid-address"
            type="text"
            placeholder="123 Apple St."
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
            for="grid-city"
          >
            City
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
            "
            required=""
            id="grid-city"
            type="text"
            placeholder="Seattle"
          />
        </div>
      </div>
      <div class="-mx-3 md:flex mb-2">
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
            for="grid-state"
          >
            State
          </label>
          <div class="relative">
            <select
              class="
                block
                appearance-none
                w-full
                bg-grey-lighter
                border border-grey-lighter
                text-grey-darker
                py-3
                px-4
                pr-8
                rounded
              "
              required=""
              id="grid-state"
            >
              <option disable hidden value="">Select State</option>
              <option v-for="state in states" :key="state.abbreviation">
                {{ state.name }}
              </option>
            </select>
          </div>
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
              mt-6
            "
            for="grid-zip"
          >
            Zip
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
              mb-6
            "
            required=""
            id="grid-zip"
            type="text"
            placeholder="12345"
          />
        </div>
      </div>
    </div>
  </form>
</template>

<script>
// TODO: Change input outline colors
export default {
  name: "General",
  data() {
    return {
      states: [
        {
          name: "Alabama",
          abbreviation: "AL",
        },
        {
          name: "Alaska",
          abbreviation: "AK",
        },
        {
          name: "American Samoa",
          abbreviation: "AS",
        },
        {
          name: "Arizona",
          abbreviation: "AZ",
        },
        {
          name: "Arkansas",
          abbreviation: "AR",
        },
        {
          name: "California",
          abbreviation: "CA",
        },
        {
          name: "Colorado",
          abbreviation: "CO",
        },
        {
          name: "Connecticut",
          abbreviation: "CT",
        },
        {
          name: "Delaware",
          abbreviation: "DE",
        },
        {
          name: "District Of Columbia",
          abbreviation: "DC",
        },
        {
          name: "Federated States Of Micronesia",
          abbreviation: "FM",
        },
        {
          name: "Florida",
          abbreviation: "FL",
        },
        {
          name: "Georgia",
          abbreviation: "GA",
        },
        {
          name: "Guam",
          abbreviation: "GU",
        },
        {
          name: "Hawaii",
          abbreviation: "HI",
        },
        {
          name: "Idaho",
          abbreviation: "ID",
        },
        {
          name: "Illinois",
          abbreviation: "IL",
        },
        {
          name: "Indiana",
          abbreviation: "IN",
        },
        {
          name: "Iowa",
          abbreviation: "IA",
        },
        {
          name: "Kansas",
          abbreviation: "KS",
        },
        {
          name: "Kentucky",
          abbreviation: "KY",
        },
        {
          name: "Louisiana",
          abbreviation: "LA",
        },
        {
          name: "Maine",
          abbreviation: "ME",
        },
        {
          name: "Marshall Islands",
          abbreviation: "MH",
        },
        {
          name: "Maryland",
          abbreviation: "MD",
        },
        {
          name: "Massachusetts",
          abbreviation: "MA",
        },
        {
          name: "Michigan",
          abbreviation: "MI",
        },
        {
          name: "Minnesota",
          abbreviation: "MN",
        },
        {
          name: "Mississippi",
          abbreviation: "MS",
        },
        {
          name: "Missouri",
          abbreviation: "MO",
        },
        {
          name: "Montana",
          abbreviation: "MT",
        },
        {
          name: "Nebraska",
          abbreviation: "NE",
        },
        {
          name: "Nevada",
          abbreviation: "NV",
        },
        {
          name: "New Hampshire",
          abbreviation: "NH",
        },
        {
          name: "New Jersey",
          abbreviation: "NJ",
        },
        {
          name: "New Mexico",
          abbreviation: "NM",
        },
        {
          name: "New York",
          abbreviation: "NY",
        },
        {
          name: "North Carolina",
          abbreviation: "NC",
        },
        {
          name: "North Dakota",
          abbreviation: "ND",
        },
        {
          name: "Northern Mariana Islands",
          abbreviation: "MP",
        },
        {
          name: "Ohio",
          abbreviation: "OH",
        },
        {
          name: "Oklahoma",
          abbreviation: "OK",
        },
        {
          name: "Oregon",
          abbreviation: "OR",
        },
        {
          name: "Palau",
          abbreviation: "PW",
        },
        {
          name: "Pennsylvania",
          abbreviation: "PA",
        },
        {
          name: "Puerto Rico",
          abbreviation: "PR",
        },
        {
          name: "Rhode Island",
          abbreviation: "RI",
        },
        {
          name: "South Carolina",
          abbreviation: "SC",
        },
        {
          name: "South Dakota",
          abbreviation: "SD",
        },
        {
          name: "Tennessee",
          abbreviation: "TN",
        },
        {
          name: "Texas",
          abbreviation: "TX",
        },
        {
          name: "Utah",
          abbreviation: "UT",
        },
        {
          name: "Vermont",
          abbreviation: "VT",
        },
        {
          name: "Virgin Islands",
          abbreviation: "VI",
        },
        {
          name: "Virginia",
          abbreviation: "VA",
        },
        {
          name: "Washington",
          abbreviation: "WA",
        },
        {
          name: "West Virginia",
          abbreviation: "WV",
        },
        {
          name: "Wisconsin",
          abbreviation: "WI",
        },
        {
          name: "Wyoming",
          abbreviation: "WY",
        },
      ],
    };
  },
};
</script>

<style >
select:invalid {
  color: rgba(156, 163, 175, 1);
}
</style>
