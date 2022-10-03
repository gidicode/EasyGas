<!-- eslint-disable prettier/prettier -->
<template>
    <main>
        <section class="grid grid-cols-1 place-items-center">             
            <div class="bg-white rounded-xl w-auto px-8 mt-20 shadow-md">
                <form action="" class="grid grid-cols-1 place-items-center">
                    <h5 class="font-medium mb-5 mt-2 text-[#FF00B5] text-2xl">  {{accountType}} SIGNUP </h5>
                    <div class="mt-4">                    
                        <input 
                            v-model="username"
                            type="text" id="username" 
                            name="usename" placeholder="Username"
                            class="w-64 h-10 border border-[#5400C0] p-2 focus:outline-none">
                        <p class="text-xs text-rose-500 w-64"> {{ errors.username}}</p>
                    </div>

                    <div class="mt-6">                    
                        <input 
                            v-model="email"
                            type="email" id="email" 
                            name="email" placeholder="Email"
                            class="w-64 h-10 border border-[#5400C0] p-2 focus:outline-none">
                        <p class="text-xs text-rose-500 w-64"> {{ errors.email}}</p>
                    </div>

                    <div class="mt-6">                                       
                        <input 
                            v-model="password"
                            type="password" id="password" 
                            placeholder="Password" name="password" 
                            class="w-64 h-10 border border-[#5400C0] p-2 focus:outline-none">
                        <p class="text-xs text-rose-500 w-64"> {{errors.password}}</p>
                    </div>

                    <div class="mt-6">                       
                        <input 
                            v-model="password2"
                            type="password" id="password2" 
                            name="Password2" placeholder="Confirm Password" 
                            class="w-64 h-10 border border-[#5400C0] p-2 focus:outline-none">
                        <p class="text-xs text-rose-500 w-64"> {{ errors.password2}}</p>                            
                    </div>

                    <div class="mt-10">
                        <button  
                            v-if="isSubmitting" 
                            type="button" 
                            class="bg-[#8157B6] p-2 w-36 rounded-xl text-white text-base font-medium mt-10 mb-8" disabled>
                            <svg class="animate-spin h-5 w-5 mr-3 ..." viewBox="0 0 24 24">
                                <!-- ... -->
                            </svg>
                            Processing...
                        </button>
                        
                        <button 
                            v-else
                            @click.prevent="selectRegType"
                            class="rounded-xl mb-8 bg-[#8157B6] 
                                p-2 w-36 h-10
                                text-white text-base 
                                font-medium">
                                Proceed
                        </button>                        
                    </div>  
                </form>
            </div>
        </section>
    </main>
</template>

<script setup>
import { useAuthUserStore } from "../store/auth.module";
import { useRouter } from "vue-router";
import { computed, onMounted } from "vue";
import { useForm, useField } from "vee-validate";
import * as yup from "yup";
import { useGasStore } from '../store'

onMounted(() => {
  if (loggedInStatus.value) {
    router.push("/dashboard/summary");
  }
});

const store = useGasStore()
const authStore = useAuthUserStore();;
const router = useRouter();
const loggedInStatus = computed(() => authStore.state.status.loggedIn);
const accountType = computed(()=> store.accountType)

const schema = yup.object({
  username: yup.string().required(),
  email: yup.string().required().email(),
  password: yup.string().required(),
  password2: yup.string().required(),
});

const { errors, handleSubmit, setFieldError, isSubmitting } = useForm({
  validationSchema: schema,
});

const { value: email } = useField("email");
const { value: username } = useField("username");
const { value: password } = useField("password");
const { value: password2 } = useField("password2");

const selectRegType = () => {
  if(accountType.value == "USER") {
    registerUser()
  } else{
    registerVendor()
  }
}

const registerUser = handleSubmit(() => {
  authStore
    .register({
      username: username.value,
      email: email.value,
      password: password.value,
      password2: password2.value,
      vendor: false,
    })
    .then(
      () => {
        router.push("/login");
      },
      (error) => {
        if (error.response.data.email) {
          setFieldError("email", "This email already exist");
        }

        if (error.response.data.username) {
          setFieldError("username", "This username is not available");
        }

        if (error.response.data.password) {
          setFieldError("password", error.response.data.password);
        }
      }
    );
});

const registerVendor = handleSubmit(() => {
  authStore
    .register({
      username: username.value,
      email: email.value,
      password: password.value,
      password2: password2.value,
      vendor: true,
    })
    .then(
      () => {
        router.push("/login");
      },
      (error) => {
        if (error.response.data.email) {
          setFieldError("email", "This email already exist");
        }

        if (error.response.data.username) {
          setFieldError("username", "This username is not available");
        }

        if (error.response.data.password) {
          setFieldError("password", error.response.data.password);
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
