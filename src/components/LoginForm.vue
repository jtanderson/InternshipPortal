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
        <h1 class="font-medium text-3xl mt-3 text-center font-sans">
          Admin Login
        </h1>
        <form action="" class="mt-6">
          <div class="my-5 text-sm">
            <label class="block text-black">Username</label>
            <input
              type="text"
              autofocus
              autocomplete="off"
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
            <label for="password" class="block text-black">Password</label>
            <input
              type="password"
              autocomplete="off"
              class="
                px-4
                py-3
                mt-3
                focus:outline-none
                bg-gray-100
                w-full
                rounded-lg
              "
              placeholder="Password"
              v-model="password"
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
            Login
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  name: "LoginForm",
  setup() {
    const username = ref("");
    const password = ref("");

    async function submitForm(event) {
      event.preventDefault();
      const username = this.username;
      const password = this.password;
      const toSend = { username, password };
      await fetch(`${process.env.SERVER_URL}/login-submit`, {
        method: "POST",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(toSend),
      })
        .then((res) => {
          if (res.status === 200) {
            // Need refactor, better way of routing
            window.location.href = "/admin";
          } else if (res.status === 403) {
            res.json().then((r) => {
              alert(r.err_msg);
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }

    return {
      username,
      password,
      submitForm,
    };
  },
};
</script>
