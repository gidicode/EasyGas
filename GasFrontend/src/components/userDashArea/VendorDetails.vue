<template>
  <div>
    <header class="flex justify-between mt-5">
      <div>
        <history-back />
      </div>
    </header>

    <div class="grid grid-cols-1 justify-items-center">
      <p class="text-8xl text-[#472154] absolute top-20">
        <font-awesome-icon icon="fa-solid fa-circle-user" />
      </p>
      <div class="bg-slate-50 shadow-md max-w-lg p-5 rounded-2xl mt-4 mb-10">
        <section class="mt-6 flex flex-col items-center">
          <div>
            <h2 class="text-3xl font-extrabold">Biggins Gas Calabar</h2>
          </div>

          <button
            @click="showRefill"
            class="rounded-xl bg-[#3B0087] w-6/12 h-12 text-white mt-8 font-medium"
          >
            REQUEST REFILL
          </button>
        </section>

        <section class="ml-5 mt-8">
          <div class="flex justify-start">
            <p class="text-[#FF00B5] mr-2">
              <font-awesome-icon icon="fa-solid fa-location-arrow" />
            </p>
            <p>No 15 new load street by highway.</p>
          </div>

          <div class="flex justify-start">
            <p class="text-[#FF00B5] mr-2">
              <font-awesome-icon icon="fa-solid fa-square-phone" />
            </p>
            <p>+234 7048567129</p>
          </div>

          <div class="flex justify-start">
            <p class="text-[#FF00B5] mr-2">
              <font-awesome-icon icon="fa-solid fa-square-phone" />
            </p>
            <p>+234 7048567129</p>
          </div>

          <p
            class="mt-8 border-2 w-full border-[#3B0087] p-4 text-[#3B0087] text-sm"
          >
            We refill gas cylinder at an affordable rate at your door step, we
            have several dispatch ready for pickup.
          </p>

          <h6 class="mt-7 font-bold text-[#7FE3A7]">
            CURRENT PRICE PER/KG: <span class="text-[#00A743]">N750</span>
          </h6>

          <table
            class="w-full table-auto border-collapse border border-slate-500 mt-7"
          >
            <tbody>
              <tr>
                <td class="border border-[#3B0087] p-1">Deliveries</td>
                <td class="border border-[#3B0087] p-1">50</td>
              </tr>
              <tr>
                <td class="border border-[#3B0087] p-1">Rating</td>
                <td class="border border-[#3B0087] p-1">
                  <vue3starRatings
                    v-model="rating"
                    :starSize="15"
                    :showControl="false"
                    :disableClick="true"
                    class="ratingsUpdate"
                  />
                </td>
              </tr>
              <tr>
                <td class="border border-[#3B0087] p-1">Opening Hours</td>
                <td class="border border-[#3B0087] p-1">08:00 AM</td>
              </tr>
              <tr>
                <td class="border border-[#3B0087] p-1">Closing Hours</td>
                <td class="border border-[#3B0087] p-1">08:00PM</td>
              </tr>
            </tbody>
          </table>

          <div class="grid grid-cols-2 place-items-center mt-7 mb-3">
            <div class="w-full mr-5">
              <button class="rounded-xl bg-[#4F2585] p-3 w-full text-white">
                Unfavourite
              </button>
            </div>
            <div class="w-full">
              <button class="rounded-xl bg-[#D60097] p-3 w-full text-white">
                Chat
              </button>
            </div>
          </div>
        </section>

        <section
          v-if="refillRequest"
          class="absolute top-0 right-0 z-50 h-screen"
        >
          <RefillRequestSent />
        </section>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import HistoryBack from "../userDashArea/HistoryBack.vue";
import RefillRequestSent from "../userDashArea/RefillRequestSent.vue";
import vue3starRatings from "vue3-star-ratings";

const refillRequest = ref(false);
const showRefill = () => (refillRequest.value = true);
const rating = ref(4);
</script>

<style scoped>
.ratingsUpdate {
  margin: 0px auto;
  padding: 0px;
  position: relative;
  right: 45px;
}
</style>
