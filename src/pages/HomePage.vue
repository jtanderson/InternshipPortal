<template>
  <section class="text-gray-600 body-font">
    <div
      class="
        container
        mx-auto
        flex
        px-5
        py-24
        items-center
        justify-center
        flex-col
      "
    >
      <img
        alt="SU Logo"
        src="../img/sulogo.jpeg"
        style="height: 200px; width: 600px; margin-bottom: 50px"
      />
      <div class="text-center lg:w-2/3 w-full">
        <h1
          class="
            title-font
            sm:text-4xl
            text-3xl
            mb-4
            font-medium
            text-gray-900
            font-sans
          "
        >
          Internship Web Portal
        </h1>
        <p class="leading-relaxed font-sans" style="margin-bottom: 25px">
          Wow, this is a really cool website. I bet the front-end designers of
          this website are super cool. Back-end developers are a little cool but
          not as cool as the people who created this awesome, innovative,
          perfect, masterpiece of a UI design and functionality is brilliant.
        </p>
        <div class="flex justify-center">
          <button
            class="
              red-button
              inline-flex
              text-white
              border-0
              py-2
              px-4
              focus:outline-none
              rounded
              text-lg
              bg-primary
            "
          >
            <a href="/login">Admin Login</a>
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "HomePage",
};
</script>
