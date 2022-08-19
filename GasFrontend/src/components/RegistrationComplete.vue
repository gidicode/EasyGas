<!-- eslint-disable prettier/prettier -->
<template>
    <main class="grid grid-cols-1 place-items-center">
        <h4 class=" text-[#7000FF] text-xl mt-20">Registration Completed!</h4>
        <p class="text-center text-[#22004D] text-xs mt-4">
            Thanks for completing your registration, 
            you can now start searching for a gas vendor 
            to come refill at your door step.
        </p>
        <div class="mt-10">
            <RouterLink to= "/dashboard/summary">
                <button 
                    class="rounded-xl mb-8 bg-[#8157B6] 
                        p-2 w-36 h-10
                        text-white text-base 
                        font-medium">
                        Proceed
                </button>
            </RouterLink>
        </div>  
    </main>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>