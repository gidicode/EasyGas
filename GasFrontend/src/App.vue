<template>
  <div>
    <header class="container-lg bg-[#7000FF] mx-auto px-8">
      <nav class="flex justify-between pt-3 pb-3">
        <div class="">
          <RouterLink to="/" class="font-bold text-white"> EasyGas </RouterLink>
        </div>

        <div class="text-white space-x-0.5">
          <font-awesome-icon icon="fa-solid fa-ellipsis-vertical" />
          <font-awesome-icon icon="fa-solid fa-ellipsis-vertical"/>
          <font-awesome-icon icon="fa-solid fa-ellipsis-vertical"/>
        </div>
      </nav>
    </header>
    <body>
      <WelcomePage/>
    </body>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import WelcomePage from '../src/views/WelcomePage.vue'
</script>
