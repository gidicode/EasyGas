<!-- eslint-disable prettier/prettier -->
<template>
    <main class="bg-neutral-900/75 relative top-0 h-screen w-screen">
        <section class="grid grid-cols-1 place-items-center">
            <div class="relative top-24" @click="closeSignUp">
                <font-awesome-icon class="text-white text-3xl" icon="fa-solid fa-circle-xmark" />
            </div>    

            <div class="bg-white rounded-xl w-80 p-4 mt-52">
                <form action="" class="grid grid-cols-1 place-items-center">
                    <h5 class="font-medium mb-5 mt-2 text-[#FF00B5] text-2xl">SIGNUP</h5>
                    <div class="mt-4">                    
                        <input 
                            type="text" id="username" 
                            name="usename" placeholder="Username"
                            class="w-64 h-10 border border-[#5400C0] p-2">
                    </div>

                    <div class="mt-6">                    
                        <input 
                            type="email" id="email" 
                            name="email" placeholder="Email"
                            class="w-64 h-10 border border-[#5400C0] p-2">
                    </div>

                    <div class="mt-6">                                       
                        <input 
                            type="password" id="password" 
                            placeholder="Password" name="password" 
                            class="w-64 h-10 border border-[#5400C0] p-2">
                    </div>

                    <div class="mt-6">                       
                        <input 
                            type="password" id="password2" 
                            name="Password2" placeholder="Confirm Password" 
                            class="w-64 h-10 border border-[#5400C0] p-2">
                    </div>

                    <div class="mt-10">
                        <RouterLink to= "/dashboard/complete-registration">
                            <button 
                                class="rounded-xl mb-8 bg-[#8157B6] 
                                    p-2 w-36 h-10
                                    text-white text-base 
                                    font-medium">
                                    Proceed
                            </button>
                        </RouterLink>
                    </div>  
                </form>
            </div>
        </section>
    </main>
</template>

<script setup>
import { useGasStore } from '../store'
import { RouterLink } from 'vue-router'

const store = useGasStore()
const closeSignUp = () => store.changeSignUp()
</script>

<style scoped>
::placeholder{
    color: #DEC5FD;
    opacity: 1;
}

:-ms-input-placeholder{
    color: #DEC5FD;
}

::-ms-input-placeholder{
    color: #DEC5FD;
}
</style>