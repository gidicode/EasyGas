<!-- eslint-disable prettier/prettier -->
<template>
    <main class="bg-neutral-900/75 relative  top-0 h-screen w-screen" @click.self="closeSignIn">    
        <section class="grid grid-cols-1 place-items-center">            
            <div class="bg-white rounded-xl w-80 p-4 mt-60">
                <form action=""  class="grid grid-cols-1 place-items-center ">
                    <div class="mt-4 ">                        
                        <label for="email" class="text-[#8157B6] text-sm font-medium w-64"> Email </label>                        
                        <br>
                        <input type='email' id="email" name="Email" class="w-64 border-b-2 border-[#9062CB]">
                    </div>                    
                    <div class=" mt-4 ">
                        <label for="password" class="text-[#8157B6] text-sm font-medium w-64"> Password</label>                        
                        <br>
                        <input 
                            type="password" id="password" 
                            name="Password" 
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
                </form>
            </div>            
        </section>
    </main>
</template>

<script setup>
import { useGasStore } from '../store'

const store = useGasStore()
const closeSignIn = () => store.changeSignin()
</script>