<template>
  <div>
    <header class="container-lg bg-[#7000FF] mx-auto px-8">
      <nav class="flex justify-between pt-3 pb-3">
        <div class="font-bold text-white text-[30px]">
          <RouterLink to="/" > EasyGas </RouterLink>
        </div>
        
        <div class="text-white space-x-0.5 mt-4" @click="openMenu">
          <font-awesome-icon icon="fa-solid fa-ellipsis-vertical" />
          <font-awesome-icon icon="fa-solid fa-ellipsis-vertical"/>
          <font-awesome-icon icon="fa-solid fa-ellipsis-vertical"/>
        </div>
      </nav>
    </header>
    
    <body>
      <nav class="absolute top-0 z-50 h-auto" v-if="showMenu">
        <MenuItems/>
      </nav>
      <RouterView/>
    </body>    
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useGasStore } from '../src/store'
//import { useAuthUserStore } from '../src/store/auth.module'
import MenuItems from '../src/components/MenuItems.vue'
import {computed} from 'vue'

const store = useGasStore()
const openMenu = () => store.changeMenu(true)
const showMenu = computed(() => store.showMenu)
</script>
