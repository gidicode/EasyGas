<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
    <main >
        <section class=" bg-[#7000FF] h-screen grid grid-cols-1 place-items-center">            
            <div class="grid place-items-center">
                <div class="mb-5">
                    <LocationCircle/>   
                </div>
                                                                   
                <p class="text-center text-white text-[16px] mb-5">
                    Locate gas vendors that refill at your door step, Enjoy the easy life!
                </p>                
                    
                <p class="text-center text-white text-xl mb-5 font-semibold">
                    Get Started
                </p> 
                <div v-if="isLogedInChk">
                    <RouterLink to="/dashboard/summary">
                        <button   class="rounded-xl px-8 w-[216px] h-[56px] 
                        border-solid border-2 broder-white text-white text-[20px] font-semibold">                    
                            Dashboard
                        </button>    
                    </RouterLink>
                </div>
                <div v-else > 
                    <RouterLink to="/login">
                        <button @click="changeSignIn" class="rounded-xl w-[216px] h-[56px] 
                        border-solid border-2 broder-white mb-5 text-white text-[20px] font-semibold">                    
                            SignIn
                        </button>  
                    </RouterLink>
                </div>

                <router-link to="/signUp"> 
                    <section v-if="!isLogedInChk" @click="accountType('USER')" class="text-center text-white mb-5">
                        <p class="text-[11px] italic">Don't have an account yet?</p>
                        <h6 class="underline text-[14px] font-bold">SignUp</h6>
                    </section> 
                </router-link>

                <router-link to="/signUp">                
                    <section v-if="!isLogedInChk" @click="accountType('VENDOR')" class="text-white text-center">
                        <h6 class="text-[16px] font-bold">Gas Vendor?</h6>
                        <p class="underline text-[14px]">SignUp</p>
                    </section>
                </router-link>
            </div>                                                                               
        </section>                                                  
    </main>
     
</template>

<script setup> 
import { computed } from 'vue'
import LocationCircle from '../components/LocationCircle.vue'
import { useGasStore } from '../store'
import { useAuthUserStore } from '../store/auth.module'
import { RouterLink } from 'vue-router'


const store = useGasStore()
const authStore = useAuthUserStore()
const isLogedInChk = computed(() => authStore.state.status.loggedIn)
const changeSignIn = () => store.changeSignin()

const accountType = (value) => store.accountType = value
</script>