<template>
    <div>
        <font-awesome-icon @click="historyBack" class="text-sm text-[#6C439E] cursor-pointer" icon="fa-solid fa-arrow-left" />
    </div>
</template>

<script setup>
import { useRouter } from "vue-router"

const router = useRouter()
const historyBack = () => router.go(-1)
</script>