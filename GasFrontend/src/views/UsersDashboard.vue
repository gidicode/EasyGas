<!-- eslint-disable prettier/prettier -->
<template>
    <main class="container-lg mt-2">
        <header class="px-8">
           <MenuDetails/>
        </header>
        <section class="px-8">
            <RouterView/>
        </section>
    </main>
</template>

<script setup>
import { RouterView } from 'vue-router'
import MenuDetails from '../components/userDashArea/MenuDetails.vue'
</script>