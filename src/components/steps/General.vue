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
              border border-red
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
            Address
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
            for="grid-password"
          >
            Password
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
            id="grid-password"
            type="password"
            placeholder="******************"
          />
        </div>
      </div>
      <div class="-mx-3 md:flex mb-2">
        <div class="md:w-1/2 px-3 mb-6 md:mb-0">
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
            placeholder="Albuquerque"
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
              <option>New Mexico</option>
              <option>Missouri</option>
              <option>Texas</option>
            </select>
            <div
              class="
                pointer-events-none
                absolute
                pin-y pin-r
                flex
                items-center
                px-2
                text-grey-darker
              "
            >
              <svg
                class="h-4 w-4"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z"
                />
              </svg>
            </div>
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
            placeholder="90210"
          />
        </div>
      </div>
    </div>
    <div class="flex justify-center align-center">
      <button class="text-center">
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
  </form>
</template>

<script>
export default {
  name: "General",
};
</script>
