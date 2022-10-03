<!-- eslint-disable prettier/prettier -->
<template>
  <main class="">
    <section class="grid grid-cols-1 place-items-center">     
      <div class="bg-white rounded-xl w-auto px-8 shadow-lg mt-20">
        <form
          @submit.prevent="logInUser"
          class="grid grid-cols-1 place-items-center "
        >
          <h5 class="font-medium mb-5 mt-2 text-[#FF00B5] text-2xl">LOGIN</h5>
          <p class="text-xs text-rose-400 text-center w-64" v-if="showInvalid">
            {{ invalidCredentials }}
          </p>

          <div class="mt-4">
            <label for="email" class="text-[#8157B6] text-sm font-medium w-64">
              Email
            </label>
            <br />
            <input
              type="email"
              v-model="email"
              id="email"
              required
              name="Email"
              class="w-64 border-b-2 border-[#9062CB] focus:outline-none"
            />
            <p class="text-xs text-rose-500 w-64">{{ errors.email }}</p>
          </div>
          <div class="mt-4">
            <label
              for="password"
              class="text-[#8157B6] text-sm font-medium w-64"
            >
              Password</label
            >
            <br />
            <input
              type="password"
              id="password"
              name="Password"
              required
              v-model="password"
              class="w-64 border-b-2 border-[#9062CB] focus:outline-none"
            />
            <p class="text-xs text-rose-500 w-64">{{ errors.password }}</p>
          </div>

        <button 
            disabled 
            type="button" 
            v-if="Submitting" 
            class="text-white p-2 w-36 bg-[#8157B6] mt-10 mb-8 hover:bg-[#8157B8] focus:ring-4 focus:ring-blue-300 font-medium rounded-xl text-sm text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 inline-flex items-center">
            <svg role="status" class="inline mr-3 w-4 h-4 text-white animate-spin" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="#E5E7EB"/>
            <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentColor"/>
            </svg>
            Loading...
        </button>

          <button
            v-else
            type="submit"
            class="rounded-xl mb-8 bg-[#8157B6] p-2 w-36 text-white text-base font-medium mt-10">
            Login
          </button>
        </form>
      </div>
    </section>
  </main>
</template>

<script setup>
import { useGasStore } from "../store";
import { useAuthUserStore } from "../store/auth.module";
import { useRouter } from "vue-router";
import { ref, computed, onMounted } from "vue";
import { useForm, useField } from "vee-validate";
import * as yup from "yup";

const store = useGasStore();
const authStore = useAuthUserStore();
const router = useRouter();
const loggedInStatus = computed(() => authStore.state.status.loggedIn);

onMounted(() => {
  if (loggedInStatus.value) {
    router.push("/dashboard/summary");
  }
});

const schema = yup.object({
  email: yup.string().required().email(),
  password: yup.string().required(),
});

const { errors, handleSubmit } = useForm({
  validationSchema: schema,
});

const { value: email } = useField("email");
const { value: password } = useField("password")

//const closeSignIn = () => store.changeSignin()

const invalidCredentials = ref("");
const showInvalid = ref(false);

const Submitting = ref(false);

const logInUser = handleSubmit(() => {
  Submitting.value = true;
  authStore.login({ email: email.value, password: password.value }).then(
    () => {
      Submitting.value = false;
      router.push("/dashboard/summary");
      store.changeSignin();
      store.changeMenu(false);
    },
    (error) => {
      Submitting.value = false;
      if (error.response.status == 401) {
        invalidCredentials.value = "Email or password is incorrect";
        showInvalid.value = true;
        //setTimeout(() => showInvalid.value = false, )
      }
    }
  );
});
</script>

<style scoped>
::placeholder {
  color: #dec5fd;
  opacity: 1;
}

:-ms-input-placeholder {
  color: #dec5fd;
}

::-ms-input-placeholder {
  color: #dec5fd;
}
</style>
