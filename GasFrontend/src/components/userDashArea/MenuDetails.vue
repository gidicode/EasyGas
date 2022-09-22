<!-- eslint-disable prettier/prettier -->
<template>
    <div class="flex justify-between">
        <div class="">
            <p v-if="loading"></p>
            <p v-else class="text-xs text-[#FF00B5]">Welcome {{ currentUser.username }}</p>                        
        </div>        

        <div class="w-14">
            <div class="flex justify-between">
                <div class="text-[#CEA8FF] text-base">
                    <font-awesome-icon icon="fa-solid fa-bell" class="mr-5" />
                </div>
                <div class="text-[#CEA8FF] text-base">
                    <RouterLink to="/dashboard/user-profile">
                    <font-awesome-icon icon="fa-solid fa-circle-user" />
                    </RouterLink>
                </div>               
            </div>                        
        </div>
    </div>
</template>

<script setup>
import { useGasStore } from "../../store"
import { computed } from "vue";
import { RouterLink } from "vue-router";

const store = useGasStore()
store.getCurrentUser()
const currentUser = computed(() => store.currentUserData)
const loading = computed(()=> store.loading);
</script>
