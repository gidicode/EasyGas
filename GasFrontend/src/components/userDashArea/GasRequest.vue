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
                <h2 class="text-xl text-[#9062CB] font-bold">Gas Request</h2>
                <p class="text-xs text-[#3B0087] mb-4">View all your gas request and their status</p>

                <hr>

                <div class="bg-[#F3E9FF] mt-5 p-1.5">
                    <section class="flex flex-row justify-between px-3 mb-0.5">
                        <div>
                            <p class="font-bold text-xs  text-[#7C57AA]">10KG</p> 
                        </div>
                        <div>
                            <p class="font-bold text-xs text-[#FF00B5]">Pending</p>
                        </div>
                    </section>

                    <section class="flex flex-row justify-between px-3 mb-0.5">
                        <div>
                            <p class="text-xs  text-[#7C57AA]">Roph Gas Calabar</p> 
                        </div>
                        <div>
                            <p class=" text-xs text-[#7C57AA]">12-05-2022</p>
                        </div>
                    </section>

                    <section class="flex flex-row justify-between px-3">
                        <div>
                            <p class="text-xs  text-[#7C57AA]">N 780</p> 
                        </div>
                    </section>
                </div>

                <div class="bg-[#F3E9FF] mt-2 p-1.5">
                    <section class="flex flex-row justify-between px-3 mb-0.5">
                        <div>
                            <p class="font-bold text-xs  text-[#7C57AA]">10KG</p> 
                        </div>
                        <div>
                            <p class="font-bold text-xs text-[#FF00B5]">Pending</p>
                        </div>
                    </section>

                    <section class="flex flex-row justify-between px-3 mb-0.5">
                        <div>
                            <p class="text-xs  text-[#7C57AA]">Roph Gas Calabar</p> 
                        </div>
                        <div>
                            <p class=" text-xs text-[#7C57AA]">12-05-2022</p>
                        </div>
                    </section>

                    <section class="flex flex-row justify-between px-3">
                        <div>
                            <p class="text-xs  text-[#7C57AA]">N 780</p> 
                        </div>
                    </section>
                </div>

                <div class="bg-[#F3E9FF] mt-2 p-1.5">
                    <section class="flex flex-row justify-between px-3 mb-0.5">
                        <div>
                            <p class="font-bold text-xs  text-[#7C57AA]">10KG</p> 
                        </div>
                        <div>
                            <p class="font-bold text-xs text-[#FF00B5]">Pending</p>
                        </div>
                    </section>

                    <section class="flex flex-row justify-between px-3 mb-0.5">
                        <div>
                            <p class="text-xs  text-[#7C57AA]">Roph Gas Calabar</p> 
                        </div>
                        <div>
                            <p class=" text-xs text-[#7C57AA]">12-05-2022</p>
                        </div>
                    </section>

                    <section class="flex flex-row justify-between px-3">
                        <div>
                            <p class="text-xs  text-[#7C57AA]">N 780</p> 
                        </div>
                    </section>
                </div>               
            </div>
        </section>

        <div class="absolute inset-0 z-50 " v-if="detailState">            
            <GasRequestDetails
            @hide-gas-request-detail="hideDetailState"
            />                
        </div>
    </div>
</template>

<script setup>
import GasRequestDetails from "../userDashArea/GasRequestDetails.vue"
import { ref } from "vue"
import HistoryBack from "../userDashArea/HistoryBack.vue"

const detailState = ref(true)
const hideDetailState = () => (detailState.value = false)

</script>