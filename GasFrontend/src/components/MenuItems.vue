<!-- eslint-disable prettier/prettier -->
<template>
    <div class="bg-neutral-900/75 relative top-0 h-screen w-screen" @click.self="closeMenu">
        <nav class="absolute right-0 bg-white w-56 h-auto ">      
            <ul class=" px-4 list-none text-[#7000FF] text-[16px] font-semibold w-50">
                <li class=" mb-8 text-[#DFC7FF] mt-4 relative left-0"> 
                    <font-awesome-icon @click="closeMenu" class="absolute bottom-2 right-5" icon="fa-solid fa-circle-xmark" />
                </li>
                <li class="mb-3 mt-5"> 
                    <span class="mr-1"><font-awesome-icon icon="fa-solid fa-house" /> </span> 
                    Home
                </li>            
                <li class="mb-3"> 
                    <span class="mr-1"> <font-awesome-icon icon="fa-solid fa-circle-info" /></span> 
                    About
                </li>            
                <li class="mb-3"> 
                    <span class="mr-1"> <font-awesome-icon icon="fa-solid fa-magnifying-glass-location" /></span> 
                    Find
                </li>            
                <li class="mb-3"> 
                    <span class="mr-1"> <font-awesome-icon icon="fa-solid fa-user-plus" /></span> 
                    SignUp
                </li>
                <li class="mb-3"> 
                    <span class="mr-1"> <font-awesome-icon icon="fa-solid fa-user-plus" /></span> 
                    SignIn
                </li>
                <li class="mb-3"> 
                    <span class="mr-1"> <font-awesome-icon icon="fa-solid fa-user-plus" /></span> 
                    Log Out
                </li>
            </ul>        
        </nav>   
    </div>
</template>

<script setup> 
import { useGasStore } from '../store'

const store = useGasStore()
const closeMenu = () => store.changeMenu(false)
</script>