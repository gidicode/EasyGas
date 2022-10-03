<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <header class="flex justify-between mt-5">
            <div> 
                <history-back/>
            </div>
            <div>                 
                <font-awesome-icon class="text-[#6C439E] text-sm mr-1" icon="fa-solid fa-magnifying-glass" /> 
                <span class="text-sm text-[#6C439E] cursor-pointer">Search</span>
            </div>
        </header>   

        <section class="grid grid-cols-1 place-items-center mt-5">
            <div class="w-6/12">
                <h2 class="text-xl text-[#9062CB] font-bold">VENDORS</h2>
                <p class="text-sm text-[#3B0087] mb-4">All favourite vendors saved. 
                    <span> 
                    <font-awesome-icon icon="fa-solid fa-heart-circle-check" />
                    </span>
                </p>
                
                <hr>

                <div class="bg-[#F3E9FF] mt-5 p-1.5 hover:border-sky-500 border-l-4">
                    <section class="flex flex-row justify-between px-3 mt-2 mb-0.5">
                        <div>
                            <p class="font-bold text-base text-[#7C57AA]">Bigins Gas C...</p> 
                        </div>
                        <div>
                             <vue3starRatings
                                v-model="rating"
                                :starSize="23"
                                :showControl=false
                                :disableClick=true 
                                class="ratingsUpdate"                                                                                                                                                                       
                            />  
                        </div>
                        <div>
                            <font-awesome-icon class="text-2xl" icon="fa-solid fa-circle-user" />
                        </div>
                    </section>

                    <section class="flex flex-row justify-between px-3 mb-0.5">
                        <div>
                            <p class="text-xs text-[#7C57AA]">Current Price: N750</p> 
                        </div>                        
                    </section>                   
                </div>                         
            </div>
        </section>       
    </div>
</template>

<script setup> 
import { ref } from "vue"
import vue3starRatings from "vue3-star-ratings"
import HistoryBack from "../userDashArea/HistoryBack.vue"

const rating  = ref(4)
</script>

<style scoped>
.ratingsUpdate{
    margin: 0px auto;
    padding: 0px;
}
</style>