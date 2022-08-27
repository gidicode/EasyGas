<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<!-- eslint-disable prettier/prettier -->
<template>
    <main >
        <section class="container-lg bg-[#7000FF] h-screen grid grid-rows-4 grid-flow-col gap-1 justify-items-center">
            <div class="mt-[4rem]">
                <LocationCircle/>                                
            </div>   
            <div class="mt-[2rem]">
                <p class="text-center text-white text-[16px] px-8">
                    Locate gas vendors that refill at your door step, Enjoy the easy life!
                </p>
                <p class="text-center text-white text-[16px] mt-4 font-semibold">
                    Get Started
                </p>
            </div>         
            <div>                
                <!--<RouterLink to="/login"></RouterLink>-->                
                <div v-if="isLogedInChk">
                    <RouterLink to="/dashboard/summary">
                        <button   class="rounded-xl px-8 w-[216px] h-[56px] 
                        border-solid border-2 broder-white text-white text-[20px] font-semibold">                    
                            Dashboard
                        </button>    
                    </RouterLink>
                </div>

                <div v-else >
                    <button @click="changeSignIn" class="rounded-xl px-8 w-[216px] h-[56px] 
                    border-solid border-2 broder-white text-white text-[20px] font-semibold">                    
                        SignIn
                    </button>  
                </div>
                                                             
                <aside v-if="!isLogedInChk" class="text-center mt-7 text-white" @click="changeSignUp">
                    <p class="text-[11px] italic">Don't have an account yet?</p>
                    <h6 class="underline text-[14px] font-bold">SignUp</h6>
                </aside>            
            </div>               

            <div v-if="!isLogedInChk" class="text-white text-center">
                <h6 class="text-[16px] font-bold">Gas Vendor?</h6>
                <p class="underline text-[14px]">SignUp</p>
            </div>     
        </section>                                    
        <section class="absolute top-0 z-50 h-auto" v-if="showSignIn">            
            <SignIn/> 
        </section>

        <section class="absolute top-0 z-50 h-auto" v-if="showSignUp">            
            <SignUp/> 
        </section>
    </main>
     
</template>

<script setup> 
import { computed } from 'vue'
import LocationCircle from '../components/LocationCircle.vue'
import SignIn from '../components/SignIn.vue'
import SignUp from '../components/SignUp.vue'
import { useGasStore } from '../store/index'
import { useAuthUserStore } from '../store/auth.module'
import { RouterLink } from 'vue-router'
const store = useGasStore()
const authStore = useAuthUserStore()
const isLogedInChk = computed(() => authStore.state.status.loggedIn)
const showSignIn = computed(() => store.showSignIn)
const showSignUp = computed(() => store.showSignUp)
const changeSignIn = () => store.changeSignin()
const changeSignUp = () => store.changeSignUp()
</script>