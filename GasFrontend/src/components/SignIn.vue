<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
    <main class="bg-neutral-900/75 relative  top-0 h-screen w-screen" >    
        <section class="grid grid-cols-1 place-items-center">            
            <div class="relative top-36" @click="closeSignIn">
                <font-awesome-icon class="text-white text-3xl" icon="fa-solid fa-circle-xmark" />
            </div>            
            <div class="bg-white rounded-xl w-80 p-4 mt-60">
                <form @submit="logInUser"  class="grid grid-cols-1 place-items-center">
                    <div class="mt-4 ">                        
                        <label for="email" class="text-[#8157B6] text-sm font-medium w-64"> Email </label>                        
                        <br>
                        <input type='email' v-model="email" id="email" required name="Email" class="w-64 border-b-2 border-[#9062CB]">
                    </div>                    
                    <div class=" mt-4 ">
                        <label for="password" class="text-[#8157B6] text-sm font-medium w-64"> Password</label>                        
                        <br>
                        <input 
                            type="password" id="password" 
                            name="Password" v-model="password"
                            class="w-64 border-b-2 border-[#9062CB] focus:outline-none e focus:ring focus:border-blue-500">
                    </div>                                        

                    <div class="mt-10">                        
                        <button 
                            class="rounded-xl mb-8 bg-[#8157B6] 
                                p-2 w-36
                                text-white text-base 
                                font-medium">
                                Login
                        </button>                        
                    </div>                    

                    <aside v-if="showError">
                        <p class="text-red">Error Occured</p>
                    </aside>
                </form>
            </div>            
        </section>
    </main>
</template>

<script setup>
import { useGasStore } from '../store'
import { useAuthUserStore } from '../store/auth.module'
import { useRouter } from 'vue-router'
import { ref, computed, onMounted } from 'vue'

const store = useGasStore()
const authStore = useAuthUserStore()
const router = useRouter()

onMounted(() => {
    if (loggedInStatus.value) {
        router.push('/dashboard/summary')
    }
})

const loggedInStatus = computed(()=> authStore.state.status.loggedIn)
const closeSignIn = () => store.changeSignin()
const showError = ref(false)
const email = ref('')
const password = ref('')

const logInUser = () => {
    console.log(email.value, 'email')
    authStore.login({email:email.value, password: password.value}).then(
        () => {
            router.push('/dashboard/summary')
        },
        (error) => {
            console.log(error)}
    )
}


</script>