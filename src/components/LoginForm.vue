<template>
  <div class="bg-gray-300 flex h-screen justify-center items-center">
    <div class="bg-white lg:w-4/12 md:6/12 w-10/12 m-auto my-10 shadow-md">
      <div class="py-8 px-8 rounded-xl">
        <h1 class="font-medium text-3xl mt-3 text-center font-sans">
          Admin Login
        </h1>
        <form action="" class="mt-6">
          <div class="my-5 text-sm">
            <label for="username" class="block text-black">Username</label>
            <input
              type="text"
              autofocus
              id="username"
              class="
                rounded-sm
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
                rounded-sm
                px-4
                py-3
                mt-3
                focus:outline-none
                bg-gray-100
                w-full
              "
              placeholder="Password"
              @input="onPasswordChange($event.target.value)"
            />
          </div>

          <button
            class="
              block
              text-center text-white
              bg-primary
              p-3
              duration-300
              rounded-sm
              hover:bg-red-700
              w-full
            "
            v-on:click="submitForm"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    onUsernameChange(value) {
      this.username = value;
    },

    onPasswordChange(value) {
      this.password = value;
    },

    async submitForm(e) {
      e.preventDefault();
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
      }).then((res) => {
        if (res.status === 200) {
          // Become redirects / modals
          window.location.href = "/admin";
        } else {
          alert("Failed");
        }
      });
    },
  },
};
</script>
