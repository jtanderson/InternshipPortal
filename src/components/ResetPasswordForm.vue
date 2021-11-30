<template>
  <div class="bg-gray-100 flex h-screen justify-center items-center">
    <div
      class="
        bg-white
        lg:w-4/12
        md:6/12
        w-10/12
        m-auto
        my-10
        shadow-md
        rounded-xl
      "
    >
      <div class="py-8 px-8 rounded-xl">
        <h1 class="font-extrabold text-3xl mt-3 text-center font-sans">
          Reset Password
        </h1>
        <form action="" class="mt-6">
          <div class="my-5 text-sm">
            <label for="username" class="block text-black">Username</label>
            <input
              type="text"
              autofocus
              id="username"
              class="
                rounded-lg
                px-4
                py-3
                mt-3
                focus:outline-none
                bg-gray-100
                w-full
              "
              placeholder="Username"
              v-model="username"
            />
          </div>
          <div class="my-5 text-sm">
            <label for="email" class="block text-black">Email</label>
            <input
              type="email"
              id="email"
              class="
                px-4
                py-3
                mt-3
                focus:outline-none
                bg-gray-100
                w-full
                rounded-lg
              "
              placeholder="joemamma@gmail.com"
              v-model="email"
            />
          </div>

          <button
            class="
              block
              text-center text-white
              bg-primary
              p-3
              duration-300
              hover:bg-red-700
              w-full
              rounded-lg
              mb-3
            "
            type="button"
            @click="submitForm"
          >
            Send Reset Token
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  name: "ResetPasswordForm",
  setup() {
    const username = ref("");
    const email = ref("");
    async function submitForm() {
      const toSend = {
        username: username.value,
        email: email.value,
      };
      await fetch(`${process.env.SERVER_URL}/reset-password-email`, {
        method: "POST",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(toSend),
      }).then((res) => {
        if (res.status === 200) {
          alert("Email!");
          window.location.href = "/ResetPassword";
        } else {
          alert("Failed");
        }
      });
    }
    return {
      username,
      email,
      submitForm,
    };
  },
};
</script>
