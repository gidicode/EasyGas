<!-- eslint-disable prettier/prettier -->
<template>
    <div class="flex justify-between">
        <div class="">
            <p class="text-xs text-[#FF00B5]">Welcome {{ currentUser.username }}</p>            
            
        </div>        

        <div class="w-14">
            <div class="flex justify-between">
                <div class="text-[#CEA8FF] text-base">
                    <font-awesome-icon icon="fa-solid fa-bell" class="mr-5" />
                </div>
                <div class="text-[#CEA8FF] text-base">
                    <font-awesome-icon icon="fa-solid fa-circle-user" />
                </div>               
            </div>                        
        </div>
    </div>
</template>

<script setup>
import {useAuthUserStore} from '../../store/auth.module'
import { computed } from 'vue'

const authStore = useAuthUserStore()

const currentUser = computed(() => authStore.state.user)
</script>