<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
    <main class="bg-neutral-900/75 relative  top-0 h-screen w-screen" >    
        <section class="grid grid-cols-1 place-items-center">            
            <div class="relative top-36" @click="closeSignIn">
                <font-awesome-icon class="text-white text-3xl" icon="fa-solid fa-circle-xmark" />
            </div>            
            <div class="bg-white rounded-xl w-80 p-4 mt-60">
                <form @submit.prevent="logInUser" class="grid grid-cols-1 place-items-center">

                    <p class="text-xs text-rose-400 text-center w-64" v-if="showInvalid">{{ invalidCredentials }}</p>

                    <div class="mt-4 ">                        
                        <label for="email" class="text-[#8157B6] text-sm font-medium w-64"> Email </label>                        
                        <br>
                        <input type='email' v-model="email" id="email" required name="Email" class="w-64 border-b-2 border-[#9062CB]">
                        <p class="text-xs text-rose-500 w-64">{{ errors.email }}</p>
                    </div>                    
                    <div class=" mt-4 ">
                        <label for="password" class="text-[#8157B6] text-sm font-medium w-64"> Password</label>                        
                        <br>
                        <input 
                            type="password" id="password" 
                            name="Password" v-model="password"
                            class="w-64 border-b-2 border-[#9062CB] focus:outline-none e focus:ring focus:border-blue-500">
                        <p class="text-xs text-rose-500 w-64">{{ errors.password }}</p>
                    </div>                    
                    
                    <button 
                        type="submit"                        
                        :disabled="isSubmitting"
                        class="rounded-xl mb-8 bg-[#8157B6] 
                            p-2 w-36
                            text-white text-base 
                            font-medium mt-10">
                            Login
                    </button>

                    <aside v-if="showError">
                        <p class="text-red">Error Occured</p>
                    </aside>
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

const { errors, handleSubmit, isSubmitting } = useForm({
  validationSchema: schema,
});

const { value: email } = useField("email");
const { value: password } = useField("password");

const closeSignIn = () => store.changeSignin();
const showError = ref(false);

const invalidCredentials = ref('')
const showInvalid = ref(false)

const logInUser = handleSubmit(() => {
  authStore.login({ email: email.value, password: password.value }).then(
    () => {
      router.push("/dashboard/summary");
      store.changeSignin();
      store.changeMenu(false);
    },
    (error) => {        
      if (error.response.status == 401) {
        invalidCredentials.value = 'Email or password is incorrect'
        showInvalid.value = true

        //setTimeout(() => showInvalid.value = false, )
      }      
    }
  );
});
</script>
