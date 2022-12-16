<template>
  <div>
    <header class="flex justify-between mt-5">
      <div>
        <history-back />
      </div>
      <div>        
        ****
      </div>
    </header>

    <div class="px-40">
      <h2 class="text-3xl text-[#9062CB] font-bold">VENDORS</h2>
      <p class="text-sm text-[#9062CB]">
        Select a vendor you want to refill gas from around your area.
      </p>

      <RouterLink to="/dashboard/vendor-details">
        <section
          class="grid grid-cols-3 shadow hover:shadow-lg place-items-stretch mt-10 bg-white border-l-4 border-[#472174] text-base pl-3"
        >
          <div class="mt-3 mb-3">
            <h6 class="text-lg text-[#9062CB]">Biggins Gas Vendor..</h6>
            <span>
              <p class="text-base text-[#9062CB] font-extrabold">N700</p>
            </span>
          </div>

          <div class="mt-4 mb-3">
            <vue3starRatings
              v-model="rating"
              :starSize="20"
              :showControl="false"
              :disableClick="true"
              class="ratingsUpdate"
            />
          </div>

          <div class="mt-4 mb-3">
            <p class="text-3xl text-center text-[#472174]"> 
              <font-awesome-icon icon="fa-solid fa-circle-user" /> 
            </p> 
          </div>
        </section>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import HistoryBack from "../userDashArea/HistoryBack.vue";
import vue3starRatings from "vue3-star-ratings";
import { ref } from "vue";

const rating = ref(0);
</script>

<style scoped>
.ratingsUpdate {
  margin: 0px auto;
  padding: 0px;
}
</style>
