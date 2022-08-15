<!-- eslint-disable prettier/prettier -->
<template>
    <main class="container bg-[#7000FF] h-screen grid grid-rows-4 grid-flow-col gap-4 justify-items-center">
        <div class="mt-[3rem]">
            <LocationCircle/>                                
        </div>   
        <div class="mt-[4rem]">
            <p class="text-center text-white text-[16px] px-3">
                Locate gas vendors that refill at your door step, Enjoy the easy life!
            </p>
        </div>  
        <div>
            <p class="text-center text-white text-[16px]">
                Get Started
            </p>
        </div>    
        <div class="mt-0">
            <button class="rounded-full ...">Sign In</button>
        </div>               
    </main>
</template>

<script setup> 
import LocationCircle from '../components/LocationCircle.vue'
</script>