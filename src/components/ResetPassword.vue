<template>
  <div class="bg-gray-300 flex h-screen justify-center items-center">
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
              @input="onUsernameChange($event.target.value)"
            />
          </div>
          <div class="my-5 text-sm">
            <label for="password" class="block text-black">Password</label>
            <input
              type="password"
              id="password"
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
              @input="onPassword1Change($event.target.value)"
            />
          </div>
          <div class="my-5 text-sm">
            <label for="password" class="block text-black">Re-Enter Password</label>
            <input
              type="password"
              id="password"
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
              @input="onPassword2Change($event.target.value)"
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
            v-on:click="submitForm"
          >
            Reset Password
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ResetPassword",
  data() {
    return {
      form: {
        username: "",
        password1: "",
        password2: "",
      },
    };
  },
  methods: {
    onUsernameChange(value) {
      this.username = value;
    },

    onPassword1Change(value) {
      this.password1 = value;
    },

    onPassword2Change(value) {
      this.password2 = value;
    },

    async submitForm(e) {
      e.preventDefault();
      const username = this.username;
      const password1 = this.password1;
      const password2 = this.password2;
      const toSend = { username, password1, password2 };
      await fetch(`${process.env.SERVER_URL}/reset-password-submit`, {
        method: "PUT",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(toSend),
      }).then((res) => {
        if (res.status === 200) {
          // Become redirects / modals
          window.location.href = "/login";
        } else {
          alert("Failed");
        }
      });
    },
  },
};
</script>
