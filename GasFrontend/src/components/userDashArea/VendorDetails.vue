<template>
    <div>
        <header class="flex justify-between mt-5">
            <div> <p class="text-black">hello</p></div>
            
        </header>

        <section>
            <h2>VENDOR</h2>
            <h6>Vendor Details</h6>
            <hr>

            <button @click="showRefill" class="rounded-xl bg-[#A589C9] w-56 h-11 text-white mb-6 mt-6 font-medium">REQUEST REFILL</button>
        </section>

        <section class="">
            <h2> Biggins Gas Calabar</h2>
            <p> No 15 new load street by highway.</p>
            <p> +234 7048567129 </p>
            <p> +234 8047850193</p>

            <p class="mt-3 border-2 p-4 text-sm ">
                We refill gas cylinder at an affordable rate at your door step,
                we have several dispatch ready for pickup
            </p>

            <h6 class="mt-4">CURRENT PRICE P/KG: N750</h6>
             
             <table>
                <thead>
                    <tr> Deliveries</tr>
                    <tr> Rating </tr>
                    <tr> Opening Hours</tr>
                    <tr> Closing Hours</tr>
                </thead>
                <tbody>
                    <tr>50</tr>
                    <tr> 5555</tr>
                    <tr>08:00AM</tr>
                    <tr>06:00PM</tr>
                </tbody>
             </table>

             <div class="grid grid-cols-2 place-items-center mt-4">
                <div>
                    <button class="rounded-xl bg-[#D60097] p-3 text-white"> Unfavourite</button>
                </div>
                <div>
                    <button class="rounded-xl bg-[#D60097] p-3 text-white"> Chat</button>
                </div>
             </div>
        </section>

        <section v-if="refillRequest" class="absolute top-0 right-0 z-50 h-screen">
            <RefillRequestSent />
        </section>
    </div>
</template>


<script setup>
import { ref } from "vue";
import RefillRequestSent from "../userDashArea/RefillRequestSent.vue"

const refillRequest = ref(false)
const showRefill = () => (refillRequest.value = true)
</script>