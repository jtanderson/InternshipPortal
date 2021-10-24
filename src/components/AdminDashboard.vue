<template>
  <section class="text-gray-600 body-font">
    <div class="container px-5 py-24 mx-auto">
      <div class="flex flex-wrap -m-5">
        <div class="container px-5 py-24 mx-auto">
          <div class="absolute top-20 right-20">
            <div class="p-4 lg:w-1/10">
              <div
                class="
                  h-full
                  bg-yellow-100 bg-opacity-100
                  p-20
                  rounded-lg
                  overflow-hidden
                  text-center
                  relative
                "
              >
                <h1
                  class="
                    title-font
                    sm:text-2xl
                    text-xl
                    font-bold
                    text-red-700
                    mb-3
                  "
                >
                  Business Requests
                </h1>
                <br />
                <div class="flex flex-wrap -m-4">
                  <div class="p-4 lg:w-1/10">
                    <button
                      class="
                        bg-red-500
                        hover:bg-red-600
                        text-white
                        sm:text-xl
                        text-xl
                        font-bold
                        shadow-lg
                        px-8
                        pt-16
                        pb-24
                        rounded-lg
                      "
                    >
                      Pending
                    </button>
                  </div>
                  <div class="p-4 lg:w-1/8">
                    <button
                      class="
                        bg-red-500
                        hover:bg-red-600
                        text-white
                        sm:text-xl
                        text-xl
                        font-bold
                        shadow-lg
                        px-8
                        pt-16
                        pb-24
                        rounded-lg
                      "
                    >
                      Accepted
                    </button>
                  </div>
                  <div class="p-4 lg:w-1/8">
                    <button
                      class="
                        bg-red-500
                        hover:bg-red-600
                        text-white
                        sm:text-xl
                        text-xl
                        font-bold
                        shadow-lg
                        px-8
                        pt-16
                        pb-24
                        rounded-lg
                      "
                    >
                      Denied
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!--student info-->

        <div class="container px-8 py-20 mx-auto">
          <div class="absolute top-20 left-20">
            <div class="p-4 lg:w-1/8">
              <div
                class="
                  h-full
                  bg-yellow-100 bg-opacity-100
                  px-20
                  py-10
                  rounded-lg
                  overflow-hidden
                  text-center
                  align-text-top
                  relative
                "
              >
                <h1
                  class="
                    title-font
                    sm:text-2xl
                    text-xl
                    font-bold
                    text-red-700
                    mb-3
                  "
                >
                  Student Information
                </h1>
                <br />
                <div class="flex flex-wrap -m-4">
                  <div
                    class="
                      h-full
                      space-x-4
                      bg-yellow-200 bg-opacity-100
                      p-5
                      rounded-lg
                      overflow-hidden
                      text-center
                      relative
                    "
                  >
                    <h1
                      class="
                        title-font
                        sm:text-lg
                        text-lg
                        font-bold
                        text-red-700
                        mb-3
                      "
                    >
                      Weekly-Check in
                    </h1>
                    <div class="p-4 lg:w-1/8">
                      <button
                        class="
                          bg-red-500
                          hover:bg-red-600
                          text-white
                          sm:text-xl
                          text-xl
                          font-bold
                          shadow-lg
                          px-8
                          pt-16
                          pb-20
                          rounded-lg
                        "
                      >
                        Pending
                      </button>
                    </div>
                    <div class="p-4 lg:w-1/8">
                      <button
                        class="
                          bg-red-500
                          hover:bg-red-600
                          text-white
                          sm:text-xl
                          text-xl
                          font-bold
                          shadow-lg
                          px-8
                          pt-16
                          pb-20
                          rounded-lg
                        "
                      >
                        Reviewed
                      </button>
                    </div>
                  </div>
                  <div
                    class="
                      h-full
                      space-x-4
                      bg-yellow-200 bg-opacity-100
                      p-5
                      rounded-lg
                      overflow-hidden
                      text-center
                      relative
                    "
                  >
                    <h1
                      class="
                        title-font
                        sm:text-lg
                        text-lg
                        font-bold
                        text-red-700
                        mb-3
                      "
                    >
                      Internships
                    </h1>
                    <div class="p-4 lg:w-1/8">
                      <button
                        class="
                          bg-red-500
                          hover:bg-red-600
                          text-white
                          sm:text-xl
                          text-xl
                          font-bold
                          shadow-lg
                          px-8
                          pt-16
                          pb-20
                          rounded-lg
                        "
                      >
                        Pending
                      </button>
                    </div>
                    <div class="p-4 lg:w-1/8">
                      <button
                        class="
                          bg-red-500
                          hover:bg-red-600
                          text-white
                          sm:text-xl
                          text-xl
                          font-bold
                          shadow-lg
                          px-8
                          pt-16
                          pb-20
                          rounded-lg
                        "
                      >
                        Reviewed
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import AdminStats from "./AdminStats.vue";
import AdminCard from "./AdminCard.vue";
export default {
  name: "AdminDashboard",
  components: {
    AdminStats,
    AdminCard,
  },
};
</script>
