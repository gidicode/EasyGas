<template>
  <div>
    <header class="container-lg bg-[#7000FF] mx-auto px-8">
      <nav class="flex justify-between pt-3 pb-3">
        <div class="">
          <RouterLink to="/" class="font-bold text-white text-[30px]"> EasyGas </RouterLink>
        </div>
        
        <div class="text-white space-x-0.5 mt-4" @click="openMenu">
          <font-awesome-icon icon="fa-solid fa-ellipsis-vertical" />
          <font-awesome-icon icon="fa-solid fa-ellipsis-vertical"/>
          <font-awesome-icon icon="fa-solid fa-ellipsis-vertical"/>
        </div>
      </nav>
    </header>
    <body>
      <RouterView/>
    </body>    
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useGasStore } from '../src/store'

const store = useGasStore()
const openMenu = () => store.changeMenu(true)
</script>
